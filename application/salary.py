from typing import Union


def calculate_salary(hours: Union[int, float], salary_rate: int, coefficient: float) -> Union[int, float]:
    print('Calculating salary...')
    salary: Union[int, float] = hours*salary_rate+hours*salary_rate*coefficient
    print(f"Salary = {salary}")
    return salary
