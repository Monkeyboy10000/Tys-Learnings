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

dogs.append('dog3')
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
