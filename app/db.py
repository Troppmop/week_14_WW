import mysql.connector 
import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASS = os.getenv('MYSQL_PASS')
MYSQL_DB = os.getenv('MYSQL_DB')

def connect_db():
    cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASS,
                                host=MYSQL_HOST, database=MYSQL_DB, port='3306'
                                )
    cursor = cnx.cursor()
    return cnx, cursor

def disconnect_db(cnx:mysql.connector.MySQLConnection, cursor):
    cursor.close()
    cnx.close()

def create_table(cnx, cursor):
    cursor.execute("""create table if not exists weapons(
                    id int auto_increment,
                    weapon_id varchar,
                    weapon_name varchar,
                    weapon_type varchar,
                    range_km_ int,
                    weight_kg float,
                    manufacturer varchar,
                    origin_country varchar,
                    storage_location varchar,
                    year_estimated int,
                    risk_level varchar                       
                    primary key (id)
                   )
                   
                   """)
    cnx.commit()



