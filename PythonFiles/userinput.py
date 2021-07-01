
# # name=input('Enter your Name: ')
# # print('Hello {0}'.format(name))



# def twelver(a:int,b:int):
#     return (a==12 or b==12) or (a+b==12)


# print(twelver(6,6))



def pay_extra(working:bool,hour:int):
    if hour in list(range(1,9)) + list(range(20,25)) and working:
        return True
    else:
        return False


print(pay_extra(True,7))
print(pay_extra(True,9))
print(pay_extra(False,22))