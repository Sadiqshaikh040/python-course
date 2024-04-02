# it_companies1 = ['Facebook', 'Google', 'Microsoft','Nitin', 'Apple', 'IBM', 'Oracle', 'Amazon']

# #future me problem
# def middle_element(it_companies):
#     it_companies = it_companies[3:]
#     it_companies = it_companies[:-2]
#     it_companies = it_companies[0:len(it_companies) // 2]  + it_companies[len(it_companies) // 2 + 1 :]
    
#     #pop,sort(arg) return (arg = sort_arg)
#     return it_companies

# print(middle_element(it_companies1))
ages = [1,2,3,4,5,6,7,8,9,10,11]
ages.sort()

print(len(ages),len(ages)//2)
print('%0.2f'%((ages[len(ages)//2] + ages[~(len(ages)//2)])/2))

x = ages[5:]
print(x,ages)