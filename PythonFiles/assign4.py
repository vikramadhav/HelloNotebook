# def last_list(*args: list):
#     return args[-1]


# print(last_list([1,2],[3,45]))



def key_list_items(**kwargs):
    return kwargs.get(list(kwargs.keys())[-1])[-2]


print(key_list_items(people='Ram',am=['A','B','c']))