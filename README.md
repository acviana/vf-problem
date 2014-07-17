This python module provides an interactive parser for the included .csv file. Features:

* List all Managers
* List all Employees reporting to a given Manager
* List all people with the position "Python Developer"
* List everyone who has a phone number
* Permit the user to order results by a specified field
* Object-oriented design
* Test cases
* PEP-8 compliance / other best practices
* Support for compound queries, eg. as "list all employees reporting
to X with job title Y"


This project took about 3 horus to complete.

Example Usage:


	$ python query_employees.py
	Choose a field:
		 ['LastName', 'FirstName', 'Position', 'Manager', 'Email', 'reports_to', 'phone']
	> phone
	Choose a query type:
		 ['is', 'is not']
	> is not
	What value to query for?
	> none
	Choose a field to sort on:
		 ['LastName', 'FirstName', 'Position', 'Manager', 'Email', 'reports_to', 'phone']
	> LastName
	Querying for phone is not none
	|        Austin        |        Steve         |   Python Developer   |       employee       |      sa@vf.com       |    Oscar Goldman     |      3121230810      |
	|       Sommers        |        Jamie         |   Project Manager    |       manager        |      js@vf.com       |    Oliver Spencer    |      7735550818      |
	Would you like to query on these results? (yes/no)
	> yes
	Choose a field:
		 ['LastName', 'FirstName', 'Position', 'Manager', 'Email', 'reports_to', 'phone']
	> LastName
	Choose a query type:
		 ['is', 'is not']
	> is
	What value to query for?
	> Austin
	Choose a field to sort on:
		 ['LastName', 'FirstName', 'Position', 'Manager', 'Email', 'reports_to', 'phone']
	> LastName
	Querying for LastName is Austin
	|        Austin        |        Steve         |   Python Developer   |       employee       |      sa@vf.com       |    Oscar Goldman     |      3121230810      |
	Would you like to query on these results? (yes/no)
	> no
	
Nosetests:

	$ nosetests
	....
	----------------------------------------------------------------------
	Ran 4 tests in 0.009s
	
	OK
