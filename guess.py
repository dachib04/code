import random as rd



guess_number = rd.randrange(0,100)
limit = 1


guess = int(input("guess the number: "))
print('you lost, try again') 

while limit<5:
    guess = int(input('guess the number: '))
    limit += 1 
    if guess==guess_number:
        print('you won')
    else:
        print('you lost, try again')
    if limit == 5:
        print('You lost, you used all your guesses')

if guess==guess_number:
    print("you won")
print(guess_number)


while guess != guess_number:
    if guess < guess_number:
        print('it is low')
    elif guess > guess_number:
        print("it is high")

    guess = int(input('guess the number: '))
    limit +=1
    if limit == 5:
        break
    
