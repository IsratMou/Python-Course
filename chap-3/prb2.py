letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''

name=input("enter your name: ")
date= input
print(name)
print(date)
print(letter.replace("<|Name|>",name))
print(letter.replace("<|Date|>",date))
