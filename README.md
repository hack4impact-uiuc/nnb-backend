# NNB Map Board 

Restful API using Flask <br>
Dependencies:
- Python 3.x
- pip 9.0
- PostgreSQL 

## Setup 
If your developing with Windows, ¯\\_(ツ)_/¯ <br>
To install Postgres with Homebrew([postgresapp](http://postgresapp.com/) also works):
```
$ brew install postgresql
$ brew link postgresql
```
This should start your postgres server(Ctrl-C to stop):
```
$ postgres -D /usr/local/var/postgres
```
It should say ```listening on IPv6 address "::1", port 5432``` If not, change the port. On a separate CLI:
```
$ createdb
$ psql -h localhost
```
Always remember to use the same virtual environement!!!! This is a good practice for any python development. <br>
First, install virtualenv, create and activate the environment called **venv**, and install the python package dependencies:
```bash
pip3 install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
To deactivate when you're using it:
```
$ deactivate venv
```
After installing Postgres, in your CLI create a user and database and grant privileges:
```
$ psql
# create user nbb with password 'password';
# create database nbb_db owner nbb encoding 'utf-8';
# GRANT ALL PRIVILEGES ON DATABASE nbb_db TO nbb;
```


## Run Development Server
To run the server, make sure you are in the root directory:
```
python run.py
```

The API should be at http://127.0.0.1:5000/ for you to experience its beauty LOL 

## Database Schema Changes
The Database Schema is described in ```models.py```. For any changes you make, you MUST let everyone know about it. First, create migration files for your changes:
```
$ python manage.py db migrate 
```
This will be reflected in ```/migrations```. Then, upgrade the database and let everyone know to do to.
```
$ python manage.py db upgrade
```
Everyone will have to follow this same process whenever someone pushes new changes to ```models.py```. Migration files will not be pushed into the main repo due to versioning complaints.
## Heroku Deployment
You must have a Heroku Account and have the Heroku CLI installed on your computer. First, create an application in your Heroku dashboard, click on the "Deploy" tab and find the ```git remote add ....``` and run that command in your repository. While you're still in your Heroku Dashboard, click add "Heroku Postgres". This will add a Postgres Database to your app(we will connect it later).\n
Then, login into heroku in your command line:
```
$ heroku login
```
To double check whether you have the postgres add-on:
```
$ heroku addons
```
And you should get something with ```heroku-postgresql (postgresql-metric-75135)```\n
We will then connect the Heroku Postgres Database to the App in Heroku. Until I implement a better way to do this, we will have to comment out ```SQLALCHEMY_DATABASE_URI = 'postgresql://nbb:password@127.0.0.1:5432/nbb_db'``` and uncomment ```SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')``` in config.py \n
Then commit it and push it to heroku: 
```
$ git commit config.py -m "changing database uri for heroku deployment"
$ git push heroku master
```
After pushing your app to heroku, you need to migrate and update heroku postgres:
```
$ heroku run bash
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
A pretty neat command to go into the heroku postgres CLI is:
```
$ heroku pg:psql
```
## Git Flow 
Before you start making changes, make sure you have the most recently updated version of `master`:
```
git pull
```

Make a new branch for your changes:
```
git checkout -b <branch_name>
```

If you want to see all of your branches that exist:
```
git branch
```

If you want to switch to a branch that already exists:
```
git checkout <branch_name>
```

Make sure you commit your changes to your own branch! 

Push your code and submit a PR to leave it up for review:
```
git push
```
This might walk you through some remote branch push settings, just follow what it says. It should only happen the first time you push to a new branch

Then go to this repo on Github, refresh the page, and you should see an option to create a pull request from your branch.
## Code Reviews
It is recommended to:
1) Keep PRs small and manageable
2) Put up a PR early on (even before it is ready for review), so you can get early feedback

### Labels:
#### `In Progress` 
Use this while you are working on your changes. Reviewers can take a look to make sure you're on the right track and make some suggestions along the way. Also use this as a way to ask questions about your code (_Is this the right way to do x?, Does this follow conventions properly?, etc._).

#### `Ready For Review`
Use this when you feel like your code is ready to be thoroughly reviewed before shipping. Assign your PR to your technical lead and teammates who know more about the areas you worked on (Github might have suggestions based on previous contributions).

#### `In Review`
Reviewers, set this to indicate the PR is currently being reviewed.

#### `SHIP IT`
Reviewers, set this to indicate the PR is ready to be merged, but let the pull requester do the merging.

PRs can't be merged without at least one reviewer approving your changes. If waiting on your reviewer becomes a blocker, bug them about it!

## Conventions
- **Controllers**, which describe API endpoints will be defined under ``api/views/*``. We will be using [Flask Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) for easier collaborations in view controllers. Be sure to know how to use them. <br>
- The **Database** Structure will be defined under ``api/models.py``

## MISC

If you're annoyed by the __pycache__ files 
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

Feel free to contact me for questions :) 
