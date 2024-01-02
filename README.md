# KAMIAirlines 
Virtual airlines of KAMI


## Installation Tutorial


### Requirements:

Before proceed please ensure you already have the requirements below installed on your system:
- Python 3+
- Git


### Clone the code

Open your teminal, then copy the line below and paste it on your terminal
git clone https://github.com/aguseka/KAMIAirlines.git

go into that folder by typing this command.
cd KAMIAirlines

### Create a Python Virtual Environment

python3 -m venv env


### Activate the Virtual Environment

source env/bin/activate


### Install the requirements

pip install -r requirements.txt


###  Run Django


python manage.py makemigrations
python manage.py migrate
python manage.py create superuser
python manage.py runserver


### Test The API

localhost:8000/swagger or
localhost:8000/api

