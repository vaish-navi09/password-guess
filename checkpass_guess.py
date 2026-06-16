
# def checkpassword():
#     password = input("enter the password")
#     hasupper = False
#     hasdigit = False
#     for ch in password:
#         if ch .isupper():
#             hasupper = True
#         if ch .isdigit():
#             hasdigit= True
#     if len(password) >= 8 and hasupper and hasdigit:
#             print("strong password")
#     else:
#             print("not strong")

# print(checkpassword())
# with open ("text.txt", "w") as f:
#     f.write("python\n github\n welcome world")

# with open ("text.txt", "r") as f:
#      data = f.readlines()
#      print(data)
# with open ("text.txt", "r") as f:
#      data = f.read()
#      z = data.splitlines()
#      print(len(z))

# secret = 7 

# while True:
#     guess = int(input("enter the number"))
#     if guess > secret :
#         print("high")
#     elif guess < secret :
#         print("low")
#     else:
#         print("correct")
#         break