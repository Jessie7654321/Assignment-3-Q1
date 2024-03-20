import psycopg2
from psycopg2 import sql

# Database connection parameters
conn_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost'
}


def db_connect():
    try:
        conn = psycopg2.connect(**conn_params)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None


def getAllStudents():
    conn = db_connect()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM students ORDER BY student_id")
            records = cursor.fetchall()
            for row in records:
                print(row)
        conn.close()


def addStudent(first_name, last_name, email, enrollment_date):
    conn = db_connect()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))
            conn.commit()
        conn.close()


def updateStudentEmail(student_id, new_email):
    conn = db_connect()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE students SET email = %s WHERE student_id = %s",
                           (new_email, student_id))
            conn.commit()
        conn.close()


def deleteStudent(student_id):
    conn = db_connect()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            conn.commit()
        conn.close()


# Example usage
if __name__ == '__main__':
    # Demonstrate all functions
    print("Initial students:")
    getAllStudents()

    print("\nAdding a student:")
    addStudent('New', 'Student', 'new.student@example.com', '2023-10-01')
    getAllStudents()

    print("\nUpdating student email:")
    updateStudentEmail(1, 'updated.email@example.com')
    getAllStudents()

    print("\nDeleting a student:")
    deleteStudent(1)
    getAllStudents()
