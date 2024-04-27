# 1. random olaraq 6 rəqəmli otp kod generasiya edən python proqramı yazın

import random
import string

def rand_pass(size):
    generate_pass=''.join([random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)for n in range(size)])    
    return generate_pass 

generated_otp = rand_pass(6)
print('new OTP :'+generated_otp)

while True:
    OTP = input('enter your OTP here:')
    if OTP == generated_otp:
        print('Correct OTP')
        break
    else:
        print('ACCESS DENIED.')
        continue