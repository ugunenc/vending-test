import unittest
from vending import Vending
import datetime

date = datetime.datetime


class TestVending(unittest.TestCase):
    def test_validate_time(self):
        vending = Vending()
        # fail
        self.assertRaises(TypeError, vending.validate_time, 1)
        self.assertRaises(TypeError, vending.validate_time, True)
        self.assertRaises(TypeError, vending.validate_time, False)
        self.assertRaises(ValueError, vending.validate_time, "1")

        # success
        time = "Mon: 1204-1400 Tue: 0920-1100 Fri: 0000-2400 Sun: 2000-2400"
        self.assertTrue(vending.validate_time(time))

    def test_set_vending_free_time(self):
        vending = Vending()

        # fail
        time = "Mos: 1204-1400"
        self.assertRaises(ValueError, vending.set_free_time, time)

        # success
        time = "Mon: 1204-1400"
        vending.free_time = time
        self.assertEqual(time, vending.free_time)

    def test_check_free_time(self):
        vending = Vending()

        # fail
        # not today
        tomorrow = (date.today() + datetime.timedelta(days=1)).strftime("%A")[0:3]

        start_hour = date.now().hour - 2
        start_minute = date.now().minute
        if len(str(start_minute)) == 1:
            start_minute = "0" + str(start_minute)

        end_hour = date.now().hour - 1
        end_minute = date.now().minute
        if len(str(end_minute)) == 1:
            end_minute = "0" + str(end_minute)
        time = "{day}: {s_hour}{s_minute}-{e_hour}{e_minute}".format(day=tomorrow, s_hour=start_hour, s_minute=start_minute, e_hour=end_hour, e_minute=end_minute)
        print(time)
        print()
        vending.free_time = time
        self.assertFalse(vending.check_free_time())

        # today but not now
        today = date.today().strftime("%A")[0:3]
        start_hour = date.now().hour - 2
        start_minute = date.now().minute
        if len(str(start_minute)) == 1:
            start_minute = "0" + str(start_minute)

        end_hour = date.now().hour - 1
        end_minute = date.now().minute
        if len(str(end_minute)) == 1:
            end_minute = "0" + str(end_minute)

        time = "{day}: {s_hour}{s_minute}-{e_hour}{e_minute}".format(day=today, s_hour=start_hour, s_minute=start_minute, e_hour=end_hour, e_minute=end_minute)
        vending.free_time = time
        self.assertFalse(vending.check_free_time())

        # success
        today = date.today().strftime("%A")[0:3]
        start_hour = date.now().hour - 1
        start_minute = date.now().minute

        end_hour = date.now().hour + 1
        end_minute = date.now().minute
        if len(str(end_minute)) == 1:
            end_minute = "0" + str(end_minute)
        time = "{day}: {s_hour}{s_minute}-{e_hour}{e_minute}".format(day=today, s_hour=start_hour, s_minute=start_minute, e_hour=end_hour, e_minute=end_minute)
        vending.free_time = time
        self.assertTrue(vending.check_free_time())


if __name__ == '__main__':
    unittest.main()
