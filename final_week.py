import mysql.connector

#Create mysql
myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "113801", auth_plugin='mysql_native_password')

cur = myconn.cursor()

#print(cur)

try:
    #cur.execute('create database new1')
    cur.execute("show databases")
    cur.execute("use userlogin")
    myconn.commit()
    print(cur)
    print(myconn.commit())
except:
    myconn.rollback()
"""for i in cur:
    print(i)"""
myconn.close()
