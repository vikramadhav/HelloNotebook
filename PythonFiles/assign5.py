def first3(number:list):
    length = len(number) if len(number) < 4  else 4
    if 6 in number[0:length]:
        return True
    else :
       return False
   
print(first3([1,2,3]))
print(first3([1,2,3,6]))
print(first3([2,3,4,8,3,1,6]))