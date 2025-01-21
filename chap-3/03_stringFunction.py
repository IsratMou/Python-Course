name= "harry"

print(len(name))

print(name.endswith("arry")) #true dibe

print(name.startswith("Ha")) #false dibe
print(name.capitalize()) #Harry bnabe. name=harry vai hole output: Harry vai [Vai banabe na]

# some more functions
text = "Hello, World!"
print(text.lower())  # Output: "hello, world!"
print(text.upper()) # Output: "HELLO, WORLD!"


#Removes leading and trailing whitespace (or specified characters).
text = "   Hello, World!   "
print(text.strip())  # Output: "Hello, World!"


text = "I like Python"
print(text.replace("Python", "Java"))  # Output: "I like Java"

text = "apple,banana,cherry"
print(text.split(","))  # Output: ["apple", "banana", "cherry"]


words = ["apple", "banana", "cherry"]
print(", ".join(words))  # Output: "apple, banana, cherry"


text = "Hello, World!"
print(text.find("World"))  # Output: 7

text = "hello world"
print(text.title())  # Output: "Hello World"

text = "Python"
print(text.isalpha())  # Output: True. Checks if all characters in the string are alphabetic.

text = "12345"
print(text.isdigit())  # Output: True


text = "banana"
print(text.count("a"))  # Output: 3. Counts the occurrences of a substring in the string.

#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Check if an object is an integer or not:

x = 200
print(isinstance(x, int))






