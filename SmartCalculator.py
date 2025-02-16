from tkinter import *

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by Zero"

def mod(a, b):
    return a % b

def lcm(a, b):
    from math import gcd
    return (a * b) // gcd(int(a), int(b))

def hcf(a, b):
    from math import gcd
    return gcd(int(a), int(b))

def extract(text):
    numbers = []
    for word in text.split():
        try:
            numbers.append(float(word))
        except ValueError:
            pass
    return numbers

def calculate():
    text = textin.get().upper()
    for key, func in operations.items():
        if key in text:
            try:
                numbers = extract(text)
                if len(numbers) >= 2:
                    result = func(numbers[0], numbers[1])
                    result_list.delete(0, END)
                    result_list.insert(END, result)
                else:
                    raise ValueError("Insufficient numbers provided")
            except Exception as e:
                result_list.delete(0, END)
                result_list.insert(END, f"Error: {str(e)}")
            return
    
    result_list.delete(0, END)
    result_list.insert(END, "Error: Invalid operation")

operations = {
    'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
    'SUBTRACT': sub, 'DIFFERENCE': sub, 'MINUS': sub, 'SUBTRACTION': sub,
    'LCM': lcm, 'HCF': hcf, 'PRODUCT': mul, 'MULTIPLICATION': mul, 'MULTIPLY': mul,
    'DIVISION': div, 'DIV': div, 'DIVIDE': div,
    'MOD': mod, 'REMAINDER': mod, 'MODULUS': mod
}

win = Tk()
win.geometry('550x300')
win.title('Smart Calculator')
win.configure(bg='skyblue')

Label(win, text='Welcome to my World', font=("Arial", 12, "bold"), bg='skyblue').pack(pady=10)
Label(win, text="Instructions Please", font=("Arial", 10), bg='skyblue').pack()

textin = StringVar()
Entry(win, width=40, textvariable=textin).pack(pady=5)

Button(win, text='Execute', command=calculate, font=("Arial", 10, "bold"), bg="lightgray").pack(pady=5)

result_list = Listbox(win, width=30, height=3)
result_list.pack(pady=10)

win.mainloop()