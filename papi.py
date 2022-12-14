import requests
import json
import mysql.connector

try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='papidb')
except mysql.connector.Error as e:
    print("db connection error",e)
mycursor=mydb.cursor()
data=requests.get("https://api.publicapis.org/entries").text
data_info=json.loads(data)
for j in data_info['entries']:
    http=str(j['HTTPS'])
    try:
        #sql='INSERT INTO `papi`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ("'+j['API']+'","'+j['Description']+'","'+j['Auth']+'","'+http+'","'+j['Cors']+'","'+j['Link']+'","'+j['Category']+'")'
        #sql="INSERT INTO `papi`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ('"+j['API']+"','"+j['Description']+"','"+j['Auth']+"','"+http+"','"+j['Cors']+"','"+j['Link']+"','"+j['Category']+"')"
        sql="INSERT INTO `papi`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data=(j['API'],j['Description'],j['Auth'],http,j['Cors'],j['Link'],j['Category'])
        mycursor.execute(sql,data)
        mydb.commit()
        print("Data inserted successfully",j['API'])
    except mysql.connector.Error as e:
        print("error is",e)
    

        