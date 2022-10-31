def start_date(package, start_date):
    """
    set the start date of a package
    input: package - dictionary
           start_date - string
    """
    package["start_date"] = start_date
    
    
def end_date(package, end_date):
    """
    set the end date of a package
    input: package - dictionary
           end_date - string
    """
    package["end_date"] = end_date


def destination(package, destination):
    """
    set the destination of a package
    input: package - dictionary
           destination - string
    """
    package["destination"] = destination


def price(package, price):
    """
    set the price of a package
    input: package - dictionary
           price - float
    """
    package["price"] = price


def month(month):
    '''
    set the month of travel
    input: month - integer
    '''
    if month < 1 or month > 12:
        raise ValueError("Invalid month!")
    return month
