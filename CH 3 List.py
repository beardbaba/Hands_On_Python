motorcycles = ['honda','suzuki','yamaha']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

"""
to add elements to the end of the list we use "append()"
append method makes it easy to build list dynamically as we
can start with an empty list and then add items to it using a series of append calls
"""

motorcycles.append('royal enfield')
print(motorcycles)

cars = []
print(cars)
cars.append('tata')
cars.append('koenisegg')
cars.append('volkswagen')
print(cars)

#insert elements into list
cars.insert(1,'ford') # insert at index 2, so ford is inserted after tata but before koenisegg
print(cars)


#Removing an Item

#using del statement
del cars[0]
print(cars)

#using pop method
print(cars)
popped_cars = cars.pop()
print(cars)
print(popped_cars)


last_owned = cars.pop()
print(f"My last owned car was a {last_owned.title()}")

#popping can be done from any position just mention the position within the paranthesis
#like .pop(0)

"""
Remember that each time you use pop(), the item you work with is no
longer stored in the list.
If you’re unsure whether to use the del statement or the pop() method,
here’s a simple way to decide: when you want to delete an item from a list
and not use that item in any way, use the del statement; if you want to use an
item as you remove it, use the pop() method.
"""
#3-4
guest_list = [ 'ab','bc','cd','de']
print(f"Hello Mr.{guest_list[0].title()} . I would love to invite you over for a dinner")
print(f"Hello Mr.{guest_list[1].title()} . I would love to invite you over for a dinner")
print(f"Hello Mr.{guest_list[2].title()} . I would love to invite you over for a dinner")
print(f"Hello Mr.{guest_list[3].title()} . I would love to invite you over for a dinner")
#3-5
#unavailable_guest = 'cd'
#guest_list.remove(unavailable_guest)
unavailable_guest = guest_list.pop(2)
guest_list.insert(2,'ef')
print(f"Mr. {unavailable_guest} won't be able to join the party instead Mr. {guest_list[2]} will be joining us")
print("New Invitation")
print(f"Hello Mr.{guest_list[0].title()} . I would love to invite you over for a dinner")
print(f"Hello Mr.{guest_list[1].title()} . I would love to invite you over for a dinner")
print(f"Hello Mr.{guest_list[2].title()} . I would love to invite you over for a dinner")
print(f"Hello Mr.{guest_list[3].title()} . I would love to invite you over for a dinner")
#3-6
#rest is easy so leaving it


cars = ['Bmw','audi','toyota','Subaru']
"""There will be issue in sorting if all the values are not in same case(upper or lower)
as it will sort according to the ASCII
"""
#there are two ways to sort this ----- 1) temporarily 2) permanently
cars.sort() #this sorts it permanently
print(cars)
#also cars.sort(reverse= True) will sort it in descending

print("Here is the temp sorting\n")
print(sorted(cars))
print("\nHere is the OG list")
print(cars)