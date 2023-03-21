#Basics

import time #stuff life time.sleep(#) 

Men = ['a', 'b', 'c']

print(men.title()) #will make this into This

for Mens in Men:
    print(Mens) #to loop untill finished (**need the print(thing) and (for thing) to be the same
    
\n #will move to a new line when printing print("Hey all,", "\nScott here")

dogs = ['dog1', 'dog2', 'dog3']

dogs[0] = 'big dog'
#replaces number in list with specified *thing*

print(dogs.index('dog1'))
#finds which number specified *thing* is at

print(dog1 in dogs)
#true or false if item is in list (this would be true)

dogs.append('dog4')
#adds *thing* to end of the list

dogs.insert(4, 'dog5')
#same as .append but you can choose where

cats [] #-- we can also make empty lists?!!??! (and then add stuff with append/insert!?!?!!)

#doing -1 for the number makes it always the newest i guess?

dogs.sort #sort into alphabetical (woah i spelled alphabetical right i think)

dogs.sort(reverse=True) #take a guess at what this does.

for dog in sorted(dogs):
    print(dog.title())
#this sorts the list but doesnt permantly change the main list

dogs.reverse() #you can also do this to reverse

numbers.sort() #puts numbers in numerical order
numbers.sort(reverse=True) #again take a guess man

print(sorted(numbers)) #same as other one put sorts while preserving og list

nod = len(dogs) #(number of dog) the amount of users in list

print(str(nod)) #len just returns an integer, which we can't print so we use str to turn it into a string and then print

del dogs (0) #will remove said number/value from list

dogs.remove('dog1') #will remove item by value (will only remove first in list if multple values)

lastdog = dogs.pop() #grabs item and removes it from list (if () empty grabs last item)

input = input("enter something here") #again take a guess man 

threedogs = dogs[0:3] #grabs everything in a list (you can leave first number empty to grab everything up to the other number, leaves og list uneffected

middledog = dogs[1:3] #another example cause why not

enddog = dogs[2:] #another another example becuase im sure you forgot this super simple bit

alldog = dogs[:] #dog, basicly a copy which you can delete stuff in idk

number = range(1,11) #range is just an easier number list (put something like ,2 after 11 to go up in twos.)

numbers = list(range(1,11)) #makes it into a list cause it wasnt in one before i guess

for number in numbers[-10:]:
    print(number) 
#i forgot about this before i think and i dont feel like checking
    
print(str(len(numbers)) #len = lenght (i think idk) and str turns (integers?) into strings that can be printed
      
small = min(numbers)
big = max(numbers)
total = sum(numbers)
      
#so didnt do anything for 2 months lol nice
      
import sys
#figure it out yourself, idc
if sys.platform.startswith('linux'):
      print("yippe")
    


num1 = 1_000_000_000

num2 = 2_000

ans = num1*num2
print(f'{ans:_}')

      
      
      










#------------------- FUNCTIONS (stfu i know this is badly orginazed but whatever)
#i feel like you should remember this but idc
def (*thing*)(argument) #to create a function

#probably bad example i just made (does work tho, do remeber to put () after title cause apparently that can mess stuff up)
def dog(names, message):
  print(message)
  for name in names:
    print(name.title())
    
names = ['Charlie', 'Max', 'Hailey']
names.sort()
dog(names, "Dog!!")

#just took this from (http://introtopython.org/introducing_functions.html) lmao


def get_number_word(number):
    # Takes in a numerical value, and returns
    #  the word corresponding to that number.
    if number == 0:
        return 'zero'
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    else:
        return "I'm sorry, I don't know that number."
    
# Let's try out our function.
for current_number in range(0,6):
    number_word = get_number_word(current_number)
    print(current_number, number_word)





