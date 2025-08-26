from app import repo


def uppercase_name(employee: dict):
    employee["name"] = employee["name"].upper()


def save_employee(employee):
    uppercase_name(employee)
    return repo.save_employee(employee)


def list_employees():
    return repo.list_employees()
