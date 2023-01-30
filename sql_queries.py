# DROP TABLES

songplay_table_drop = 'DROP TABLE IF EXISTS songplays;'
user_table_drop = 'DROP TABLE IF EXISTS users;'
song_table_drop = 'DROP TABLE IF EXISTS songs;'
artist_table_drop = 'DROP TABLE IF EXISTS artists;'
time_table_drop = 'DROP TABLE IF EXISTS time;'

# CREATE TABLES

songplay_table_create = (
    'CREATE TABLE IF NOT EXISTS songplays ('
    '    songplay_id SERIAL PRIMARY KEY,'
    '    start_time BIGINT,'
    '    user_id INT,'
    '    level VARCHAR,'
    '    song_id VARCHAR,'
    '    artist_id VARCHAR,'
    '    session_id INT,'
    '    location VARCHAR,'
    '    user_agent VARCHAR'
    ');'
)

user_table_create = (
    'CREATE TABLE IF NOT EXISTS users ('
    '    user_id INT PRIMARY KEY,'
    '    first_name VARCHAR,'
    '    last_name VARCHAR,'
    '    gender VARCHAR,'
    '    level VARCHAR'
    ');'
)

song_table_create = (
    'CREATE TABLE IF NOT EXISTS songs ('
    '    song_id VARCHAR NOT NULL PRIMARY KEY,'
    '    title VARCHAR NOT NULL,'
    '    artist_id VARCHAR NOT NULL,'
    '    year INT,'
    '    duration FLOAT'
    ');'
)

artist_table_create = (
    'CREATE TABLE IF NOT EXISTS artists ('
    '    artist_id VARCHAR NOT NULL PRIMARY KEY,'
    '    name VARCHAR NOT NULL,'
    '    location VARCHAR,'
    '    latitude FLOAT,'
    '    longitude FLOAT'
    ');'
)

time_table_create = (
    'CREATE TABLE IF NOT EXISTS time ('
    '    start_time BIGINT PRIMARY KEY,'
    '    hour INT,'
    '    day INT,'
    '    week INT,'
    '    month INT,'
    '    year INT,'
    '    weekday INT'
    ');'
)

# INSERT RECORDS

songplay_table_insert = ('\n'
                         '    INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id,\n'
                         '                           artist_id, session_id, location, user_agent)\n'
                         '    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s);\n')

user_table_insert = ('\n'
                     '    INSERT INTO users (user_id, first_name, last_name, gender, level)\n'
                     '    VALUES (%s, %s, %s, %s, %s)\n'
                     '    ON CONFLICT (user_id) DO UPDATE'
                     '    SET level = EXCLUDED.level;\n')

song_table_insert = ('\n'
                     '    INSERT INTO songs (song_id, title, artist_id, year, duration)\n'
                     '    VALUES (%s, %s, %s, %s, %s)\n'
                     '    ON CONFLICT DO NOTHING;\n')

artist_table_insert = ('\n'
                       '    INSERT INTO artists (artist_id, name, location, latitude, longitude)\n'
                       '    VALUES (%s, %s, %s, %s, %s)\n'
                       '    ON CONFLICT DO NOTHING;\n')

time_table_insert = ('\n'
                     '    INSERT INTO time (start_time, hour, day, week, month, year, weekday)\n'
                     '    VALUES (%s, %s, %s, %s, %s, %s, %s)\n'
                     '    ON CONFLICT DO NOTHING;\n')

# FIND SONGS

song_select = ('\n'
               '    SELECT s.song_id, a.artist_id\n'
               '    FROM songs s\n'
               '    JOIN artists a ON s.artist_id = a.artist_id\n'
               '    WHERE s.title = %s AND a.name = %s AND s.duration = %s;\n')

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
