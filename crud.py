import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password ='',
        database = 'indigo'
    )
    mycursor = conn.cursor()
    print("Connected to MySQL")
except:
    print("connection error")
# creating data base on the db server
# mycursor.execute("CREATE DATABASE IF NOT EXISTS indigo")
# conn.commit()

# create a table
# mycursor.execute("""
# CREATE TABLE airport(
#    airport_id integer primary key,
#    code varchar(10) not null,
#    city varchar(10) not null,
#    name varchar(100) not null
# )
# """)
# conn.commit()

# insert data to the table
# mycursor.execute("""
# INSERT into airport values
# (1,'del','New Delhi','IGIA'),
# (2,'CCU','Kolkata','NSCA'),
# (3,'BOM','Mumbai','CSMA')
# """)
# conn.commit()

# searach / retrieve operation

mycursor.execute("SELECT * FROM airport where airport_id >1")
data = mycursor.fetchall()
print(data)

# update




