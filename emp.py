empname=input("enter the name of employee:")
desi=input("enter the designation  of employee:")
sal=int(input("enter the employee salary:"))
sep_allow=int(input("enter the special allowance:"))
bonus=int(input("enter the bonus:"))
gr_mon=sal+sep_allow
print("gross monthly salary:",gr_mon)
gr_anl=((gr_mon*12)+bonus)
print("gross annual salary:",gr_anl)
if(gr_anl>500000):
    tx=((gr_anl*15)/100)
    print("taxable income is :",gr_anl-tx)
elif(gr_anl>400000):
    tx=((gr_anl*10)/100)
    print("taxable income is :",gr_anl-tx)
else:
    tx=((gr_anl*12)+bonus)
    print("taxable income is :",gr_anl-tx)
 
 
 