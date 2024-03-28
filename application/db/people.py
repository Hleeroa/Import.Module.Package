def get_employees(name: str, phone_number: int, salary) -> dict:
    employee = dict(name = name, phone_number = phone_number, salary = salary)
    print(f'Our employee is called {name}, you call him with number {phone_number}, their salary is {salary}₽')
    return employee
