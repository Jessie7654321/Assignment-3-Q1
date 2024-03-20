We need  PostgreSQL Python 3 psycopg2 library (for Python)
Install PostgreSQL 
Create a Database and User and log into the PostgreSQL CLI using psql -U postgres, then run the sql:
CREATE DATABASE mydatabase;
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
Clone this project to local machine with "git clone <repository-url>"
Navigate to the project directory and install the required Python libraries. (use "pip install psycopg2-binary")
Configure Database Connection: Update the database connection parameters in the Python script (dbname, user, password, host, port) to match your PostgreSQL setup.
Run the Application
Use the command-line prompts to add, view, update, or delete student records.
