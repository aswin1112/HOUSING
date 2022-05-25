import regionf
import areaf
import localitiesf
import buildingf
import flatsf
import peoplesf
import func1
import func2
import func3
import func4
import func5
import func6
from tabulate import tabulate 

def region():
    r = regionf.region()
    table = tabulate(r, headers = ['RID','RNAME'], tablefmt = 'fancy_grid')
    print(table)
    
def area():
    r = areaf.area()
    table = tabulate(r, headers = ['PINCODE','RID','ANAME'], tablefmt = 'fancy_grid')
    print(table)
 
def localities():
    r = localitiesf.localities()
    table = tabulate(r, headers = ['LID','STEETNAME','PINCODE'], tablefmt = 'fancy_grid')
    print(table)

def buildings():
    r = buildingf.buildings()
    table = tabulate(r, headers = ['LID','BNO','BNAME'], tablefmt = 'fancy_grid')
    print(table)
    
def flats():
    r = flatsf.flats()
    table = tabulate(r, headers = ['FLAT_NO','BNO','WING'], tablefmt = 'fancy_grid')
    print(table)
 
def peoples():
    r = peoplesf.peoples()
    table = tabulate(r, headers = ['PID','WING','HNAME','DNAME'], tablefmt = 'fancy_grid')
    print(table)
    

def question1():
    r = func1.fun()
    table = tabulate(r, headers = ['RNAME','TOTAL_NO_OF_FLATS'], tablefmt = 'fancy_grid')
    print(table)

def question2():
    r = func2.fun()
    table = tabulate(r, headers = ['DNAME','HNAME'], tablefmt = 'fancy_grid')
    print(table)
    
def question3():
    r = func3.fun()
    table = tabulate(r, headers = ['RNAME','TOTAL_NO_OF_FLATS','RANK'], tablefmt = 'fancy_grid')
    print(table)

def question4():
    r = func4.fun()
    table = tabulate(r, headers = ['HNAME'], tablefmt = 'fancy_grid')
    print(table)
    
def question5():
    r = func5.fun()
    table = tabulate(r, headers = ['RNAME','TOTAL_NO_OF_LOCALITIES'], tablefmt = 'fancy_grid')
    print(table)

def question6():
    r = func6.fun()
    table = tabulate(r, headers = ['TOTAL_NO_OF_FLATS'], tablefmt = 'fancy_grid')
    print(table)


    
if __name__ == "__main__":
    region()
    area()
    localities()
    buildings()
    flats()
    peoples()
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    
    