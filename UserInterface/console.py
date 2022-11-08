import Domain.operations as op


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
          6. Print all packages for a specific interval of dates
          7. Print all packages for a specific destination
          8. Print all packages for a specific end date
          9. Print the number of packages for a specific destination
          10. Print all packages for a specific duration and price
          11. Print the medium price for a specific destination
          
                        REMOVAL
          12. Remove the packages that have a specific destination, but a bigger price
          13. Remove the packages that are available in a different month
          
                        UNDO
          14. Undo the last operation
          x. Exit
          """)


def add_package(all_packages):
    destination = input("Destination: ")
    start_date = input("Start date {dd-mm-yyyy}: ")
    end_date = input("End date {dd-mm-yyyy}: ")
    price = input("Price: ")
    op.add_package(all_packages, destination, start_date, end_date, price)


def modify_package(all_packages):
    destination = input("Destination: ")
    start_date = input("Start date {dd-mm-yyyy}: ")
    end_date = input("End date {dd-mm-yyyy}: ")
    price = input("Price: ")
    op.modify_package(all_packages, start_date, end_date, destination, price)


def delete_packages_for_destination(all_packages):
    destination = input("Destination: ")
    print(op.delete_packages_for_destination(all_packages, destination))


def delete_packages_for_shorter_duration(all_packages):
    days = int(input("Days: "))
    op.delete_packages_for_shorter_duration(all_packages, days)


def delete_packages_for_price(all_packages):
    price = float(input("Price: "))
    op.delete_packages_for_price(all_packages, price)


def print_packages_for_interval(all_packages):
    start_date = input("Start date {dd-mm-yyyy}: ")
    end_date = input("End date {dd-mm-yyyy}: ")
    print(op.print_packages_for_interval(all_packages, start_date, end_date))


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
    options = {1: add_package,
               2: modify_package,
               3: delete_packages_for_destination,
               4: delete_packages_for_shorter_duration,
               5: delete_packages_for_price,
               6: print_packages_for_interval,
               7: print_packages_for_destination_and_price,
               8: print_packages_for_end_date,
               9: print_number_of_packages_for_destination,
               10: print_packages_for_duration_and_price,
               11: print_medium_price_for_destination,
               12: remove_package_for_destination_higher_price,
               13: remove_package_for_other_month,
               14: undo_last_operation,
               15: exit
               }
    all_packages = []
    while True:
        print_options()
        opt = input("Option: ")
        if opt == "x":
            break
        opt = int(opt)
        options[opt](all_packages)
