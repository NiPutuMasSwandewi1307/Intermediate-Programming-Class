import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database= "login_uas_sem2" # The "Users" Table
)
