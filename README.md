# VDO-Summarizer-Backend
https://github.com/anthonypiegaro/VDO-Summarizer-Backend/assets/84252391/7bcf8735-c77a-4ff8-bcf9-3a65b3fb1516
## Background Info
Vdo Summarizer is a web app that creates Youtube video summaries for users. This repo is for the backend. Go to the [VDO-Summarizer-Frontend](https://github.com/anthonypiegaro/VDO-Summarizer-Frontend) if you want the frontend for this web app.
### Features
1. Youtube Video Summarization
2. Past Summaries Archive
3. User Registration and Login
## Getting Started
### Cloning
To get started, clone the repo by running the following in the command line:
```
git clone https://github.com/anthonypiegaro/VDO-Summarizer-Backend.git
```
### Virtual Environment
After cloning, I would also recommend creating a [Python Virtual Environment](https://docs.python.org/3/library/venv.html). This can be done by running the follwing:
```
python3 -m venv venv
```
Then, you should activate your newly created virtual environment. You can do this by running the following in the command line:  
For Mac users
```
source venv/bin/activate
```
For Windows users
```
venv\Scripts\activate
```
Now, your virtual environment should be activated.
### Downloading Dependencies
For this project, there a few dependencies that will be needed in order for the project to run. These dependencies are stored in the requirements.txt file. Luckly, it is very easy to download these to your virtual environment.
```
pip3 install -r requirements.txt
```
You now should have all the dependencies downloaded and ready to go.
### Environment Variables
This app uses environment variables for security. Thus, you will need to add these to your environment.
#### Django Secret Key
You will need to create a Django secret key for your app. In Django, the "secret key" is a crucial piece of information used for security purposes, particularly for cryptographic functions such as hashing passwords and creating security tokens. Thus, you will need to create one and store it in your environment variables. To do so, you can create your own, or use a tool to create one, such as [Random.org](https://www.random.org/strings/). Once you get your secret key, you will set it in your environment variables, storing it with the variable name DJANGO_SECRET_KEY. To do this, you can run the following in the command line:  
On Mac
```
export DJANGO_SECRET_KEY=your_secret_key_here
```
On Windows
```
set DJANGO_SECRET_KEY=your_secret_key_here
```
#### OpenAI API Key
This app also relies on the [OpenAI API](https://openai.com/blog/openai-api), thus follow the link to get started with theor api, and create your API key. Once you have your API key, set it to the OPENAI_API_KEY variable. To do this, you can run the following in the command line:  
On Mac
```
export OPENAI_API_KEY=your_openai_api_key
```
On Windows
```
set OPENAI_API_KEY=your_openai_api_key
```
### Running Django
#### Running Locally
The app is ran with [Django](https://www.djangoproject.com/). To run the app, you will have to do some set up. First, you will need to get your database set up. You can do this by running the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
Next, I would suggest creating a superuser to start utilizing Django's features. To do this run the following in the command line:
```
python3 manage.py createsuperuser
```
Prompts will follow and ask you to create your user. After this, you will be set up to start the app locally. To start the local server, run the following in the command line:
```
python3 manage.py runserver
```
Now the backend should be up and running, and you can use your superuser account to login.
#### Deploy with Heroku
The app is currently set up to be deployed on [Heroku](https://www.heroku.com/). You can follow the [Heroku Python docs](https://www.heroku.com/python) to get set up with deploying a Django app with Heroku.
## Thank you
I hope you enjoy!
