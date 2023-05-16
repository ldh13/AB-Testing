# Connecting to the database in bit.io and retrieving data

# imports
import pandas as pd
import sqlalchemy


# variables
PG_STRING = 'postgresql://nico71995:v2_43CJt_WPpFFvuW3A42GLQxpK5FEAj@db.bit.io:5432/griffinmasterschool/ab_test_project'


# first set up engine
engine = sqlalchemy.create_engine(PG_STRING, pool_pre_ping= True)


# query 1 with the data in the User and Group tables
query1 = sqlalchemy.text('SELECT id, country, gender, g.group, join_dt, g.device as visit_device FROM users AS u JOIN groups AS g ON u.id = g.uid')
query2 = sqlalchemy.text('SELECT * FROM activity')
query3 = sqlalchemy.text('SELECT id, country, gender, g.group, g.device, spent, join_dt, dt FROM users AS u JOIN groups AS g ON g.uid = u.id LEFT JOIN activity AS a ON a.uid = u.id')

# retrieving data to a pandas df
with engine.connect() as conn:
    user_data = pd.read_sql(query1, conn)
    activity_data = pd.read_sql(query2, conn)
    active_user_data = pd.read_sql(query3, conn)





