#!/usr/bin/python3
import mysql.connector


def binarysearch(arr, left, right, x):
    if(left >= right):
        mid = (left+right)//2
        if(arr[mid] >x):
            return binarysearch(arr, left, mid-1,x)
        elif(arr[mid] <x):
            return binarysearch(arr, mid+1, right,x)
        elif(arr[mid] == x):
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

arr = r_no.copy()
arr.sort()
x = int(input("Enter the Roll Number you want to search in the database:"))
x = binarysearch(arr, 0, len(arr)-1, x)

if (result!= -1):
    print("The Roll No is found at the position: " + str(result+1) + " in the Database")
else:
    print("Sorry the Roll No " + str(x) + " is not found in the Database! ")
