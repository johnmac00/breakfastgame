from sys import exit

def entrance_prompt():
    print('\n')
    print("Welcome to The Breakfast Chronicles.")
    print('''Would you like to play The Breakfast Chronicles?
1. Enter (1) for yes.
2. Enter (2) for no.
    ''')

    choice = input("> ")

    if choice == "1":
        pid()#change this back to pid()
    elif choice == "2":
        end("Ok goodbye!")

    else:
        end("Ok goodbye!")


def pid():
    print(f'Please enter your DOB, {name}')
    DOB = input('DOB> ')
    print(f'Please enter your hair color, {name}')
    hair_color = input('Hair Color> ')
    print(f'Please enter your eye color, {name}')
    eye_color = input('Eye Color> ')
    print(f'Ok, you are {name}, born {DOB}, with {hair_color} hair, and {eye_color} eyes.')
    print('Is this correct?')

    choice = input('> ')

    if choice == "yes":
        print('.... loading')
        print('.... loading')
        print('please press enter for confirmation')

        choice = input('> ')

        print('Thank you for your enrollment in Mail-Serve.')
        input()
        instructions()

    else:
        pid()


def instructions():
    print(f"Let's begin, {name}!")
    print('''
First, some instructions. Type in the option given in <Option>
to choose a route! If not specificed, yes or no will suffice
''')
    print("For example: Go outside? <yes> or <no> \n")
    print(f"Make Sense {name}? <yes> or <no>...  Type w/o <>")

    choice = input("> ")

    if choice == "yes":
        begin()

    else:
        end("Ok!")

def begin():
    print(f'You wake up in Boston {name} and it\'s really cold.')
    print(f'Do you stay <inside> for breakfast {name}, or <go out> for breakfast')

    choice = input("> ")

    if choice == "inside":
        print(f"Good choice {name}, but your food options are limited. Are you sure. <yes> or <no>")

        choice = input(">")

        if choice == "yes":
            print('Okie dokie!')
            inside_breakfast()

        elif choice == "no":
            print('Ok outside we go!')
            outside_coat()

        else:
            print("invalid entry, retry")
            begin()

    elif choice == "go out":
        print(f"Ok {name} put on the parka, we're going outside for breakfast!")
        outside_coat()

    else:
        print("please retry!")
        begin()

def inside_breakfast():
    print('Open up your fridge, what\'s in there? I see waffles!')
    print(f'Do you want waffles {name}?')

    choice = input("> ")

    if choice == "yes":
        waffles()

    else:
        print('''
Well, let\'s go back to the fridge and see what else is there.
...
...
...
        ''')
        fridge_reexamine()

def waffles ():
    print(f"Great choice on the waffles {name}, I've always found them nutritious")
    print("<syrup> or <jam> on those puppies?")

    choice = input("> ")

    if choice == "syrup":
        end("A classic, yet orthodox choice. You've won breakfast!")

    else:
        end('''
    Jam is becoming much more mainstream on waffles!
    Good choic on a hip breakfast!
    ''')


def fridge_reexamine():
    print('I see some greek yogurt or eggs.')
    print('''
<greek yogurt>
<eggs>
<abandon hopes and go out for breakfast>
    ''')

    choice = input('> ')

    if choice == "greek yogurt":
        greek_yogurt()

    elif choice =="eggs":
        eggs()

    else:
        outside_coat()


def greek_yogurt():
    print('''
    Alright solid choice, healthy, low fat but full of protein.
    <granola>, <fruit>, <both>, or <plain>?''')

    choice = input("> ")

    if choice == "granola" or "fruit" or "both" or "plain":
        end("Good choice on a hearty breakfast!")

    else:
        print("Unless you want some eggs, looks like no breakfast! Eggs?")

        choice = input("> ")

        if choice == "yes":
            eggs()

        else:
            end("Well I guess no breakfast for you")

def eggs():
    print("Eggs are a classic mechanism of food injestion")
    print("<over-easy>, <scrambled> or <boiled>")

    choice = input('> ')

    if choice == "over-easy" or "scrambled" or "boiled":
        end("Looks like you'll have a great breakfast!")

    else:
        print("That wasn't valid, but let's get back to the fridge! Yes?")

        choice = input('> ')

        if choice == "yes":
            fridge_reexamine()

        else:
            end("Well maybe don't eat!")

def outside_coat():
    print('''
You step outside and it's cold! Do you want to go back in and put on
another coat?''')

    choice = input("> ")

    if choice == "yes":
        outside()

    else:
        outside()



def outside():
    print('Ok we\'re outside, and properly dressed')
    print('Walking down the street towards Newbury Street, you see a few options.')
    print('''Do you want to go to a <diner>, or a nice <sitdown> restaurant,
or <something else>?''')

    choice = input('> ')

    if choice == "diner":
        print('Ok off to a diner!')
        diner_option()

    elif choice == "sitdown":
        print('Ok to a sitdown we go.')
        continue_outside()

    else:
        print('Ok, well what type of food would you like?')

        choice = input('> ')

        food(f'Ok great choice on {choice}')

def food(type):
    print(type, ',that\'s an unorthodox choice but good!')
    print('What\'s your favorite type?')

    choice = input('> ')

    end(f'Well good choice on {choice}')

def diner_option():
    print('Strolling down Newbury street, there isn\'t a diner to be found')
    print('''But out of the corner next to the Patagonia, a man sunglasses
approaches you''')
    print('He says: \'Do you want to eat at a diner??\'.. <yes> <no>')

    choice = input('> ')

    if "yes" in choice or "Yes" in choice:
        swarthydinerman()

    else:
        continue_outside()

def swarthydinerman():
    print(''''You follow him on a subway out to Allston, the land
of diners''')
    print('''He asks you, will this diner suffice? It is exceptionally
greasy and old looking. You say....''')

    choice = input('> ')

    if "yes" in choice or "Yes" in choice:
        end('Most excellent gastrointestinal choice!')

    else:
        continue_outside()

def continue_outside():
    print('Probably a good idea to avoid gastrointestinal distress')
    print('You\'ve reached a few options, boils down to:')
    print('''1. Trident Bookstore Cafe
2. Starbucks
3. Brunch place
    ''')

    choice = input('> ')

    if "trident" in choice or "1" in choice or "brunch" in choice or "3" in choice or "bougie" in choice:
        end('Most excellent choice, although sorry for your wallet!')

    elif 'starbucks' in choice or 'Starbucks' in choice or '2' in choice:
        end('Starbucks isn\'nt too creative.')

    else:
        print('Please re-choose! Or exit the game')
        print('1. Trident, 2. Starbucks, 3. Brunch 4. Exit')

        choice = input('> ')

        if "1" in choice or 'trident' in choice or 'Trident' in choice:
            end('Pricey, but excellent choice')

        elif "2" in choice or "starbucks" in choice or "Starbucks" in choice:
            end('Not too imaginative but that\'ll do')

        elif '3' in choice or 'brunch' in choice or 'Brunch' in choice:
            end('Pricey but always worth it.')

        else:
            end('Too bad.')
            end('Pricey, but definitely worth it.')

def end(way):
    print(way, "See you next time.")
    exit(0)


##start script

print('What\'s your name?')
name = input('> ')

print('How hungry are you on a scale of 1 -> 10?')

choice = input('> ')

if choice == '6' or choice == '7' or choice == '8' or choice == '9' or choice == '10':
    print('You are sufficiently hungry to begin your quest.')
    entrance_prompt()

else:
    end("That's silly, try again another time.")
