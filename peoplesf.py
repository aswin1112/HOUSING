import hconnector
connection = hconnector.fun()
cursor = connection.cursor()

def peoples():
    select_query6="""SELECT * FROM PEOPLES"""
    rows=cursor.execute(select_query6)
    ro = cursor.fetchall()
    return ro
    
if __name__ == "__main__":
    peoples()