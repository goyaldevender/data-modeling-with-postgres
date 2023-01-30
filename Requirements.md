# Schema for Song Play Analysis

Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

#### Fact Table

1. **songplays** - records in log data associated with song plays i.e. records with page `NextSong`
  * _songplay\_id, start\_time, user\_id, level, song\_id, artist\_id, session\_id, location, user\_agent_

#### Dimension Tables

1. **users** - users in the app
  * _user\_id, first\_name, last\_name, gender, level_
2. **songs** - songs in music database
  * _song\_id, title, artist\_id, year, duration_
3. **artists** - artists in music database
  * _artist\_id, name, location, latitude, longitude_
4. **time** - timestamps of records in **songplays** broken down into specific units
  * _start\_time, hour, day, week, month, year, weekday_

# Project Template

To get started with the project, go to the workspace on the next page, where you'll find the project template files. You can work on your project and submit your work through this workspace. Alternatively, you can download the project template files from the Resources folder if you'd like to develop your project locally.

In addition to the data files, the project workspace includes six files:

1. `test.ipynb` displays the first few rows of each table to let you check your database.
2. `create_tables.py` drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
3. `etl.ipynb` reads and processes a single file from `song_data` and `log_data` and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4. `etl.py` reads and processes files from `song_data` and `log_data` and loads them into your tables. You can fill this out based on your work in the ETL notebook.
5. `sql_queries.py` contains all your sql queries, and is imported into the last three files above.
6. `README.md` provides discussion on your project.  
  
  

# Project Steps

---

> **NOTE:** You will not be able to run `test.ipynb`, `etl.ipynb`, or `etl.py` until you have run `create_tables.py` at least once to create the `sparkifydb` database, which these other files connect to.

Below are steps you can follow to complete the project:

### Create Tables
  1. Write `CREATE` statements in `sql_queries.py` to create each table.
  2. Write `DROP` statements in `sql_queries.py` to drop each table if it exists.
  3. Run `create_tables.py` to create your database and tables.
  4. Run `test.ipynb` to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.

### Build ETL Processes

Follow instructions in the `etl.ipynb` notebook to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run `test.ipynb` to confirm that records were successfully inserted into each table. Remember to rerun `create_tables.py` to reset your tables before each time you run this notebook.

### Build ETL Pipeline

Use what you've completed in `etl.ipynb` to complete `etl.py`, where you'll process the entire datasets. Remember to run `create_tables.py` before running `etl.py` to reset your tables. Run `test.ipynb` to confirm your records were successfully inserted into each table.

### Run Sanity Tests

When you are satisfied with your work, run the cell under the **Sanity Tests** section in the `test.ipynb` notebook. The cells contain some basic tests that will evaluate your work and catch any silly mistakes. We test column data types, primary key constraints and not-null constraints as well look for on-conflict clauses wherever required. If any of the test cases catches a problem, you will see a warning message printed in Orange that looks like this:
    
    [WARNING] The songplays table does not have a primary key! 

You may want to make appropriate changes to your code to make these warning messages go away. The tests below are only meant to help you make your work foolproof. The submission will still be graded by a human grader against the project rubric.

### Document Process
  1. Do the following steps in your `README.md` file.
    * Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
    * How to run the Python scripts
    * An explanation of the files in the repository
    * State and justify your database schema design and ETL pipeline.
    * \[Optional\] Provide example queries and results for song play analysis.
  2. Here's a [_https://www.markdownguide.org/basic-syntax/_](https://www.markdownguide.org/basic-syntax/)[guide](https://www.markdownguide.org/basic-syntax/) on Markdown Syntax.\*
  3. Provide `DOCSTRING` statement in each function implementation to describe what each function does.

# Project Rubric

Read the project [rubric](https://review.udacity.com/#!/rubrics/4792/view) before and during development of your project to ensure you meet all specifications.