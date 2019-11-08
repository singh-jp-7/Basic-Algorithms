#!/usr/bin/env python 3
import mysql.connector
import datetime
a = datetime.datetime.now()
def partition(arr,low,high):
    
    """Function to divide in two halves"""
    
    i = ( low-1 )     
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        if   arr[j] < pivot: 
          
            
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
def quickSort(arr,low,high): 
    
    #Function to quick sort
    
    if low < high: 
  
        
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

sql = "select university_roll_no from data"
con = mysql.connector.connect(user="*****", password="*********", host="127.0.0.1", database="students")
cursor=con.cursor()
cursor.execute(sql)
r_no = []
rows = cursor.fetchall()
for row in rows:
    r_no.append(row[0])

arr = r_no.copy()
print("The sorted University Roll numbers from the database are as follows: \n")
d=len(arr)-1
quickSort(arr, 0, d)
for i in range (len(arr)):
    print(arr[i])

b = datetime.datetime.now()
c=b-a
print("The time taken for the executuion is :" ,c)
