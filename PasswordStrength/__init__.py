import string

from PasswordStrength.timetocrack import timetocrack

password = input("Enter Password: ")

uppercase = any(c in string.ascii_uppercase for c in password)
lowercase = any(c in string.ascii_lowercase for c in password)
digit = any(c in string.digits for c in password)
special = any(c in string.punctuation for c in password)

criteria = [uppercase, lowercase, digit, special]
length = len(password)

score = 0

with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as f:
    exPass = {line.strip() for line in f}

if password in exPass:
    print("Password is in the list of common passwords. Please choose a different password.")
    choice = input("Would you like us to generate a strong password for you? (y/n):")
    if choice == 'y':
        from PasswordStrength.generatePass import generatePass
        password = generatePass()
        print(f"Generated password: {password}")
    elif choice == 'n':
        print("Please choose a different password.")
else:
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 16:
        score += 1
    if length > 20:
        score += 1

    print(f"Password length is {length}, adding {score} points.")

    score += max(0, sum(criteria) - 1)
    print(f"Password has {sum(criteria)} different character types, adding {sum(criteria) - 1} points.")

    if score < 4:
        strength = "very weak"
    elif score < 6:
        strength = "pretty good"
    else:
        strength = "strong"

    print(f"{password} is {strength}. Score is {score} points /7.")

crack_time = timetocrack(password)
print(f"Estimated time to crack the password: {crack_time}")

exit()
