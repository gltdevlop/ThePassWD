import random
import string

print("Welcome to ThePassWD Generator. Let's get started.")
print("First, give me one word you would like to appear in your password  (Min 7 Letters)")
word_in_password = input("Word : ")

while len(word_in_password) < 7:
    print("Please enter a min 7 letters word")
    word_in_password = input("Word : ")
else:
    char_list = list(word_in_password)
    char_list[2], char_list[6], char_list[4] = char_list[6], char_list[4], char_list[2]
    word_in_2 = "".join(char_list)
    print(word_in_2)

number1 = random.randint(1,64)
number2 = random.randint(512,1024)
char1 = random.choice(string.ascii_letters)
char2 = random.choice(string.ascii_letters)

final_passwd = str(number1) + char2 + "-" + word_in_2 + "-" + str(number2) + char1
print("Your final password is " + final_passwd)




