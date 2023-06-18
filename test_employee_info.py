import employee_info as info

def test_def_get_employees_by_age_range():
    result = info.get_employees_by_age_range(25,36)
    ans = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
            ]
    assert (result == ans)

def test_calculate_average_salary():
    result=info.calculate_average_salary()
    assert (result == 60166.666666666664)

def test_get_employees_by_dept():
    result = info.get_employees_by_dept('Sales')
    ans = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
        ]
    assert (result == ans)

def test_