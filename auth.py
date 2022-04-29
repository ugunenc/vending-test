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


def log_level():
    level = os.getenv("VENDING_LOG_LEVEL", '0')

    if level == '0':
        from dotenv import load_dotenv

        load_dotenv()
        level = os.getenv("VENDING_LOG_LEVEL", '0')

    try:
        level = int(level)
    except Exception as e:
        level = 0

    return level
