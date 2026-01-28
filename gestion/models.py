import cx_Oracle


class Departamento:
   def __init__(self):


       self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")


   def insert_dept(self, dept_no, dnombre, loc):
       cursor = self.connection.cursor()
       try:
           cursor.execute(
               "INSERT INTO DEPT (DEPT_NO, DNOMBRE, LOC) VALUES (:dept_no, :dnombre, :loc)",
               {"dept_no": dept_no, "dnombre": dnombre, "loc": loc}
           )
           self.connection.commit()
           return "Registro correct"


       except self.connection.Error as error:
           print("Error: ", error)


       return cursor


   def update_dept(self, dept_no, dnombre, loc):
       cursor = self.connection.cursor()
       try:
           cursor.execute(
               "UPDATE DEPT SET DNOMBRE = :dnombre, LOC = :loc WHERE DEPT_NO = :dept_no",
               {"dept_no": dept_no, "dnombre": dnombre, "loc": loc}
           )
           self.connection.commit()
           if cursor.rowcount == 0:
               return "No se encontró el depa"
           return "correcto"
       except self.connection.Error as error:
           print("Error: ", error)


       return cursor


   def delete_dept(self, dept_no):
       cursor = self.connection.cursor()
       try:
           cursor.execute(
               "DELETE FROM DEPT WHERE DEPT_NO = :dept_no",
               {"dept_no": dept_no}
           )
           self.connection.commit()
           if cursor.rowcount == 0:
               return "No se encontró el depa"
           return "correcto"
       except self.connection.Error as error:
           print("Error: ", error)


       return cursor


   def get_all(self):
       cursor = self.connection.cursor()
       try:
           cursor.execute("SELECT DEPT_NO, DNOMBRE, LOC FROM DEPT ")
           rows = cursor.fetchall()
           return [{"dept_no": r[0], "dnombre": r[1], "loc": r[2]} for r in rows]
       except self.connection.Error as error:
           print("Error: ", error)


       return cursor




   def exists_dept(self, dept_no):
       cursor = self.connection.cursor()
       try:
           cursor.execute("SELECT 1 FROM DEPT WHERE DEPT_NO = :dept_no", {"dept_no": dept_no})


       except self.connection.Error as error:
           print("Error: ", error)


       return cursor

from django.db import models

# Create your models here.
