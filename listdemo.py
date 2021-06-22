my_list=['b','d','a','z','x']
another_list=[1,2,3,4,5]


final_list=my_list[:3]
final_list.sort()
final_list.reverse()
another_list.reverse()
final_list=final_list + another_list[:3]
print(final_list)

# ['d', 'b', 'a', 5, 4, 3]