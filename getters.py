def start_date(package):
    """
    get the start date of a package
    input: package - dictionary
    return: start_date - string
    """
    return package["start_date"]


def end_date(package):
    """
    get the end date of a package
    input: package - dictionary
    return: end_date - string
    """
    return package["end_date"]


def destination(package):
    """
    get the destination of a package
    input: package - dictionary
    return: destination - string
    """
    return package["destination"]


def price(package):
    """
    get the price of a package
    input: package - dictionary
    return: price - float
    """
    return package["price"]