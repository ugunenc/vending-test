import os
import re
from datetime import datetime as date, time
from auth import log_level
import logging

logging.basicConfig(level=log_level(), format='%(asctime)s :: %(levelname)s :: %(message)s')

string_error_message = "Time must be string! Ex: \"Mon: 1200-1400 Tue: 0900-1100 Fri: 0000-2400\" "


class Vending:
    def __init__(self):
        self._free_time = os.getenv("VENDING_FREE_TIME", '')
        self._regex = r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun):\s(((0|1)[0-9])|[2][0-4])(([0][0-9])|([1-5][0-9]))-(((0|1)[0-9])|[2][0-4])(([0][0-9])|([1-5][0-9]))"

        if self._free_time == '':
            from dotenv import load_dotenv

            load_dotenv()
            self._free_time = os.getenv("VENDING_FREE_TIME", '')

    def set_free_time(self, time):
        try:
            self.validate_time(time)
            self._free_time = time
            os.environ["VENDING_FREE_TIME"] = time
        except Exception as e:
            print(e)
            logging.error(string_error_message)
            raise ValueError(string_error_message)

    def get_free_time(self):
        return self._free_time

    def validate_time(self, time):
        if not isinstance(time, str):
            logging.error(string_error_message)
            raise TypeError(string_error_message)

        matches = re.finditer(self._regex, time)
        matches = tuple(matches)
        if len(matches) > 0:
            return True
        else:
            logging.error(string_error_message)
            raise ValueError(string_error_message)

    def check_free_time(self):
        matches = re.finditer(self._regex, self._free_time)
        matches = tuple(matches)
        for matchNum, match in enumerate(matches, start=1):
            today = date.today().strftime("%A")[0:3]
            if match.group().split(": ")[0] == today:
                hours = match.group().split(": ")[1]

                start_time = hours.split("-")[0]
                if start_time == "2400":
                    start_time = "2359"
                start_hour = int(start_time[0:2])
                start_minute = int(start_time[2:4])
                if len(str(start_minute)) == 1:
                    start_minute = int("0" + str(start_minute))
                start_time = time(start_hour, start_minute)

                end_time = hours.split("-")[1]
                if end_time == "2400":
                    end_time = "2359"
                end_hour = int(end_time[0:2])
                end_minute = int(end_time[2:4])
                if len(str(end_minute)) == 1:
                    end_minute = int("0" + str(end_minute))
                end_time = time(end_hour, end_minute)

                if start_time <= date.now().time() <= end_time:
                    return True
                else:
                    return False

        return False

    free_time = property(get_free_time, set_free_time)
