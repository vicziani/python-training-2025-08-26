import psycopg2
import os


def connect():
    host = os.getenv("DB_HOST", "localhost")
    """Connect to the PostgreSQL database."""
    return psycopg2.connect(
        host=host, user="employees", password="employees", dbname="employees"
    )


def init():
    """Initialize the repository."""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL
                );
            """)


def save_employee(employee: dict) -> dict:
    """Save an employee to the repository."""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO employees (name) VALUES (%s) RETURNING id, name;",
                (employee["name"],),
            )
            saved_employee = cur.fetchone()
            return {"id": saved_employee[0], "name": saved_employee[1]}


def list_employees() -> list[dict]:
    """List all employees in the repository."""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM employees;")
            rows = cur.fetchall()

            return [{"id": row[0], "name": row[1]} for row in rows]


if __name__ == "__main__":
    init()

    employee = {"name": "John Doe"}
    saved_employee = save_employee(employee)
    print(f"Saved employee: {saved_employee}")

    employees = list_employees()
    print(f"All employees: {employees}")
