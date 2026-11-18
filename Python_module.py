
# FLIGHT RESERVATION SYSTEM

passengers = {}
tickets = {}
ticket_no = 1001

flights = [
    ["AI101", "Chennai", "Delhi", 5000, 10],
    ["AI102", "Chennai", "Mumbai", 4000, 15],
    ["AI103", "Delhi", "Bangalore", 6000, 12],
    ["AI104", "Mumbai", "Delhi", 4500, 8]
]


# PASSENGER SIGN UP

def signup():
    print("\n--- PASSENGER SIGN UP ---")

    username = input("Enter Username: ")

    if username in passengers:
        print("Username Already Exists!")
        return

    password = input("Enter Password: ")
    passengers[username] = password

    print("Signup Successful!")


# PASSENGER SIGN IN

def signin():
    print("\n--- PASSENGER SIGN IN ---")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in passengers and passengers[username] == password:
        print("Login Successful!")
        passenger_menu(username)
    else:
        print("Invalid Username or Password!")


# CHECK AVAILABILITY

def check_availability():
    print("\n--- FLIGHT AVAILABILITY ---")

    source = input("Enter Source: ")
    destination = input("Enter Destination: ")

    found = False

    for flight in flights:
        if flight[1].lower() == source.lower() and flight[2].lower() == destination.lower():
            print("\nFlight ID:", flight[0])
            print("Source:", flight[1])
            print("Destination:", flight[2])
            print("Fare: Rs.", flight[3])
            print("Available Seats:", flight[4])
            found = True

    if not found:
        print("No Flights Available!")


# BOOK TICKET

def book_ticket(username):
    global ticket_no

    print("\n--- BOOK TICKET ---")

    source = input("Enter Source: ")
    destination = input("Enter Destination: ")

    found = False

    for flight in flights:
        if flight[1].lower() == source.lower() and flight[2].lower() == destination.lower():

            if flight[4] > 0:
                print("\nFlight ID:", flight[0])
                print("Fare: Rs.", flight[3])
                print("Seats:", flight[4])

                choice = input("Do you want to book? (yes/no): ")

                if choice.lower() == "yes":
                    ticket_id = ticket_no
                    ticket_no += 1

                    flight[4] -= 1

                    tickets[ticket_id] = [
                        username,
                        flight[0],
                        flight[1],
                        flight[2],
                        flight[3],
                        "Pending"
                    ]

                    print("Ticket Booking Successful!")
                    print("Ticket ID:", ticket_id)
                    print("Status: Pending Approval")

                else:
                    print("Booking Cancelled!")

                found = True
                break

            else:
                print("No Seats Available!")
                found = True
                break

    if not found:
        print("Flight Not Found!")


# CANCEL TICKET

def cancel_ticket(username):
    print("\n--- CANCEL TICKET ---")

    ticket_id = int(input("Enter Ticket ID: "))

    if ticket_id in tickets and tickets[ticket_id][0] == username:

        if tickets[ticket_id][5] == "Cancelled":
            print("Ticket Already Cancelled!")
        else:
            for flight in flights:
                if flight[0] == tickets[ticket_id][1]:
                    flight[4] += 1

            tickets[ticket_id][5] = "Cancellation Requested"
            print("Cancellation Request Sent!")

    else:
        print("Ticket Not Found!")


# STATUS CHECKING

def status_checking(username):
    print("\n--- TICKET STATUS ---")

    found = False

    for ticket_id, details in tickets.items():

        if details[0] == username:
            print("\nTicket ID:", ticket_id)
            print("Flight ID:", details[1])
            print("Source:", details[2])
            print("Destination:", details[3])
            print("Fare: Rs.", details[4])
            print("Status:", details[5])
            found = True

    if not found:
        print("No Tickets Found!")


# PASSENGER MENU

def passenger_menu(username):

    while True:
        print("\n===== PASSENGER MENU =====")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Status Checking")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            check_availability()

        elif choice == "2":
            book_ticket(username)

        elif choice == "3":
            cancel_ticket(username)

        elif choice == "4":
            status_checking(username)

        elif choice == "5":
            print("Passenger Logout!")
            break

        else:
            print("Invalid Choice!")


# CASHIER APPROVE TICKET

def approve_ticket():
    print("\n--- APPROVE TICKET ---")

    for ticket_id, details in tickets.items():
        if details[5] == "Pending":
            print("Ticket ID:", ticket_id)
            print("Passenger:", details[0])
            print("Flight:", details[1])

    ticket_id = int(input("Enter Ticket ID: "))

    if ticket_id in tickets:

        if tickets[ticket_id][5] == "Pending":
            tickets[ticket_id][5] = "Approved"
            print("Ticket Approved Successfully!")

        else:
            print("Ticket Is Not Pending!")

    else:
        print("Ticket Not Found!")


# CASHIER CANCEL TICKET

def cashier_cancel():
    print("\n--- CASHIER CANCEL TICKET ---")

    ticket_id = int(input("Enter Ticket ID: "))

    if ticket_id in tickets:

        if tickets[ticket_id][5] in ["Pending", "Approved", "Cancellation Requested"]:
            for flight in flights:
                if flight[0] == tickets[ticket_id][1]:
                    flight[4] += 1

            tickets[ticket_id][5] = "Cancelled"
            print("Ticket Cancelled Successfully!")

        else:
            print("Ticket Already Cancelled!")

    else:
        print("Ticket Not Found!")


# CASHIER MENU

def cashier_menu():

    while True:
        print("\n===== CASHIER MENU =====")
        print("1. Approve Ticket")
        print("2. Cancel Ticket")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            approve_ticket()

        elif choice == "2":
            cashier_cancel()

        elif choice == "3":
            break

        else:
            print("Invalid Choice!")


# MAIN MENU

while True:

    print("\n===== FLIGHT RESERVATION SYSTEM =====")
    print("1. Passenger")
    print("2. Cashier")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        while True:
            print("\n1. Sign Up")
            print("2. Sign In")
            print("3. Back")

            option = input("Enter Choice: ")

            if option == "1":
                signup()

            elif option == "2":
                signin()

            elif option == "3":
                break

            else:
                print("Invalid Choice!")

    elif choice == "2":

        username = input("Cashier Username: ")
        password = input("Cashier Password: ")

        if username == "admin" and password == "1234":
            cashier_menu()
        else:
            print("Invalid Cashier Login!")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
