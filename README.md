# SkySpectra

SkYSpectra is a weather app build using django and openweathermap API.
Web App Link: http://yashagrahari07.pythonanywhere.com/
![image](https://user-images.githubusercontent.com/92152225/215326154-98187b0b-3542-4183-ad83-03a1ced3a2ff.png)

## Installation
we need to first create a virtual environment to run our django app.

```bash
py -m venv virtualenv
```
To activate virtual environment:
```bash
virtualenv\Scripts\activate.bat
```
After activating virtual environment, we need to install django in virtual environment.
```bash
pip install django
```
To deactivate virtual environment:
```bash
deactivate
```
After creation of virtual environment and django installation, just clone the repository inside virtual environment. 

## Usage
To run django server:
```bash
python manage.py runserver
```
After running the server, our web app will be successfully run.

## Note
This repository does not have django security keys, due to security reasons.
Therefore, it will throw error while running.

## Future Goals
Since, Till now our project can tell the weather of a city but if the city does not exist then it will throw a error.
So further, we are seeking to solve this problem.
