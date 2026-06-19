import random

chars = "abcdeghigh0987654@$IJKLMNOPrstu321"

password = ""
for i in range(8):
    password += random.choice(chars)
    
print("password", password)
