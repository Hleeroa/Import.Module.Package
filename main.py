import pyjokes
from datetime import datetime
from application.salary import calculate_salary as salary
from application.db.people import get_employees as employee

if __name__ == '__main__':
    print(datetime.date(datetime.now()))
    Johns_salary = salary(200, 166, 0.8)
    employee('John', 8964482728, Johns_salary)
    print(pyjokes.get_joke())



