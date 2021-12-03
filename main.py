from datetime import datetime
from application.salary import calculate_salary
from application.people import get_employees


if __name__ == '__main__':
    print(datetime.now().date())
    calculate_salary()
    get_employees()
