name="Mou"

a ='harry' # Single quoted string
b = "harry" # Double quoted string
c = '''harry''' # Triple quoted string

nameshort=len(name)   #name er length ber kora
print(nameshort)

#slicing......
name2="Harry"
nameslice=name2[0:3]    #Harry nam k slice koro from 0th index to 3th index but exclude 3th index.(0 theke 2 porjonto count korbe and 3rd index count hbe na)

print(nameslice) #output=Har(0,1,2 th index)

character1=name2[1]
print(character1) #output: a .cause 0 to 1

#Loop through the letters in the word "banana":

for x in "banana":
 print(x) 


#Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

txt2 = "The best things in life are free!"
if "free" in txt2:
 print("Yes, 'free' is present.")

#Check if "expensive" is NOT present in the following text:

txt3 = "The best things in life are free!"
print("expensive" not in txt3)
