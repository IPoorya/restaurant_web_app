# Restaurant Web App

this project demonstrated how to handle user orders using Django as the back-end.

front-end is developed by Django templates. UI/UX was not the purpose of this project so it's not responsive and something exceptional. 

user authentication is just there and has nothing to do with submitting orders. OTP functionality is implemented but it's not connected to any SMS service. you can read the OTP code from the admin panel.

## Setup

The first thing to do is to clone the repository:

```bash
https://github.com/IPoorya/restaurant_web_app
cd restaurant_web_app
```
Create a virtual environment to install dependencies in and activate it:
```bash
python3 -m venv env
source env/bin/activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```
Once pip has finished downloading the dependencies, create migrations and apply them:
```bash
python manage.py makemigrations
python manage.py migrate
```

and run server:
```bash
python manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.