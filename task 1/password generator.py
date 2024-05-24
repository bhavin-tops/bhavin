import random

"""function to generate a random password of given length"""
def generate_password(length: int) -> str:
    
    charset = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
   
    return "".join(random.sample(charset, length))

pass_length = int(input("Enter the length of password : "))

password = generate_password(pass_length)

print(password)
