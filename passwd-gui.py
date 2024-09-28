import tkinter
import random
import string
import ctypes


def gen_passwd():
    word_in_password = word.get()

    char_list = list(word_in_password)
    char_list[2], char_list[6], char_list[4] = char_list[6], char_list[4], char_list[2]
    word_in_2 = "".join(char_list)
    print(word_in_2)

    number1 = random.randint(1, 64)
    number2 = random.randint(512, 1024)
    char1 = random.choice(string.ascii_letters)
    char2 = random.choice(string.ascii_letters)

    final_passwd = str(number1) + char2 + "-" + word_in_2 + "-" + str(number2) + char1
    passwd.set(final_passwd)


root = tkinter.Tk()
root.title("ThePassWD")
root.geometry('450x600')

word_text = tkinter.Label(root, text="Enter a 7 letters min word")
word_text.place(x=160,y=250)

word = tkinter.Entry(root)
word.place(x=170, y=300)

generate_button = tkinter.Button(root, text="Generate", command=gen_passwd)
generate_button.place(x=170, y=350)

passwd = tkinter.StringVar(root)

passwd2 = tkinter.Entry(root, textvariable=passwd, width=40)
passwd2.place(x=130, y=400)

root.mainloop()


