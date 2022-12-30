import time
def countdown(n):
    print(n)
    if n==0:
        return
    else:
        countdown(n-1)
n=int(input())   
countdown(n)

'''
# import the time module
import time

# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
'''