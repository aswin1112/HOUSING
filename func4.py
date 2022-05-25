import hconnector
connection = hconnector.fun()
cursor = connection.cursor()

def fun():
    select_query6="""select p.hname as HNAME from peoples p join flats f on p.wing = f.wing join buildings b on b.bno = f.bno join localities l on l.lid = b.lid join area a on a.pincode = l.pincode join region r on r.rid = a.rid WHERE r.rname = 'B_EAST'"""
    
    rows=cursor.execute(select_query6)
    ro = cursor.fetchall()
    return ro
    
if __name__ == "__main__":
    fun()