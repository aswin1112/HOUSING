import hconnector
connection = hconnector.fun()
cursor = connection.cursor()

def localities():
    select_query6="""SELECT * FROM LOCALITIES"""
    rows=cursor.execute(select_query6)
    ro = cursor.fetchall()
    return ro
    
if __name__ == "__main__":
    localities()