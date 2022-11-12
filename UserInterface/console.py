from datetime import datetime
import Domain.operations as op
import Domain.entities as domain
time_format = "%d-%m-%Y"


def print_options():
    print("""
                ADDITION & MODIFICATION
          1. Add package
          2. Modify package
          
                        DELETION
          3. Delete all packages for a specific destination
          4. Delete all packages for a shorter duration
          5. Delete all packages for a bigger price
          
                        PRINTING
          6. Print all packages
          7. Print all packages for a specific interval of dates
          8. Print all packages for a specific destination and price
          9. Print all packages for a specific end date
          10. Print the number of packages for a specific destination
          11. Print all packages for a specific duration and price
          12. Print the medium price for a specific destination
          
                        REMOVAL
          13. Remove the packages that have different destination or bigger price than input
          14. Remove the packages that are available in a different month
          
                        UNDO
          15. Undo the last operation
          
          x. Exit
          """)


def add_package(all_packages):
    package_id = -1
    for i in range(0, len(all_packages)):
        # if i in all_packages[i].values():
        if i+1 == domain.get_id(all_packages[i]):
            continue
        else:
            package_id = i+1
            
    if package_id == -1:
        package_id = len(all_packages) + 1
    
    start_date = input("Start date {dd-mm-yyyy}: ")
    while (type(start_date) is not str) or (len(start_date) != 10):
        print("Invalid start date!")
        while type(datetime.strptime(start_date, time_format)) is not datetime:
            print("Invalid start date!")
            start_date = input("Start date {dd-mm-yyyy}: ")
            
    end_date = input("End date {dd-mm-yyyy}: ")
    while (type(end_date) is not str) or (len(end_date) != 10):
        print("Invalid end date!")
        while type(datetime.strptime(end_date, time_format)) is not datetime:
            print("Invalid end date!")
            start_date = input("End date {dd-mm-yyyy}: ")
            
    destination = input("Destination: ")
    while type(destination) is not str:
        print("Invalid destination!")
        destination = input("Destination: ")
            
    try:
        price = float(input("Price: "))
    except TypeError as te:
        print("You entered an invalid value. You should enter a floating number. ", te)
        price = float(input("Price: "))
    
    op.add_package(all_packages, package_id, start_date, end_date, destination, price)


def modify_package(all_packages):
    if len(all_packages) == 0:
        print("There are no packages to modify.")
        return run_menu()
    
    print("These are the available packages:\n")
    print_all_packages(all_packages)
    print("Enter the ID of the package you want to modify.")
    user_id = int(input("ID: "))
    while user_id > len(all_packages) or user_id < 1:
        print("Invalid ID!")
        user_id = int(input("ID: "))
    
    if len(all_packages) >= user_id > 0:
        print("Enter the new information for the package.")
        start_date = input("Start date {dd-mm-yyyy}: ")
        end_date = input("End date {dd-mm-yyyy}: ")
        destination = input("Destination: ")
        price = float(input("Price: "))
        op.modify_package(all_packages, user_id, start_date, end_date, destination, price)


def delete_packages_for_destination(all_packages):
    if len(all_packages) == 0:
        print("There are no packages to modify.")
        return run_menu()
    
    print("These are the available packages:\n")
    print_all_packages(all_packages)
    
    destination = input("Destination: ")
    print(op.delete_packages_for_destination(all_packages, destination))


def delete_packages_for_shorter_duration(all_packages):
    if len(all_packages) == 0:
        print("There are no packages to modify.")
        return run_menu()
    
    print("These are the available packages:\n")
    print_all_packages(all_packages)
    
    days = int(input("Days: "))
    op.delete_packages_for_shorter_duration(all_packages, days)


def delete_packages_for_price(all_packages):
    if len(all_packages) == 0:
        print("There are no packages to modify.")
        return run_menu()
    
    print("These are the available packages:\n")
    print_all_packages(all_packages)
    
    price = float(input("Price: "))
    op.delete_packages_for_price(all_packages, price)


def print_all_packages(all_packages):
    for i in range(len(all_packages)):
        print(all_packages[i])

def print_packages_for_interval(all_packages):
    start_date = input("Start date {dd-mm-yyyy}: ")
    end_date = input("End date {dd-mm-yyyy}: ")
    for i in range(len(all_packages)):
        print(op.print_packages_for_interval(all_packages[i], start_date, end_date))


def print_packages_for_destination_and_price(all_packages):
    destination = input("Destination: ")
    price = input("Price: ")
    print(op.print_packages_for_destination_and_price(all_packages, destination, price))


def print_packages_for_end_date(all_packages):
    end_date = input("End date {dd-mm-yyyy}: ")
    print(op.print_packages_for_end_date(all_packages, end_date))


def print_number_of_packages_for_destination(all_packages):
    destination = input("Destination: ")
    print(op.print_number_of_packages_for_destination(all_packages, destination))


def print_packages_for_duration_and_price(all_packages):
    days = int(input("Days: "))
    price = float(input("Price: "))
    print(op.print_packages_for_duration_and_price(all_packages, days, price))


def print_medium_price_for_destination(all_packages):
    destination = input("Destination: ")
    print(op.print_medium_price_for_destination(all_packages, destination))


def remove_package_for_destination_higher_price(all_packages):
    destination = input("Destination: ")
    price = float(input("Price: "))
    op.remove_package_for_destination_higher_price(all_packages, destination, price)


def remove_package_for_other_month(all_packages):
    month = int(input("Month: "))
    op.remove_package_for_other_month(all_packages, month)


def undo_last_operation(all_packages, all_packages_copy):
    op.undo_last_operation(all_packages, all_packages_copy)


def run_menu():
    options = {
               1: add_package,
               2: modify_package,
               3: delete_packages_for_destination,
               4: delete_packages_for_shorter_duration,
               5: delete_packages_for_price,
               6: print_all_packages,
               7: print_packages_for_interval,
               8: print_packages_for_destination_and_price,
               9: print_packages_for_end_date,
               10: print_number_of_packages_for_destination,
               11: print_packages_for_duration_and_price,
               12: print_medium_price_for_destination,
               13: remove_package_for_destination_higher_price,
               14: remove_package_for_other_month,
               15: undo_last_operation,
               16: exit
    }
    all_packages = []
    while True:
        print_options()
        opt = input("Option: ")
        if opt == "x":
            break
        opt = int(opt)
        options[opt](all_packages)
