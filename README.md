# Gene REST API

## Requirements
- Python3
- mysql
- the rest of the requirements are documented in requirements.txt

## Setup database from scratch
- Connect to your server in the terminal by entering `mysql -u username -p password`, replacing username and password with the username and password you have set up with mysql.
- Create a new database by entering `CREATE DATABASE rest_api;` - note that if you decide to change the name of the database from rest_api then you'll need to update the connection string in config.py to point to the new database name.
- Use the test-data.sql source file to populate the database with the tables and data used by this project, by entering `USE rest_api; SOURCE path/to/test-data.sql` where you'll need to substitute in the local path to the test-data.sql file.

## Run project
Run the API locally by entering `python main.py` in this project directory. The API should then be hosted locally at 127.0.0.1:5000.
To test, try making a request to http://127.0.0.1:5000/genes/JAG1 in the browser or Postman.
