import time

#asks an user for a time they want to countdown
s = int(input("Enter the amounth of seconds you want to countdown: "))

#creates a loop and prints numbers between a specific range
for i in range(s, 0, -1):
    print("Bomb will explode in:" , i)
    
#delays each iteration with 1 second
    time.sleep(1)

print("Kaboom!")