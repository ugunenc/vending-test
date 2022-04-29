import os


def auth():
    user = os.getenv("VENDING_USER", '')
    password = os.getenv("VENDING_PASSWORD", '')

    if user == '':
        from dotenv import load_dotenv

        load_dotenv()
        user = os.getenv("VENDING_USER", '')
        password = os.getenv("VENDING_PASSWORD", '')
        return user, password
    else:
        return user, password


