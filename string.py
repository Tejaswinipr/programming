#string operations

#converting given string to int incomp
n="100110"
print(int(n))
print("\n")

#adding given 2 numbers in string format
a=input("first number:")
b=input("Second number:")
print(a+b)

#assigning a paragraph to variable and print
para="""Hi everyone. Welcome to Python programming.
Python is a High Level Language... because it can run in any platform,
easy to write and debubg, etc."""
print("\n"+para+"\n")

#applying slice function to get the middle name incomp
name=input("Enter your full name:")
middle_name = slice(name)
print(middle_name)
print("\n")

#replace your last name with mother name
last_name=name[-1]
mother_name=input("Enter you mother name:")
print(name.replace(last_name,mother_name)+"\n")

#print in lowercase and uppercase
print(name.lower())
print(name.upper())

#print sentence word by word using split()
x = para.split(" ")
print("\n")
print(x)

#function tohold common variable
def bdy(name):
    wish="Happy Birthday {}"
    print("\n"+wish.format(name))
bdy(name)

#to find output
itemno=567
quantity=5
price=25
myorder="I want {} pieces of item{} for {}dollars"
print(myorder.format(quantity,itemno,price))

#using escape sequence to print sentence with special charaters
print("\nCorona virus is also known as \"Covid-19\"")

