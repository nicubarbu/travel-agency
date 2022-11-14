def get_start_date(all_packages):
    """
    get the start date of a package
    input: all_packages - dictionary
    return: start_date - string
    """
    return all_packages["start_date"]


def get_end_date(all_packages):
    """
    get the end date of a package
    input: all_packages - dictionary
    return: end_date - string
    """
    return all_packages["end_date"]


def get_destination(all_packages):
    """
    get the destination of a package
    input: all_packages - dictionary
    return: destination - string
    """
    return all_packages["destination"]


def get_price(all_packages):
    """
    get the price of a package
    input: all_packages - dictionary
    return: price - float
    """
    return int(all_packages["price"])


def get_id(all_packages):
    '''
    get the id of a package
    input: all_packages - dictionary
    return: id - integer
    '''
    return all_packages["id"]


def set_start_date(all_packages, start_date):
    """
    set the start date of a package
    input: all_packages - dictionary
           start_date - string
    """
    all_packages["start_date"] = start_date
    
    
def set_end_date(all_packages, end_date):
    """
    set the end date of a package
    input: all_packages - dictionary
           end_date - string
    """
    all_packages["end_date"] = end_date


def set_destination(all_packages, destination):
    """
    set the destination of a package
    input: all_packages - dictionary
           destination - string
    """
    all_packages["destination"] = destination


def set_price(all_packages, price):
    """
    set the price of a package
    input: all_packages - dictionary
           price - float
    """
    all_packages["price"] = price
    
    
def set_id(all_packages, id):
    '''
    set the id of a package
    input: all_packages - dictionary
           id - integer
    '''
    all_packages["id"] = id


def set_month(month):
    '''
    set the month of travel
    input: month - integer
    '''
    if month < 1 or month > 12:
        raise ValueError("Invalid month!")
    return month
