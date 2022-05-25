import mysql.connector

def fun():
       try :
            connection = mysql.connector.connect(host='localhost',user='root',passwd="Murthy*****",database="housing")
            return connection
       except:
            return "NOT CONNECTED"
            
if __name__ == "__main__":
    fun()
    