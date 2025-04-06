import random
import string

charVal = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(12):
   password += random.choice(charVal)


print("Suggested Password is: ", password)

# ---list comprehension ---
# password = "".join([random.choice(charVal) for i in range(12)])
# print(password)