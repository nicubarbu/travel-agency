def get_start_date(package):
    """
    get the start date of a package
    input: package - dictionary
    return: start_date - string
    """
    return package["start_date"]


def get_end_date(package):
    """
    get the end date of a package
    input: package - dictionary
    return: end_date - string
    """
    return package["end_date"]


def get_destination(package):
    """
    get the destination of a package
    input: package - dictionary
    return: destination - string
    """
    return package["destination"]


def get_price(package):
    """
    get the price of a package
    input: package - dictionary
    return: price - float
    """
    return package["price"]

def set_start_date(package, start_date):
    """
    set the start date of a package
    input: package - dictionary
           start_date - string
    """
    package["start_date"] = start_date
    
    
def set_end_date(package, end_date):
    """
    set the end date of a package
    input: package - dictionary
           end_date - string
    """
    package["end_date"] = end_date


def set_destination(package, destination):
    """
    set the destination of a package
    input: package - dictionary
           destination - string
    """
    package["destination"] = destination


def set_price(package, price):
    """
    set the price of a package
    input: package - dictionary
           price - float
    """
    package["price"] = price


def set_month(month):
    '''
    set the month of travel
    input: month - integer
    '''
    if month < 1 or month > 12:
        raise ValueError("Invalid month!")
    return month
