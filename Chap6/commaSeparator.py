# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a 
#space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, 
#bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where 
#an empty list [] is passed to your function.

#PLAN
#input = list [x,y,z,a]
#output = x, y, z and a


#list = []

#def concatinate(list)
    #for i in range(len(list)-1)
        #if i == len(list)-1 then:
            #print(f" and {list[i]}")
        #else:
            #print(f"{list[i]}, "")

#main loop
#concatinate(list)

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)

list = []
logging.debug("start of program")

def concatinate(list):
    if not list: #checks if list is empty
        print("")
    else:
        for i in range(len(list)):
            logging.debug("i ="+str(i))
            if i == len(list)-1: #checks if it is the last element in the list
                print(f"and {list[i]}")
            else:
                print(f"{list[i]}, ", end=' ')

concatinate(list)


#my plan was basically just draft of the code, not the logic behind the code. in my plan there is mistakes...
#i forgot to add logic for empty string possibility aswell. i also didnt include the edge case of one list item, it also doesnt return a value ut just prints

#better blue print:
#Define a function that accepts a list (items).
# Handle edge cases first:
# If the list is empty, return an empty string.
# If the list has one item, return just that item as a string.
# Handle the main case:
# Slice the list to get all items except the last one.
# Join these items together with ", ".
# Create the final string by combining the joined slice, the string " and ", and the last item from the original list.
# Return the final string.

#geminis better code:
def format_list_string(items_list):
    # 1. Handle edge case: empty list
    if len(items_list) == 0:
        return ""
    # 2. Handle edge case: single item
    if len(items_list) == 1:
        return str(items_list[0])
    
    # 3. Handle the main case
    # Slice all items except the last and join them
    all_but_last = ", ".join(items_list[:-1])
    # Combine with the last item
    formatted_string = f"{all_but_last}, and {items_list[-1]}"
    
    return formatted_string

# --- Testing ---
spam = ['apples', 'bananas', 'tofu', 'cats']
single = ['apples']
empty = []

print(f"'{format_list_string(spam)}'")
print(f"'{format_list_string(single)}'")
print(f"'{format_list_string(empty)}'")

# Expected Output:
# 'apples, bananas, tofu, and cats'
# 'apples'
# ''