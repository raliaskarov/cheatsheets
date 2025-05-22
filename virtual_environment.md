# Commands to initiate, start and deactivate venv on python (Windows)

## Create venv
cd <PATH>
python -m venv env
.\env\Scripcts\activate # in windows
source env/bin/activate # in linux
pip intall -r requirements.txt

## Run app from venv
cd <PATH> & .\env\Scripts\activate & .\env\Scripts\streamlit run main.py
