# Strativ :: Interview-Task

For run this project you can follow 2 step.If you have docker installed on your pc follow step 1 otherwise follow step 2. For step 2 you have to be pre-installed python and redis on your local machine.

Step 1: For run this project on docker container using docker-compose or docker compose you have follow below step,
    At first run this command on project folder
    - `cp .env.example .env` //copy .env file

    Then Run this command on project folder,
    - `sudo docker-compose up --build -d`

    -------That's all--------

Step 2: For run this project on local machine you have to start your redis server at first then you have follow below step,
    At first run this command on project folder
    - `cp .env.example .env` //copy .env file

    After then, Run this below command one by one on project folder,
    - `python -m venv venv` //for making virtual environment
    - `source venv/bin/activate` //activate the virtual environment on linux machine
    -`source venv/Scripts/activate` //activate the virtual environment on windows machine
    -`pip install -r requirements.txt` //install all requirements
    -`python manage.py migrate` // migrate schema and data on database
    -`python manage.py runserver` // run the project

    -------That's all--------

API Url example with required parameter and response sample,
1. Get Coolest 10 District:
    - http://127.0.0.1:8000/api/coolest_10_districts , method: get

2. Get recomendation:
    - http://127.0.0.1:8000/api/recomendation?location=1&destination=58&date=2023-10-24 , method: get
        response_style: 
        {
            "location_temp": 24.6,
            "destination_temp": 23.5,
            "recomendation": "The destination is cool. It's a good time to travel!"
        }