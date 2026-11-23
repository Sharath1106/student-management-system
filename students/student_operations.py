import mysql.connector
from database.db_connection import get_connection

def add_student(name,age,course,city):
   connection=None
   cursor=None

   try:
        connection=get_connection()
        if connection is None:
            return
        cursor=connection.cursor() 
        query="""Insert into students (name,age,course,city) values(%s,%s,%s,%s)"""

        values=(name,age,course,city)

        cursor.execute(query,values)
        connection.commit()
        print("Student added succesfully")

   except mysql.connector.Error as e:
    print("Database Error:", e)
   except Exception  as e:
    print("unexpected Error:",e)

   finally:
    if cursor is not None:
            cursor.close()
    if connection is not None and connection.is_connected():
            connection.close()

def view_students():
    conn=get_connection()
    cursor=conn.cursor()
    query="""SELECT * From students """
    cursor.execute(query)
    students=cursor.fetchall()
    if students:
        for student in students:
            print("Name:",student[1])
            print("id:", student[0])
            print("Aage:",student[2])
            print("course:",student[3])
            print("city:",student[4])
    else:
        print("Student Records not found")
    cursor.close()
    conn.close()

def search_student():
    student_id=int(input("Enter a student Id:"))
    conn=get_connection()
    cursor=conn.cursor()
    query="""SELECT * FROM students WHERE id=%s"""
    cursor.execute(query,(student_id,))
    student=cursor.fetchone()
    if student:
        print("ID:",student[0])
        print("Name:",student[1])
        print("age:",student[2])
        print("Course:", student[3])
        print("City",student[4])
    else:
        print("Student Record Not Found")
    cursor.close()
    conn.close()

def update_student():
    conn=None
    course=None
    try:
        student_id=int(input("Enter a Student Id:"))
        New_course=input("Enter a Course to be updated:")
        conn=get_connection()
        if conn and conn.is_connected():
            print("connection successfull")
        cursor=conn.cursor()
        query="""UPDATE students
        SET course=%s
        where id=%s"""
        cursor.execute(query,(New_course,student_id,))
        conn.commit()
        if cursor.rowcount>0:
            print("Student Record Updated Successfully!")
        else:
            print("Student_id Not found")
    
    except ValueError as e:
        print("Invalid Input:",e)

    except Exception as e:
        print("Error:",e)

    finally:
        if course is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def delete_student():
    student_id=int(input("Enter a student id:"))
    conn=get_connection()
    cursor=conn.cursor()
    query="""DELETE FROM students WHERE id=%s"""
    cursor.execute(query,(student_id,))
    conn.commit()
    if cursor.rowcount>0:
        print("Student Record deleted succefully!")
    else:
        print("Student id not found")
    cursor.close()
    conn.close()    

def update_students():
    conn=None
    course=None
    try:
        student_id=int(input("enter a student id:"))
        new_course=input("Enter a course to update:")
        conn=get_connection()
        cursor=conn.cursor()
        if conn.is_connected:
            print ("Connection successfull!")

        query="""UPDATE students 
        SET course=%s
        where id=%s"""
        cursor.execute(query,(new_course,student_id,))
        conn.commit()
        if  cursor.rowcount>0:
            print("Student Record updated successfully!")
        else:
            print("Student Record not found")
    except ValueError as e:
        print("Invalid input:",e)
    except Exception as e:
        print("Error:",e)
    finally:
        if cursor is None:
            cursor.close()
        if conn is None:
            conn.close()

search_student()



