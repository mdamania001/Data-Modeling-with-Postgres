# DROP TABLES

songplay_table_drop = ""
user_table_drop = ""
song_table_drop = ""
artist_table_drop = ""
time_table_drop = ""

# CREATE TABLES

#num_songs:1
#artist_id:"ARD7TVE1187B99BFB1"
#artist_latitude:null
#artist_longitude:null
#artist_location:"California - LA"
#artist_name:"Casual"
#song_id:"SOMZWCG12A8C13C480"
#title:"I Didn't Mean To"
#duration:218.93179
#year:0
  

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time TIMESTAMP,
    user_id INTEGER,
    level VARCHAR(10),
    song_id VARCHAR(20),
    artist_id VARCHAR(20),
    session_id INTEGER,
    location VARCHAR(50),
    user_agent VARCHAR(150)
);
""")

user_table_create = ("""
""")

song_table_create = ("""
""")

artist_table_create = ("""
""")

time_table_create = ("""
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
