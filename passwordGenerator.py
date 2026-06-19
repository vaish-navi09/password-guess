import random

chars = "shlok0singh4321@#"

password = ""
for i in range(8):
    password += random.choice(chars)
    
print("password", password)
