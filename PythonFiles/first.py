chars="</<[||]>/>"
word ='cool'
halfLength=int(len(chars)/2)
print('{0}{1}{2}'.format(chars[:halfLength],word,chars[halfLength:]))