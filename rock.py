import random

m = str(input("rock, paper or scissor: "))
n = random.choice(["rock", "paper", "scissor"])



while m == "rock" :
    if m != n and n != 'paper':
        print('You won')
    elif m==n:
        print('Tie')
    else:
        print('You lost')
    
    break

while m == "scissor" :
    if n != m and n != 'rock':
        print('You won')
    elif m==n:
        print('Tie')
    else:
        print('You lost')
        
    break

while m == "paper" :
    if n != m and n != 'scissor':
        print('You won')

    elif m==n:
        print('Tie')
    else:
        print('You lost')
    
    break

print(n)



# if m == "rock" and m != n and n != 'paper' :
#     print('You won')
# elif m==n:
#     print('Tie')
# else:
#     print('You lost')
# if m == "scissor" and n != m and n != 'rock':
#     print('You won')

# elif m==n:
#     print('Tie')
# else:
#     print('You lost')  

# if m == "paper" and n != m and n != 'scissor':
#     print('You won')

# elif m==n:
#     print('Tie')
# else:
#     print('You lost')  


