# Simple modification to password_1.py using a while loop and if/else conditions
password = 'password'
tries = 0
print ('Hello, welcome to this app')
print ()
print ('-'*10)
print ('Can I have a name?')

userName = input()

print ('Nice to meet you, ' + userName)
print ()
print ('You see, ' + userName + '... We are not a trustfull bunch...')
print ('I need to confirm you are who you say you are')
print ('PASSWORD???')

userPass = input()

print('-'*10)

while userPass < password:
     print ('Do not test my patience. Try again')
     userPass = input()
     tries = tries + 1
     if tries >= 3:
        print ('No chance in hell you are coming in!')
        break

if userPass == password:
    print ('Did not doubt you for a second')
    print()
    print('Welcome to the Criminal Den!')

