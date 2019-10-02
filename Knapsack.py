#!/usr/bin/python3
import mysql.connector
import datetime
capacity=int(input("Enter the capacity of your knapsack:\n"))

# Sql queries to connect to database

sql="select Val,weight,ratio from knapsack"
con=mysql.connector.connect(user="******", password="*********", host="localhost", database="knapsack")
cursor=con.cursor()
cursor.execute(sql)

# Sorting according to the values in decreasing order

Val=[]
rows=cursor.fetchall()
# print(rows)

data = {}
for row in rows:
    data[row[0]] = row[1]

data1 = {}
for row in rows:
    data1[row[2]] = row[1]

for row in rows:
    Val.append(row[0])
arr=Val.copy()
arr.sort(reverse = True)

""" print("\nThe sorted values are:\n")
for i in range(len(arr)):
    print(arr[i])
 """
# Sorting according to the weights in increasing order

# print("\nThe sorted weights are as follows:\n")
weight=[]

for row in rows:
    weight.append(row[1])
arr1=weight.copy()
arr1.sort()
""" for j in range(len(arr1)):
    print(arr1[j]) """

# Sorting according to the ratio of values to the weights

# print("\nThe sorted ratios are as follows:\n")
ratio=[]
for row in rows:
    ratio.append(row[2])
arr2=ratio.copy()
arr2.sort(reverse = True)
""" for k in range(len(arr2)):
    print(arr2[k])
 """
def criteria1():
    # Sort according to value in decreasing order
    weight=0
    finalvalue=0
    for i in range(len(arr)):
        t = data[arr[i]]
        if weight + t <= capacity:
            weight = weight + t

            finalvalue = finalvalue + arr[i]
    print("The weight in knapsack when sorted according to values in decreasing order is :",weight,"\n")
    print("And the value is:",finalvalue)
    
def criteria2():
    # Sort according to increasing weights
    Weight=0
    finalvalue=0
    for j in range(len(arr1)):
        t = arr1[j]

        if Weight + t <= capacity:
            Weight = Weight + t

            val = list(data.keys())[list(data.values()).index(t)]

            finalvalue += val
            
    print("\nThe weight in knapsack when sorted according to increasing weights  is :",Weight)
    print("\nAnd the value is:",finalvalue)

def criteria3():
    # Sort according to the ratio of value to weight
    Weight=0
    finalvalue = 0
    for k in range(len(arr2)):
        temp = data1[arr2[k]]

        if Weight + temp <= capacity:
            Weight = Weight + temp
            val = temp * arr2[k]

        else:
            remain = capacity - Weight
            Weight = Weight + remain
            val = arr2[k] * remain


        finalvalue += val

    print("\nThe weight of knapsack when we consider the ratio of value to weight is:",Weight)
    print("\nAnd the value is:",finalvalue)

criteria1()

criteria2()

criteria3()
