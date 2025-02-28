# Resource for making this was: https://www.youtube.com/watch?v=NzSCNjn4_RI


import tkinter as tk

#   Basic calculations

calculation = ""

#   Defining functions

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation(): #   Evaluating Python statenments
    global calculation
    try:
            calculation = str(eval(calculation))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
    except:
         clear_field()
         text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")




root = tk.Tk()  #   Create the object
root.geometry("300x320")    #   Create the window of the calculator


text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)   #   Defining grid structure 


#   Creating buttons

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))   #   Creating the button
btn_1.grid(row=2, column=1)   #   Specifising where us the button located

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))   #   Creating the button
btn_2.grid(row=2, column=2)   #   Specifising where us the button located

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))   #   Creating the button
btn_3.grid(row=2, column=3)   #   Specifising where us the button located

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))   #   Creating the button
btn_4.grid(row=3, column=1)   #   Specifising where us the button located

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))   #   Creating the button
btn_5.grid(row=3, column=2)   #   Specifising where us the button located

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))   #   Creating the button
btn_6.grid(row=3, column=3)   #   Specifising where us the button located

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))   #   Creating the button
btn_7.grid(row=4, column=1)   #   Specifising where us the button located

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))   #   Creating the button
btn_8.grid(row=4, column=2)   #   Specifising where us the button located

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))   #   Creating the button
btn_9.grid(row=4, column=3)   #   Specifising where us the button located

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))   #   Creating the button
btn_0.grid(row=5, column=2)   #   Specifising where us the button located

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))   #   Creating the button
btn_plus.grid(row=2, column=4)   #   Specifising where us the button located

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))   #   Creating the button
btn_minus.grid(row=3, column=4)   #   Specifising where us the button located

btn_mult = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))   #   Creating the button
btn_mult.grid(row=4, column=4)   #   Specifising where us the button located

btn_divide = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))   #   Creating the button
btn_divide.grid(row=5, column=4)   #   Specifising where us the button located

btn_procent = tk.Button(root, text="%", command=lambda: add_to_calculation("%"), width=5, font=("Arial", 14))   #   Creating the button
btn_procent.grid(row=5, column=1)   #   Specifising where us the button located

btn_zarez = tk.Button(root, text=",", command=lambda: add_to_calculation(","), width=5, font=("Arial", 14))   #   Creating the button
btn_zarez.grid(row=5, column=3)   #   Specifising where us the button located

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))   #   Creating the button
btn_equals.grid(row=6, column=3, columnspan=2)   #   Specifising where us the button located

btn_clear = tk.Button(root, text="c", command=clear_field, width=11, font=("Arial", 14))   #   Creating the button
btn_clear.grid(row=6, column=1, columnspan=2)   #   Specifising where us the button located



root.mainloop() #   Runs the main loop