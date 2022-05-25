import hconnector
connection = hconnector.fun()
cursor = connection.cursor()

def buildings():
    select_query6="""SELECT * FROM BUILDINGS"""
    rows=cursor.execute(select_query6)
    ro = cursor.fetchall()
    return ro
    
if __name__ == "__main__":
    buildings()