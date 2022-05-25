import hconnector
connection = hconnector.fun()
cursor = connection.cursor()

def fun():
    select_query6="""select r.rname as RNAME , COUNT(LID) as TOTAL_NO_OF_LOCALITIES from localities l join area a on a.pincode = l.pincode join region r on r.rid = a.rid group by r.rname"""
    
    rows=cursor.execute(select_query6)
    ro = cursor.fetchall()
    return ro
    
if __name__ == "__main__":
    fun()