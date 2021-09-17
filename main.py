#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
lett = 0
comb_l = ""
for letter in range(0,nr_letters) :
  lett = random.choice(letters)
  comb_l += lett 
  #print(lett)
#print(comb_l)

sym = 0
comb_s = ""
for symbol in range(0,nr_symbols) :
  sym = random.choice(symbols)
  comb_s += sym 
  #print(sym)
#print(comb_s)

num = 0
comb_n = ""
for number in range(0,nr_numbers) :
  num = random.choice(numbers)
  comb_n += num 
  #print(num)
#print(comb_n)

password = comb_l + comb_s + comb_n
print(f"Here is your password : {password}" )

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

new = list(password)
#print(new)
random.shuffle(new)
#print(new)
gg= ''
for x in new :
  gg += x
print(f"Hard version of the password : {gg}")  