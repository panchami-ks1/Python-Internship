# Function without arguments
def welcome():
    return 'Welcome'


x = welcome()
print(x)


# Function with arguments

def welcome(name):
    return 'Welcome ' + name


x = welcome('steve')
print(x)


# Function with Optional parameter(parameter with default value)

def welcome(name='Robert'):
    return 'Welcome ' + name


x = welcome()
print(x)


# Arbitrary arguments
def fruits(*arg):
    for fruit in arg:
        print(fruit)


fruits('Apple', 'Orange', 'Grape')


# Keyword arguments

def person(name1, name2, name3):
    print(name2)


person(name1='Arjun', name2='Ishi', name3='Ishika')


# Arbitrary keyword arguments

def details(**person):
    print(person['name'] + " from " + person['place'])


details(name='Ishi', place='Kerala')


# Passing list as argument

def fruits(fruits):
    for fruit in fruits:
        print(fruit)


list1 = ['Apple', 'Orange', 'Banana']
fruits(list1)


# Nested functions

def func1(arg1):
    def func2():
        print('Welcome ' + arg1)

    func2()


func1('Function2')


# Pass an empty function without errors

def future_fun():
    pass
