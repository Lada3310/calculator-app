first = int(input('enter 1 num'))
second = int(input('enter 2 num'))
action = str(input('enter your action'))

if action == '+':
    print(first + second)

elif action == '-':    
    print(first - second)

elif action == '*':    
    print(first * second)

elif action == '/':    
    print(first / second)

else:
    print('di nahui')