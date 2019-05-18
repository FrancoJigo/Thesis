import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()
        
 # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
def write_blob(species_id,species_name, path_to_file):
    """ insert a BLOB into a table """
    conn = None
    try:
        # read data from a picture
        image = open(path_to_file, 'rb').read()
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("INSERT INTO species_1(species_1_id,species_1_name, image) " +
                    "VALUES(%s,%s,%s)",
                    (species_id, species_name,psycopg2.Binary(image),))
        # commit the changes to the database
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def read_blob(species_id, path_to_dir):
    """ read BLOB data from a table """
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        # execute the SELECT statement
        # cur.execute(""" SELECT species_1_id, species_1_name, image
        #                 FROM species_1
        #                 WHERE species_1.species_1_id = %s """,
        #             (species_id,))
        cur.execute("SELECT species_1_id, species_1_name, image from species_1")
        for row in cur:

            mypic = cur.fetchone()
            open(path_to_dir, 'wb').write(str(mypic[0]))
 
        # blob = cur.fetchone()
        # open(path_to_dir , 'wb').write(blob[0])
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect()

    read_blob(1, 'images/retreived')

