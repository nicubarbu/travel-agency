TRAVEL AGENCY

Create an application for the management of the travel packages offered by the travel agency.
The application stores the travel packages offered to the clients like the following:
the start and end date of the travel, the destination & the price.


The application should allow to:

F1: Add a new travel package
F2: Modify a travel package
F3: Delete travel packages for a given destination
F4: Delete travel packages that have a shorter duration than a given number of days
F5: Delete travel packages that have the price bigger than a given price
F6: Print travel packages that include a stay in a given interval of time (e.g. 10/08/2018 - 24/08/2018)
        valid packages:
        - start date is equal or greater than the input date and less or equal than the end date
        - end date is equal or less that the input date and equal or greater than the start date of the interval
F7: Print travel packages that have specific destination and a price  less than a given price
F8: Print travel packages with a specific end date
F9: Print number of offers for a specific destination
F10: Print available travel packages in a certain period sorted by price
F11: Print medium price for a specific destination
F12: Remove offers that have a higher price than the input price and a different destination than the input destination
F13: Remove offers where the stay requires rent days in a specific month (input by the user in console between 1 and 12)
F14: Undo the last operation (Package list rewinds to the previous state) - do not use deepCopy
-----------------------------------------------------------------------

I1: F1, F2
I2: F3, F4, F5
I3: F6, F7, F8
I4: F9, F10, F11
I5: F12, F13
I6: F14
