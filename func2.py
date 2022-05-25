import hconnector
connection = hconnector.fun()
cursor = connection.cursor()

def fun():
    select_query6="""SELECT DNAME, HNAME FROM PEOPLES"""
    
    rows=cursor.execute(select_query6)
    ro = cursor.fetchall()
    return ro
    
if __name__ == "__main__":
    fun()