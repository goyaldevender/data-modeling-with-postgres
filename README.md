# Project Structure

1. **create_tables.py:** <br /> This file contains the python script which connects to the database, create schema("sparkifydb"), then executes a function to drop all the existing tables, and finally executes a function to create new tables.
2. **etl.py:** <br /> This file contains the python script which performs the ETL process, it reads and processes the song and log data and loads it into the appropriate tables in the sparkifydb.
3. **sql_queries.py:** <br /> This file contains all the SQL queries used in the project.
4. **test.py:** <br /> This file contains the test cases for checking the correctness of the ETL process and the data in the tables.
5. **README.md:** <br /> This file contains the instructions for setting up and running the project.
6. **Requirements.md:** <br /> This file contains the requirements specified for this project.

### Installing postgres
```
brew install postgresql
```

### Installing psycopg2
```
pip3 install psycopg2
```

### Starting postgres & creating required role
```
brew services start postgresql

psql postgres

postgres=# CREATE ROLE student WITH LOGIN PASSWORD 'student';

postgres=# ALTER ROLE student CREATEDB;
```

### Restarting postgres
```
brew services restart postgresql
```

### Python modules used
* **os:** This is used to list, split and join the filepath.
* **glob:** This is used to do pattern matching while listing files.