import random
print("\nWEllCOME TO CODE GUESS GAME")
print("\n3 digit Code has generated now you guess the code")
print()
print()

def generate_code():
    x = [str(z) for z in range(10)]
    random.shuffle(x)
    return x[:3]

key = generate_code()

found = True
count = 0
while(found):
    count += 1
    guessCode = [ x for x in input("Enter your 3 guess code: ")]
    print()

    if(guessCode[0]==key[0] and guessCode[1]==key[1] and guessCode[2]==key[2]):
        print("You are smart you completed in {} try\n".format(count))
        found = False
    elif (guessCode[0]==key[0] or guessCode[1]==key[1] or guessCode[2]==key[2]):
        print("You are close try again\n")
    else:
        print("No where near\n")
