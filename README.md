# NNB Map Board 
Restful API using Flask and Postgres for Neighborhood News Bureau's interactive map tool. check out the frontend, which uses React and calls this API. For deployment, Heroku is utilized for it's ease and simplicity for making changes. 

## Development Docs
- Development Docs are <a href="docs/other.md">here.</a><br>
- The list of endpoints and its functionality are located <a href="docs/endpoints.md">here.</a>

## Making Changes
Any changes that are pushed to master while be reflected in Heroku! Thus, just clone the repo and commit the changes.
```
git clone https://github.com/hack4impact-uiuc/nnb-backend.git
```
Then, push it to master! And that's it!
```
git push origin master
```
## Application Structure
- `api/` holds the database schema and view controllers. It is the application.
- `Procfile` and `runtime.txt` are for Heroku
- `requirements.txt` provides the list of python package dependencies required for this application
- `manage.py` and `config.py` defines the configuration for this app