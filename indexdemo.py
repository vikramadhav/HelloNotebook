# # my_list=['a','b','c','e','f','a','e','a']
# # print(my_list.count('a'))

# # tup=(1,2,3,'z','c','x','SomeDatapoint',[1,3,2,1])
# # tup[7][2]='MyUpdate'

# # # print(tup[3:5])
# # print(1,3,2,2,1,3,1,1)

# tup=(1,)

# print(type(tup))



# my_list=[{'Tom':2000,'Bill':1200},['Car','laptop','TV']]

# print(my_list[0].get('Bill'))



# org_list=['cup','cereal','milk',(8,4,3)]
# org_list.append(sorted(org_list.pop(),key= lambda x:x))
# print(org_list)



my_list=[(1,2),(3,4),(['c','d','a','m'],[3,9,4,12],4),'TV',42]

my_list[2][0][3]='x'

my_list[3]='Televisions'

print(my_list)
