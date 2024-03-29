import Domain.entities as domain
from datetime import datetime
time_format = "%d/%m/%Y"


def create_package(package_id, start_date, end_date, destination, price):
    """
    create a new package
    input: start_date - string
           end_date - string
           destination - string
           price - float
    return: package - dictionary
    """
    return{
        "id": package_id,
        "start_date": start_date,
        "end_date": end_date,
        "destination": destination,
        "price": price
        }


def add_package(all_packages, package_id, start_date, end_date, destination, price):
    """
    add a new package to the list of packages
    input: all_packages - list of packages
           start_date - string
           end_date - string
           destination - string
           price - float
    """
    package = create_package(package_id, start_date, end_date, destination, price)
    all_packages.append(package)
    return all_packages


def modify_package(all_packages, new_package_id, new_start_date, new_end_date, new_destination, new_price):
    """
    modify a package
    input: all_packages - list of packages
           new_package_id - integer
           new_start_date - string
           new_end_date - string
           new_destination - string
           new_price - float
    """
    for package in all_packages:
        if domain.get_id(package) == new_package_id:
            domain.set_start_date(package, new_start_date)
            domain.set_end_date(package, new_end_date)
            domain.set_destination(package, new_destination)
            domain.set_price(package, new_price)
    return all_packages


def delete_packages_for_destination(all_packages, destination):
    """
    delete packages for a given destination
    input: all_packages - list of packages
           destination - string
    """
    for i in range(len(all_packages)-1, -1, -1):
        if domain.get_destination(all_packages[i]) == destination:
            del all_packages[i]


def delete_packages_for_shorter_duration(all_packages, days):
    """
    delete packages that have a shorter duration than a given number of days
    input: all_packages - list of packages
           days - integer
    """
    #TODO check if the input time format is right:
    # for example: 0 < days < 31
    #              0 < months < 12
    #              0 < years
    # also check if the input date is greater than today's date
    # valid for every function that requires start_date, end_date

    for i in range(len(all_packages)-1, -1, -1):
        
        start = datetime.strptime(domain.get_start_date(all_packages[i]), time_format)
        end = datetime.strptime(domain.get_end_date(all_packages[i]), time_format)

        date = end - start
        if date.days < days:
            del all_packages[i]
    return all_packages


def delete_packages_for_price(all_packages, price):
    """
    delete packages that have the price bigger than a given price
    input: all_packages - list of packages
           price - float
    """
    for i in range(len(all_packages)-1, -1, -1):
        if domain.get_price(all_packages[i]) > price:
            del all_packages[i]
    return all_packages


def print_packages_for_interval(all_packages, start_date, end_date):
    """
    print packages that include a stay in a given interval of time
    input: all_packages - list of packages
           start_date - string
           end_date - string
    """
    for i in range(len(all_packages)):
        start = datetime.strptime(domain.get_start_date(all_packages[i]), time_format)
        end = datetime.strptime(domain.get_end_date(all_packages[i]), time_format)
        
        if start_date <= start < end <= end_date:
            return all_packages[i]


def print_packages_for_destination_and_price(all_packages, destination, price):
    """
    print packages that have a given destination
    input: all_packages - list of packages
           destination - string
           price - float
    """
    for i in range(len(all_packages)):
        if domain.get_destination(all_packages[i]) == destination and domain.get_price(all_packages[i]) <= float(price):
            return all_packages[i]


def print_packages_for_end_date(all_packages, end_date):
    """
    print packages that have a given end date
    input: all_packages - list of packages
           end_date - string
    """
    for i in range(len(all_packages)):
        if domain.get_end_date(all_packages[i]) == end_date:
            return all_packages[i]


def print_number_of_packages_for_destination(all_packages, destination):
    """
    print the number of packages that have a given destination
    input: all_packages - list of packages
           destination - string
    """
    count = 0
    for i in range(len(all_packages)):
        if domain.get_destination(all_packages[i]) == destination:
            count += 1
    return count


def print_packages_for_duration_and_price(all_packages, days, price):
    """
    print packages that have a given duration and price
    input: all_packages - list of packages
           days - integer
           price - float
    """
    all_packages_copy = []
    for i in range(len(all_packages)):
        if (datetime.strptime(domain.get_end_date(all_packages[i]), time_format) -
            datetime.strptime(domain.get_start_date(all_packages[i]), time_format)).days == days\
                and domain.get_price(all_packages[i]) <= price:
            all_packages_copy.append(all_packages[i])
    return all_packages_copy


def print_medium_price_for_destination(all_packages, destination):
    """
    print the medium price for packages that have a given destination
    input: all_packages - list of packages
           destination - string
    """
    count = 0
    sum = 0
    for i in range(len(all_packages)):
        if domain.get_destination(all_packages[i]) == destination:
            count += 1
            sum += domain.get_price(all_packages[i])
    return sum/count


def remove_package_for_destination_higher_price(all_packages, destination, price):
    """
    remove offers that have a higher price that have a different location
    than the input price and a higher price than the input price
    input: all_packages - list of packages
           destination - string
           price - float
    """
    for i in range(len(all_packages)-1, -1, -1):
        if domain.get_destination(all_packages[i]) != destination or domain.get_price(all_packages[i]) > price:
            del all_packages[i]


def remove_package_for_other_month(all_packages, month):
    """
    remove packages that have a different month than the input month
    input: all_packages - list of packages
           month - integer
    """
    for i in range(len(all_packages)-1, -1, -1):
        if datetime.strptime(domain.get_start_date(all_packages[i]), time_format).month != month:
        # if domain.get_start_date(all_packages[i]).month:
            del all_packages[i]
            

# def undo(all_packages, all_packages_copy):
#     """
#     undo the last operation
#     input: all_packages - list of packages
#            all_packages_copy - list of packages
#     """
#     all_packages = all_packages_copy
#     return all_packages


def undo_last_operation(all_packages, all_packages_copy):
    """
    undo the last operation
    input: all_packages - list of packages
           all_packages_copy - list of packages
    """
    all_packages.clear()
    for i in range(len(all_packages_copy)):
        all_packages.append(all_packages_copy[i])



# def copy_deepCopy(all_packages):
#     """
#     undo the last operation
#     input: all_packages - list of packages
#     """
#     all_packages_copy = []
#     for i in all_packages:
#         ni = i[:]
#         all_packages_copy.append(ni)
#     return all_packages_copy


# def bootleg_deepcopy(main_list):
#     """
#     undo the last operation
#     input: all_packages - list of packages
#     """
#     new_list = []
#     for x in main_list:
#         nx = x[:]
#         new_list.append(nx)
#     return new_list


# def delete_elements(main_list, user_input, undolist):
#     # function that deletes elements from the list if a condition isn't met
#     undolist.append(bootleg_deepcopy(main_list))
#     main_list[:] = [element for element in main_list if not function_that_checks_something(whatever,something)]
#     return main_list


# def undo(main_list, undolist):
#     try:
#         main_list[:] = undolist.pop()
#     except Exception as ex:
#         print(ex)
#     return main_list

#TODO work on undo function
# can help: https://stackoverflow.com/questions/69800164/undo-function-using-self-made-deepcopy