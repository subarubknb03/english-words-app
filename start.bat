cd %~dp0
if not exist .env (
    python -m venv .env
    .env\Scripts\activate
    pip3 install --upgrade pip setuptools
    pip3 install -r .\windows\requirements.txt
    cd app
    python main.py
) else (
    .env\Scripts\activate
    cd app
    python main.py
)


