# Vending machine test to give free drinks 

## Installation
Python 3.8.3
```bash
python -m pip install -r requirements.txt
```

Add "VENDING_FREE_TIME, VENDING_USER, VENDING_PASSWORD, VENDING_LOG_LEVEL" to system environment 

```bash
export VENDING_FREE_TIME="Mon: 1200-1400 Tue: 0900-1100 Fri: 0000-2400"
export VENDING_USER="us3r"
export VENDING_PASSWORD="p4ssw0rd"
```

####Log level
CRITICAL = 50 \
ERROR = 40 \
WARNING = 30 \
INFO = 20 \
DEBUG = 10 \
NOTSET = 0
```bash
export VENDING_LOG_LEVEL="10"
```

### Run

```bash
python app.py
```

### Get free drink hours

Request GET method to get free drink hours 

```bash
curl http://127.0.0.1:5000/
```


### Try to get free drink

Request GET method to '/drink' to get free drink. If it is in time range you can get free drink.
 
```bash
curl http://127.0.0.1:5000/drink 
```

### Set free drink hours

Request POST method to 'set_free_time' to set free time range. You can set time range for one or more days

```bash
curl -X POST -u us3r:p4ssw0rd  -H "Content-Type: application/json" \
     -d '{"free_time": "Fri: 1330-1450"}' \
     http://localhost:5000/set_free_time
```

