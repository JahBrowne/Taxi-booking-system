import sqlite3
from sqlite3 import Error

# functions to manage our database:

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

def create_customer(conn, customer):
    sql = ''' INSERT INTO customer(title, firstname, lastname, email, telno, password, address1, town, county, postcode, paymentmethod)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, customer)
    conn.commit()
    return cur.lastrowid

def create_driver(conn, taxidriver):
    sql = ''' INSERT INTO taxidriver(title, firstname, lastname, email, password, regno)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, taxidriver)
    conn.commit()
    return cur.lastrowid

def create_company(conn, company):
    sql = ''' INSERT INTO companies(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, company)
    conn.commit()
    return cur.lastrowid

def create_trip(conn, booking):
    sql = ''' INSERT INTO booking(customerid, driverid, startaddress, destinationaddress, date, time)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, booking)
    conn.commit()
    return cur.lastrowid
      
def login_customer(conn, user):
    sql = ''' SELECT * FROM customer WHERE email=? AND password=?'''
    cur = conn.cursor()
    cur.execute(sql, user)
    first = cur.fetchall()[0] 
    return first

def get_drivers(conn):
    sql = ''' SELECT * FROM taxidriver'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def get_trips(conn):
    sql = ''' SELECT * FROM booking'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def delete_trip(conn, bookingid):
    sql = 'DELETE FROM booking WHERE bookingid=?'
    cur = conn.cursor()
    cur.execute(sql, bookingid)
    conn.commit()


