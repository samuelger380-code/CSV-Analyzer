
def check_age(age):
    age = 18
    if age >= 18:
        print('adult')
    else:
        print('minor')
    return age 

# Storing all column headers from a CSV = []
# Storing each column name and whether it's numeric or text = {}
# Storing all the values in the age Column = []

#Concept 3: Loops
    # The rule: 
        # for item in list - loops through every item
        # break - stops the loop immeddiately
        # continue - skips current item, keeps going
    
names = ["Sam", "John", "stop", "Jane", "Mike"]
for name in names: 
        if name == 'stop':
              break
        print(name) #Great work no help!!!

# 4 Functions + Return 
    # def defines a function
    # return sends a value back to whoever called it
    # without return, the function gives back none

def add_numbers(a,b):
     return a + b
print(add_numbers(10,5))

# Concept 5: try/except
# The rule:

# try — attempt this code
# except — if it fails, do this instead
# Prevents your program from crashing on bad input

def get_item(list, index):
     try:
          return list[index]
     except IndexError:
          return None
    
names = ["Sam", "John", "Jane"]
print(get_item(names, 1))
print(get_item(names, 10))
     
     


        

    

    

    
