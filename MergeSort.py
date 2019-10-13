#!/usr/bin/env/python3
import mysql.connector
import datetime
a = datetime.datetime.now()
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2  
        L = arr[:mid] 
        R = arr[mid:] 
  
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
       
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
            
            
            
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1


def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i]) 
    


sql = "select class_roll_no from data"
con = mysql.connector.connect(user="*****", password="**********", host="127.0.0.1", database="students")
cursor=con.cursor()
cursor.execute(sql)
r_no = []
rows = cursor.fetchall()
for row in rows:
    r_no.append(row[0])

arr = r_no.copy()
print("The sorted Class Roll numbers for given student from the database are as follows: \n")
mergeSort(arr)
printList(arr)
b = datetime.datetime.now()
c=b-a
print("The time taken for the sorting using merge sort is: " , c)
