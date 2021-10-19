# Import Graphical User Interface package
from tkinter import *

# This Function Find Odd or Even Number
def oddeven():
    n = int(entry.get())
    if n % 2 == 0:
        result.configure(text='Even number')
    else:
        result.configure(text='Odd number')

# This Function Find prime or Not
def prime():
    n = int(entry.get())
    for i in range(2, n):
        if (n % i) == 0:
            result.configure(text='is not prime')
            break
        else:
            result.configure(text='Is prime number')

# This function find factorial
def factorial():
    n = int(entry.get())
    f = 1
    for i in range(1, n + 1):
        f = f * i
    # print('factorial of', n, '=', f)
    result.configure(text = f'''fact is {f}''')

# this Function find Palindrome
def palindrome():
    n = int(entry.get())
    temp = n
    rev = 0
    while n > 0:
        last = n % 10
        n = n // 10
        rev = (rev*10)+last
    if rev == temp:
        result.configure(text='is palindrome')
    else:
        result.configure(text='is not palindrome')

# This function help to clear the result and input value
def clear():
    entry.delete(0, 'end')
    result.configure(text='Result:')


# creating basic window(Graphical User Interface)
window = Tk()
window.geometry("350x360")  # size of the window
window.resizable(0, 0)  # this prevents from resizing the window
window.title("Check the Number")   # title
label = Label(window, text='Enter Number') # to take input data
entry = Entry(window, width=30)
btn1 = Button(window, text='Odd_Even', command=oddeven) # this is the btn1 to btn5 to create button
btn2 = Button(window, text='Prime', command=prime)
btn3 = Button(window, text="Factorial", command=factorial)
btn4 = Button(window, text="Palindrome", command=palindrome)
btn5 = Button(window, text='Clear', command=clear)
result = Message(window, text='Result:', width=300)    # give output
label.grid(row=0, column=0)   # this is the position fo input label and button
entry.grid(row=0, column=1)
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=3, column=0)
btn4.grid(row=3, column=1)
btn5.grid(row=5, column=1)
result.grid(row=6, column=0, columnspan=2)
window.mainloop()


