import hconnector
connection = hconnector.fun()
cursor = connection.cursor()

def fun():
    select_query6="""select r.rname as RNAME, count(f.wing) as TOTAL_NO_OF_FLATS, dense_rank() over (order by count(f.wing) desc) as RNK from flats f join buildings b on b.bno = f.bno join localities l on l.lid = b.lid join area a on a.pincode = l.pincode join region r on r.rid = a.rid group by r.rname"""
    
    rows=cursor.execute(select_query6)
    ro = cursor.fetchall()
    return ro
    
if __name__ == "__main__":
    fun()