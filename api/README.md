# API

This is simple API

## Prerequirements

Install packages using command below

```
sudo apt update && sudo apt install python3.11 python3.11-venv
```

## Run

Follow next steps:
1. Setup venv from current folder
```
../scripts/setup-venv.sh
```
2. Activate venv
```
source venv/bin/activate
```
3. Install deps
```
pip install -r requirements.txt
```
4. Run app
```
uvicorn src.main:app --host <HOST> --port 8080 --reload
```
How select host:
- For WSL use 0.0.0.0 and check 127.0.0.1 in browser
- For Linux or MacOS use 0.0.0.0 and check 0.0.0.0 in browser
- For Windows use localhost and check localhost in browser