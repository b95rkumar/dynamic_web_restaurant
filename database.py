import sqlalchemy, os, pymysql
from sqlalchemy import create_engine, text
from dataclasses import dataclass
import attr
print (sqlalchemy.__version__)

DB_CONNECTION_STRING=os.environ['DB_CONNECTION_STRING']
# PyMySQL
engine = create_engine(DB_CONNECTION_STRING, 
                       connect_args={
                         "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
                       })


def load_data_from_db (food_type):
  with engine.connect() as conn :
    result = conn.execute (text (f"select * from dishes where food_type=:val"), {"val":food_type})
  #  print ("engine type", type(engine))
  total_foods = []
  for food in result.all():
    total_foods.append(food._mapping)
  return total_foods

def load_data_into_db ():
  with engine.connect() as conn :
    result = conn.execute (text (f"select * from dishes where food_type=:val"), {"val":food_type})
  #  print ("engine type", type(engine))
  total_foods = []
  for food in result.all():
    total_foods.append(food._mapping)
  return total_foods
