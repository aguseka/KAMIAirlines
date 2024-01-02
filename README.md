# KAMIAirlines 
Virtual airlines of KAMI


## Installation Tutorial
This tutorial should be applicable on MacOS, Linux or Windows.

### Requirements:

Before proceeding please ensure you already have the requirements below installed on your system:
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


### Change settings.py

Go to /airlines/ folder and find settings.py
Change this line:

SECRET_KEY="yoursecretkeyishere"
DEBUG=True

###  Run Django

Upon completion of donwload, please run this commands:

python manage.py makemigrations
python manage.py migrate
python manage.py create superuser

Follow the instructions. Please memorize the superuser name and the password, then run this command.

python manage.py runserver 



### Test The API
When it works and no error, you can open the links below.

localhost:8000/swagger or
localhost:8000/api

