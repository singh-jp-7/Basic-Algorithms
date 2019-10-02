#!/usr/bin/python3
import mysql.connector


def binsearch(array, first, last, element):
    if(last >= first):
        mid = (first+last)//2
        if(array[mid] > element):
            return binsearch(array, first, mid-1, element)
        elif(array[mid] < element):
            return binsearch(array, mid+1, last, element)
        elif(array[mid] == element):
            return mid
    else:
        return -1

sql = "select roll_no from data"
con = mysql.connector.connect(user="*****", password="********", host="127.0.0.1", database="students")
cursor = con.cursor()
cursor.execute(sql)
r_no = []
rows = cursor.fetchall()
for row in rows:
    r_no.append(row[0])

array = r_no.copy()
array.sort()
element = int(input("Enter the Roll Number you want to search in the database:"))
result = binsearch(array, 0, len(array)-1, element)

if result != -1:
    print("The Roll No is found at the position: " + str(result+1) + " in the Database")
else:
    print("Sorry the Roll No " + str(element) + " is not found in the Database! ")
