# VDO-Summarizer-Backend
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
Now, you virtual environment should be activated.
### Downloading Dependecies
For this project, there a few dependencies that will be needed in order for the project to run. These dependencies are stored in the requirements.txt file. Luckly, it is very easy to download these to your virtual environment.
```
pip3 install -r requirements.txt
```
You now should have all the dependencies downloaded and ready to go.
### Running Django
#### Running Locally
The app is ran with [Django](https://www.djangoproject.com/). To run the app, you will have to do some set up. First, you will need to get your database set up. You can do this by 
#### Deploy with Heroku
The app is currently set up to be deployed on [Heroku](https://www.heroku.com/). You can follow the [Heroku Python docs](https://www.heroku.com/python) to get set up with deploying a Django app with Heroku.
## Thank you
I hope you enjoy!