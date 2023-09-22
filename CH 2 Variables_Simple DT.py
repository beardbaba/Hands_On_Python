message = "Hello Python World!"
print(message)

name = "ada lovELAce"
print(name.title())
print(name.upper())
print(name.lower())

"""in Some situation where we want to use value of
    variable inside a string we use f just before the opening quotation mark;
    put braces around the variable name to be used in a string
    """
first_name = "divyank"
last_name = "singh"
full_name = f"{first_name} {last_name}"
#print(full_name)
print(f"Hello, {full_name.title()}!")
message_1 = f"Hello, {full_name.title()}!"
print(message_1)


print("\tPython") #for adding whitespaces
print("\tPython\n\tC++") #\n for new line

#for stripping whitespaces .strip() .rstrip() and .lstrip() is used
favourite_language = "Python         "
favourite_language
favourite_language.rstrip()



famous_person = "albert einstein"
quote = "a person who never made a mistake never tried anything new"
message = f"{famous_person.title()} once said, {quote.capitalize()}."
print(message)

import this
