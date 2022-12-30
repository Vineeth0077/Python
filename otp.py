import random as r

def otpgen(n):
    otp=""
    for i in range(n):
        otp=otp+str(r.randint(1, 9))
    print("Your one time password is:")
    print(otp)
n=int(input())
otpgen(n)