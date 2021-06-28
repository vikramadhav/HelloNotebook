from typing import List


def merge_list(list1: List,list2:List):
    return list1 + list2



# a=[1,3,2]
# b=['z','c','s']


# print(merge_list(a,b))



# def seprate(str):
#     return list(str)


# print(seprate('ABCVADASDASd'))

def multimerge(lst:List , mystr:str):
    return lst+ mystr.split(' ') + list(mystr)

a=[1,3,2]
b=['z','There is a ','Hello ']   


print(multimerge(a,"Hello There is a rabit"))