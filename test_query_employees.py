from query_employees import EmployeeQuery

def test_managers_query():
    """The query for all the managers."""
    eq = EmployeeQuery()
    eq.select('Manager', 'is', 'manager')
    result = [item['LastName'] for item in eq.data]
    assert result == ['Goldman', 'Sommers', 'Spencer']


def test_python_developers_query():
    """The query for all the Python Developers."""
    eq = EmployeeQuery()
    eq.select('Position', 'is', 'Python Developer')
    result = [item['LastName'] for item in eq.data]
    assert result == ['Austin', 'Timberlake']

def test_phone():
    """The query for everyone with a phone number."""
    eq = EmployeeQuery()
    eq.select('phone', 'is not', 'none')
    result = [item['LastName'] for item in eq.data]
    assert result == ['Austin', 'Sommers']

def test_report_to_oscar_goldman():
    """The query for everyone who reports to Oscar Goldman"""
    eq = EmployeeQuery()
    eq.select('reports_to', 'is', 'Oscar Goldman')
    result = [item['LastName'] for item in eq.data]
    assert result == ['Austin', 'Timberlake']
