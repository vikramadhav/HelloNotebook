# def sequence(l:list):
#     for i in range(len(l)-2):
#         if l[i]==1 and l[i+1]==2 and l[i+2]==3:
#             return True
#         else:
#           return False


# print(sequence([1,3,5,3]))



def grow_string(st:str):
    lm : str=''
    # while(len(st)>0):
    #     lm=st[0:len(st)]+lm
    #     st=st[0:len(st)-1]
    # return lm

    for i in range(len(st)):
        lm=lm+st[:i+1]
    return lm 

print(grow_string('Code'))
print(grow_string('abc'))
print(grow_string('ab'))