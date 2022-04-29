from flask import Flask, json, request
from flask_basicauth import BasicAuth
from auth import auth, log_level
from vending import Vending
import logging

api = Flask(__name__)

auth_user, auth_password = auth()
api.config['BASIC_AUTH_USERNAME'] = auth_user
api.config['BASIC_AUTH_PASSWORD'] = auth_password
basic_auth = BasicAuth(api)

logging.basicConfig(level=log_level(), format='%(asctime)s :: %(levelname)s :: %(message)s')


@api.route('/', methods=['GET'])
def get_check_free_time():
    logging.info("GET /")
    vending = Vending()
    logging.info("Free drink time: " + vending.free_time)
    return json.dumps({
        "status": "ok",
        "msg": "Free drink time: " + vending.free_time
    }), 200


@api.route('/set_free_time', methods=['POST'])
@basic_auth.required
def set_free_time():
    vending = Vending()
    new_free_time = request.json["free_time"]
    logging.info("GET /set_free_time " + new_free_time)
    if new_free_time:
        try:
            vending.free_time = new_free_time
            logging.info("New free time: " + vending.free_time)
            return json.dumps({
                "msg": "New free time: " + vending.free_time
            }), 200
        except Exception as e:
            logging.warning(e)
            return json.dumps({
                "msg": e
            }), 400
    else:
        logging.warning("Wrong free_time parameter. ex Mon: 1200-1400 Tue: 0900-1100 Fri: 0000-2400")
        return json.dumps({
            "msg": "Wrong free_time parameter. ex Mon: 1200-1400 Tue: 0900-1100 Fri: 0000-2400"
        }), 400


@api.route('/drink', methods=['GET'])
def get_drink():
    logging.info("GET /drink")
    vending = Vending()
    if vending.check_free_time():
        logging.info("Drinks on the house")
        return json.dumps({
            "msg": "Drinks on the house"
        }), 200
    else:
        logging.info("You have to pay for this drink")
        return json.dumps({
            "msg": "You have to pay for this drink"
        }), 200


if __name__ == '__main__':
    from waitress import serve
    serve(api, host="0.0.0.0", port=5000)
