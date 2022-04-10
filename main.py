#Password Manager

print("Password saver. Your password needs to be at least 8 letters.")
password = input("Enter your password: ")
password_confirm = input("Re-enter your password: ")

while len(password) < 8:
  print("Your password needs to be at least 8 letters.")
  password = input("Enter your password: ")
  password_confirm = input("Re-enter your password: ")

if password == password_confirm:
  print(f"The password has been set to {password}!")
else:
  print("Wrong!")
  exit()

password_prompt = input("Enter the password:\n\n")

trys = 4
if password_prompt == password:
  print("Welcome!")
  exit()
else:
  print(f"Wrong! You have {trys} trys left.")
  while trys > 0 and password_prompt != password:
    password_prompt = input("Enter the password:\n\n")
    if password_prompt != password:
      trys = trys - 1
      print(f"Wrong! You have {trys} trys left.")
    else:
      print("Correct! Welcome!")
      exit()
  if trys == 0:
    print("Out of guesses!")
    exit()
