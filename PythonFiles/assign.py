
# def string_match(x:str,y:str):
#      lt= len(x) if len(x)<len(y) else len(y)
#      counter=0
#      for i in range(lt):
#          if x[i]==y[i] :
#              counter+=1
#          else:
#              counter=0






def sum(lst:list):
    sum=0
    isEscaped=False
    for i in range(len(lst)):
        if lst[i]!=7 and not isEscaped :
            sum+=lst[i]
        elif lst[i]==8 and  isEscaped:
            isEscaped=False
        else:
            isEscaped=True
            continue
    return sum


print(sum([1,2,2,7,1,8,1]))