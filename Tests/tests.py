import Domain.entities as domain
import Domain.operations as op
"""
--- tests ---
assert len(all_packages) == 
assert (domain.get_destination(all_packages[0]) == "")
assert (domain.get_start_date(all_packages[0]) == "")
assert (domain.get_end_date(all_packages[0]) == "")
assert (domain.get_price(all_packages[0]) == )
"""


def create_package():
    assert op.create_package(1, "01-05-2022", "10-05-2022", "Paris", 1000) == [1, "01-05-2022", "10-05-2022", "Paris", 1000]


def add_package():
    all_packages = []
    op.add_package(all_packages, 1, "01-05-2022", "10-05-2022", "Paris", 1000)
    assert len(all_packages) == 1
    assert (domain.get_id(all_packages[0]) == 1)
    assert (domain.get_destination(all_packages[0]) == "Paris")
    assert (domain.get_start_date(all_packages[0]) == "01-05-2022")
    assert (domain.get_end_date(all_packages[0]) == "10-05-2022")
    assert (domain.get_price(all_packages[0]) == 1000)
    

def modify_package():
    all_packages = []
    op.add_package(all_packages, 1, "01-07-2022", "06-07-2022", "Tokyo", 1000)
    op.add_package(all_packages, 2, "01-05-2022", "10-05-2022", "Paris", 800)
    op.modify_package(all_packages, 1, "02-07-2022", "06-07-2022", "Tokyo", 2500)
    assert len(all_packages) == 2
    assert (domain.get_id(all_packages[0]) == 1)
    assert (domain.get_destination(all_packages[0]) == "Tokyo")
    assert (domain.get_start_date(all_packages[0]) == "02-07-2022")
    assert (domain.get_end_date(all_packages[0]) == "06-07-2022")
    assert (domain.get_price(all_packages[0]) == 2500)
    assert (domain.get_id(all_packages[1]) == 2)
    assert (domain.get_destination(all_packages[1]) == "Paris")
    assert (domain.get_start_date(all_packages[1]) == "01-05-2022")
    assert (domain.get_end_date(all_packages[1]) == "10-05-2022")
    assert (domain.get_price(all_packages[1]) == 800)
    
    
def delete_packages_for_destination():
    all_packages = []
    op.add_package(all_packages, 1, "01-07-2022", "06-07-2022", "Paris", 1000)
    op.add_package(all_packages, 2, "01-07-2022", "06-07-2022", "Paris", 1000)
    op.add_package(all_packages, 3, "01-07-2022", "06-07-2022", "Tokyo", 1000)
    op.delete_packages_for_destination(all_packages, "Paris")
    assert len(all_packages) == 1
    
    
def delete_packages_for_short_duration():
    all_packages = []
    op.add_package(all_packages, 1, "01-05-2022", "10-05-2022", "Paris", 800)
    op.add_package(all_packages, 2, "02-07-2022", "06-07-2022", "Costinesti", 100)
    op.add_package(all_packages, 3, "01-08-2022", "02-08-2022", "Tokyo", 1500)
    op.delete_packages_for_shorter_duration(all_packages, 2)
    assert len(all_packages) == 2
    
    
def delete_packages_for_price():
    all_packages = []
    op.add_package(all_packages, 1, "01-05-2022", "10-05-2022", "Paris", 800)
    op.add_package(all_packages, 2, "02-07-2022", "06-07-2022", "Costinesti", 100)
    op.add_package(all_packages, 3, "01-08-2022", "02-08-2022", "Tokyo", 1500)
    op.delete_packages_for_price(all_packages, 350)
    assert len(all_packages) == 1
    
    
def print_packages_for_interval():
    all_packages = []
    op.add_package(all_packages, 1, "01-05-2022", "10-05-2022", "Paris", 800)
    op.add_package(all_packages, 2, "02-07-2022", "06-07-2022", "Costinesti", 100)
    op.add_package(all_packages, 3, "01-08-2022", "02-08-2022", "Tokyo", 1500)
    assert op.print_packages_for_interval(all_packages, "01-05-2022", "10-05-2022")
    assert (domain.get_id(all_packages[0]) == 1)
    assert (domain.get_destination(all_packages[0]) == "Paris")
    assert (domain.get_start_date(all_packages[0]) == "01-05-2022")
    assert (domain.get_end_date(all_packages[0]) == "10-05-2022")
    assert (domain.get_price(all_packages[0]) == 800)
    
    
def print_packages_for_destination_and_price():
    all_packages = []
    op.add_package(all_packages, 1, "01-01-2022", "01-01-2022", "Paris", 500)
    op.add_package(all_packages, 2, "01-01-2022", "01-01-2022", "Paris", 700)
    op.add_package(all_packages, 3, "01-01-2022", "01-01-2022", "Bucharest", 200)
    assert op.print_packages_for_destination_and_price(all_packages, "Paris", 600)
    
    
# def print_packages_for_end_date():
#     all_packages = []
#     op.add_package(all_packages, "10-02-2022", "14-02-2022", "Bucharest", 500)
#     op.add_package(all_packages, "07-01-2022", "10-01-2022", "Bologna", 250)
#     op.add_package(all_packages, "01-01-2022", "03-01-2022", "Paris", 1500)
#     result = op.print_packages_for_end_date(all_packages, "15-01-2022") == ["Paris\n", "Bologna\n"]
    
    
# def print_number_of_packages_for_destination():
#     all_packages = []
#     op.add_package(all_packages, "10-02-2022", "14-02-2022", "Bucharest",  500)
#     op.add_package(all_packages, "07-01-2022", "10-01-2022", "Bologna",  250)
#     op.add_package(all_packages, "01-01-2022", "02-01-2022", "Paris",  1500)
#     assert op.print_number_of_packages_for_destination(all_packages, "Paris") == 1
    
    
# def print_packages_for_duration_and_price():
#     all_packages = []
#     op.add_package(all_packages, "10-02-2022", "14-02-2022", "Bucharest", 500)
#     op.add_package(all_packages, "07-01-2022", "10-01-2022", "Bologna", 250)
#     op.add_package(all_packages, "01-01-2022", "02-01-2022", "Paris", 1500)
#     # assert op.print_packages_for_duration_and_price(all_packages, 4, 600) == ["Bucharest\n"]
#     assert (domain.get_destination(all_packages[0]) == "Bucharest")
#     assert (domain.get_start_date(all_packages[0]) == "10-02-2022")
#     assert (domain.get_end_date(all_packages[0]) == "14-02-2022")
#     assert (domain.get_price(all_packages[0]) == 500)
    
    
# def print_medium_price_for_destination():
#     all_packages = []
#     op.add_package(all_packages, "10-02-2022", "14-02-2022", "Bucharest", 500)
#     op.add_package(all_packages, "07-01-2022", "10-01-2022", "Bucharest", 700)
#     op.add_package(all_packages,  "01-01-2022", "02-01-2022", "Paris", 1500)
#     assert op.print_medium_price_for_destination(all_packages, "Bucharest") == 600
    

# def remove_package_for_destination_higher_price():
#     all_packages = []
#     op.add_package(all_packages, "10-02-2022", "14-02-2022", "Bucharest", 500)
#     op.add_package(all_packages, "07-01-2022", "10-01-2022", "Bucharest", 700)
#     op.add_package(all_packages, "01-01-2022", "02-01-2022", "Paris", 1500)
#     op.remove_package_for_destination_higher_price(all_packages, "Bucharest", 600)
#     assert len(all_packages) == 1
    
    
# def remove_package_for_other_month():
#     all_packages = []
#     op.add_package(all_packages, "10-10-2022", "14-10-2022", "Bucharest", 500)
#     op.add_package(all_packages, "01-01-2022", "02-01-2022", "Paris", 1500)
#     op.remove_package_for_other_month(all_packages, "10")
#     # assert (domain.get_destination(all_packages[0]) == "Paris")
#     # assert (domain.get_start_date(all_packages[0]) == "01-01-2022")
#     # assert (domain.get_end_date(all_packages[0]) == "02-01-2022")
#     # assert (domain.get_price(all_packages[0]) == 1500)
    
    
# def undo_last_operation():
#     all_packages = []
#     op.add_package(all_packages, "Bucharest", "10-02-2022", "14-02-2022", 500)
#     op.add_package(all_packages, "Bucharest", "07-01-2022", "10-01-2022", 700)
#     op.add_package(all_packages, "Paris", "01-01-2022", "02-01-2022", 1500)
#     op.remove_package_for_other_month(all_packages, "02")
#     op.undo_last_operation(all_packages, all_packages_copy)
#     assert len(all_packages) == 2


def all():
    add_package()
    modify_package()
    delete_packages_for_destination()
    delete_packages_for_short_duration()
    delete_packages_for_price()
    print_packages_for_interval()
    print_packages_for_destination_and_price()
    # print_packages_for_end_date()
    # print_number_of_packages_for_destination()
    # print_packages_for_duration_and_price()
    # print_medium_price_for_destination()
    # remove_package_for_destination_higher_price()
    # remove_package_for_other_month()
    # undo_last_operation()

#TODO: resolve bugs for: 
# print_packages_for_end_date, 
# remove_package_for_other_month,
# undo_last_operation
