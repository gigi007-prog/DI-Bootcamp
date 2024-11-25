import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST= os.getenv('HOSTNAME')
DB_NAME=os.getenv('DATABASE')
DB_USER=os.getenv('USER')
DB_PASSWORD=os.getenv('PASSWORD')
DB_PORT=os.getenv('PORT')


connection = psycopg2.connect(database = DB_NAME,
                              user = DB_USER,
                              password = DB_PASSWORD,
                              host=DB_HOST,
                              port=DB_PORT)

cursor = connection.cursor()




class MenuItem:
    def __init__(self, name, price=0):
        self.name=name
        self.price=price
    
    def save(self):
        query = 'INSERT INTO....'

    def delete(self):
        query = 'DELETE FROM....'

    def updated(self):
        query = 'UPDATE '

    