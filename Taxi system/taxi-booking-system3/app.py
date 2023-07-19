from database import *

# creating database name variable to use it later
database = "tbs.db"

# create a database connection
conn = create_connection(database)

if not conn:
    print("Error! Cannot create the database connection.")
    exit()

current_user = None

def register():
    global current_user

    title = input("Enter your title:\n")
    firstname = input("Enter your first name:\n")
    lastname = input("Enter your last name:\n")
    email = input("Enter your email:\n")
    telno = input("Enter your telephone number:\n")
    password = input("Enter your password:\n")
    address1 = input("Enter the first line of your address:\n")
    town = input("Enter your town:\n")
    county = input("Enter your county:\n")
    postcode = input("Enter your postcode:\n")
    paymentmethod = input("Enter your paymentmethod:\n")
    

    data = (title, firstname, lastname, email, telno, password, address1, town, county, postcode, paymentmethod)
    current_user = create_customer(conn,data)
    
    print(f"Hello {firstname}, Your account has been created.")
    input("Press any key to continue...")
    show_menu()

def login():
    global current_user

    email = input("Enter your email:\n ")
    password = input("Enter your password:\n ")

    data = (email, password)
    try: 
        user = login_customer(conn, data)
        customerid = user[0]
        firstname = user[2]
        current_user = customerid
    except:
        print("Bad email or password.")
        show_menu()

    print(f"Hello {firstname}, You are logged in.")    
    input("Press any key to continue...")
    show_menu()

def create_booking():
    drivers = get_drivers(conn)
    print("Available drivers:")
    for i, driver in enumerate(drivers):
        print(str(i)+"."+str(driver[1])+" "+str(driver[2]))
    
    _input = input("Select option: ")
    index = int(_input)
    driver = drivers[index]
    driverid = driver[0]
    customerid = current_user
    startaddress = input("Enter your pickup address:\n ")
    destinationaddress = input("Enter your destination:\n ")
    date = input("Enter your booking date:\n")
    time = input("End the pickup time:\n ")
    
    data = (customerid, driverid, startaddress, destinationaddress, date, time)
    trip = create_trip(conn, data)
    print("Booking created!")
    input("Press any key to continue...")
    show_menu()

def show_bookings():
    bookings = get_trips(conn)
    if not bookings:
        print("No bookings.")
    else:
        print("Available bookings:")
        for i, booking in enumerate(bookings):
            print(str(i)+". "+str(booking[5])+" -> "+str(booking[8]))
        
    input("Press any key to continue...")
    show_menu()

def remove_booking():
    bookings = get_trips(conn)

    if not bookings:
        print("No bookings.")
    else:
        print("Select booking to delete:")
        for i, booking in enumerate(bookings):
            print(str(i)+". "+str(booking[5])+" -> "+str(booking[8]))
        
        _input = input("Select option: ")
        index = int(_input)
        booking = bookings[index]
        bookingid = (booking[0],)

        delete_trip(conn, bookingid)
        print("Booking deleted.")
    input("Press any key to continue...")
    show_menu()

def Cancel():
    exit()

def show_menu():
    if(not current_user):
        print("1. Register")
        print("2. Login\n")
        _input = input("Select option:\n ")

        if _input == "1":
            register()
        elif _input == "2":
            login()

    else:
        print("1. Make Booking")
        print("2. View Bookings")
        print("3. Cancel Booking")
        print("4. Exit\n")
        
        _input = input("Select option:\n ")

        if _input == "1":
            create_booking()

        elif _input == "2":
            show_bookings()

        elif _input == "3":
            remove_booking()
        elif _input == "4":
            Cancel()

show_menu()


