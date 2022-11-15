================
**Travel Agency**
================

@author: *Nicusor-Lucian Barbu*
=======

| Create an application for the management of the travel packages
| offered by the travel agency.
| The application stores the travel packages offered
| to the clients like the following:
| the start and end date of the travel, the destination & the price.

The application should allow to:
-----------

1. F1: Add a new travel package
2. F2: Modify a travel package
3. F3: Delete travel packages for a given destination
4. F4: Delete travel packages that have a shorter duration than given number of days
5. F5: Delete travel packages that have the price bigger than a given price
6. F6: Print all packages
7. F7: Print travel packages that include a stay in a given interval of time (e.g. 10/08/2018 - 24/08/2018). Valid packages:
    start date is equal or greater than the input date and less or equal than the end date
    end date is equal or less that the input date and equal or greater than the start date of the interval
8. F8: Print travel packages that have specific destination and a price less than a given price
9. F9: Print travel packages with a specific end date
10. F10: Print number of offers for a specific destination
11. F11: Print available travel packages in a certain period sorted by price
12. F12: Print medium price for a specific destination
13. F13: Remove offers that have a higher price than the input price and a different destination than the input destination
14. F14: Remove offers where the stay requires rent days in a specific month (input by the user in console between 1 and 12)
15. F15: Undo the last operation (Package list rewinds to the previous state)
* do not use deepCopy

----

1. I1: F1, F2
2. I2: F3, F4, F5
3. I3: F7, F8, F9
4. I4: F10, F11, F12
5. I5: F13, F14
6. I6: F15.
