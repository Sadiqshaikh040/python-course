#1
a="thirty "
b="days "
c="of "
d="python"
print(a+b+c+d)
#2
a="coding "
b="for "
c="all"
print(a+b+c)
#3,4,5
company="coding for all"
print(len (company))
#5
company="coding for all"
a=len(company)
print(a)
#6
company="coding for all"
a=company.upper()
print(a)
#7
company="Coding For All"
a=company.lower()
print(a)
#8  
company="coding for all"
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
company="coding for all"
b=company[7:14]
print(b)
#10 
print(company.find('all'))
#11
company="coding for all"
b=company.replace("coding", "python")
print(b)
#12
com="python for all"
m=com.replace("all","everyone")
print(m)
#25 

print( 'You cannot end a sentence with because because because is a conjunction'.replace("because",""))
#32
print (" #".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))