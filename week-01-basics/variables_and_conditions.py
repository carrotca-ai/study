#It's my first week and I started writing it on only third day of my learning!
z = 1 #variables basis: "Name = Data"
print(z) #print syntax
#many types of variables
x = int(1) #integer
print(type(x))
c = str(1) #string
print(type(c))
v = float(1) #number with .00
print(type(v))
b = complex(1j)
print(type(b))
#massive like
n = ["cherry", "burger", "ferger", 3, True] #list of any data
print(type(n))
print(n)
print(len(n)) #len syntax for measuring length
if "cherry" in n:
    print("cherry true")
else:
    print("cherry false")
m = "github"
print(f"Hello, this is template text for {m}") #f before quotes for formatting text
#something with bytes
settings = 0b1010101 #creating setting with bytes, where every number is our setting, 0 is false, 1 is true, and you need to write and read bytes right to left, when you see by your eyes left side in bytes, in code that will be right side(this blown my mind for a moment lol)
settings = settings | (1 << 1) #to set one of setting off or on! first number is 0 or 1 status, second number is position of the setting that you change.
print(bin(settings)) #for our settings get printed!
#bytes in early stages very difficult, but in fact this is very important thing, that can help you to optimize something
#you can also print something from the text starting from some point that you want, but take in mind, that in code first letter is letter 0
a = "Hello this is something I texting for my github progression!"
print(a[:5]) #this will output only "Hello" from the text!
print(a[5:10]) #this will output only "this", I think you got the concept, like me!
#also I learned some operators
print(6 + 4) #basic to + something
print(6 - 4) #like with +, but this one with the -
print(6 * 4) #I think you got the concept again!
print(6 / 4)
print(6 % 4)
print(6 ** 4) #is for squared one's
print(6 // 4)
#many intresting things that I got only in 3 days, but this is only start, I hope you will believe in me! this is not everything that I learned, I will edit this tomorrow. If you want to support me, my Paypal is: lisoilka27@gmail.com   -- I earn money for my future college in USA!
