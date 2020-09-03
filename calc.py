import tkinter as tk


class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.resizable(width=False, height=False)

        self.tk_user_calculation = tk.StringVar()
        self.string_user_calculation = ""
        self.answer = ""
        self.string_calculation = ""
        # initialises variables for later use

        calc_label = tk.Label(self.root, bg="light slate grey", text="calculator", font="helvetica", width="30",
                              height="3").grid(row=0, columnspan=4)
        # label that says calculator

        output_label = tk.Label(self.root, textvariable=self.tk_user_calculation, font="helvetica", width="30",
                                height="4",
                                bg="light gray").grid(row=1, columnspan=4)
        # label that outputs user input and answers dynamically

        _1button = tk.Button(self.root, text="1", height="5", width="5", bg="light cyan",
                             command=lambda: self.add_to_calculation("1")).grid(row=2, column=0)

        _2button = tk.Button(self.root, text="2", height="5", width="5", bg="light cyan",
                             command=lambda: self.add_to_calculation("2")).grid(row=2, column=1)

        _3button = tk.Button(self.root, text="3", height="5", width="5", bg="light cyan",
                             command=lambda: self.add_to_calculation("3")).grid(row=2, column=2)

        add_button = tk.Button(self.root, text="+", height="5", width="5", bg="light cyan",
                               command=lambda: self.add_to_calculation("+")).grid(row=2, column=3)

        _4button = tk.Button(self.root, text="4", height="5", width="5", bg="light cyan",
                             command=lambda: self.add_to_calculation("4")).grid(row=3, column=0)

        _5button = tk.Button(self.root, text="5", height="5", width="5", bg="light cyan",
                             command=lambda: self.add_to_calculation("5")).grid(row=3, column=1)

        _6button = tk.Button(self.root, text="6", height="5", width="5", bg="light cyan",
                             command=lambda: self.add_to_calculation("6")).grid(row=3, column=2)

        subtract_button = tk.Button(self.root, text="-", height="5", width="5", bg="light cyan",
                                    command=lambda: self.add_to_calculation("-")).grid(row=3, column=3)

        _7button = tk.Button(self.root, text="7", height="5", width="5", bg="light cyan",
                             command=lambda: self.add_to_calculation("7")).grid(row=4, column=0)

        _8button = tk.Button(self.root, text="8", height="5", width="5", bg="light cyan",
                             command=lambda: self.add_to_calculation("8")).grid(row=4, column=1)

        _9button = tk.Button(self.root, text="9", height="5", width="5", bg="light cyan",
                             command=lambda: self.add_to_calculation("9")).grid(row=4, column=2)

        multiply_button = tk.Button(self.root, text="x", height="5", width="5", bg="light cyan",
                                    command=lambda: self.add_to_calculation("*")).grid(row=4, column=3)

        _0button = tk.Button(self.root, text="0", height="5", width="5", bg="light cyan",
                             command=lambda: self.add_to_calculation("0")).grid(row=5, column=0)

        clear_button = tk.Button(self.root, text="clear", height="5", width="5", bg="light cyan",
                                 command=lambda: self.clear_input_field()).grid(row=5, column=1)

        eval_button = tk.Button(self.root, text="=", height="5", width="5", bg="light cyan",
                                command=lambda: self.evaluate_calculation(self.string_user_calculation)).grid(row=5,
                                                                                                              column=2)

        divide_button = tk.Button(self.root, text="÷", height="5", width="5", bg="light cyan",
                                  command=lambda: self.add_to_calculation("/")).grid(row=5, column=3)

    def change_calculation(self, string_calculation):
        self.tk_user_calculation.set(string_calculation)

        self.string_calculation = self.tk_user_calculation.get()
        self.string_calculation = self.string_calculation.replace("*", "x")
        self.string_calculation = self.string_calculation.replace("/", "÷")

        self.tk_user_calculation.set(self.string_calculation)
        # so it uses the classical signs for multiplication and division adn not the ones python
        # requires to use the eval function

    def add_to_calculation(self, operation_num):
        self.string_user_calculation += str(operation_num)
        self.change_calculation(self.string_user_calculation)

    def clear_input_field(self):
        self.change_calculation("")
        self.string_user_calculation = ""
        # resets both display and eval expressions when cleared

    def evaluate_calculation(self, string_user_calculation):
        try:
            self.answer = eval(string_user_calculation)
            self.change_calculation(str(self.answer))
        except SyntaxError:
            # if they try to evaluate an empty string
            self.change_calculation("Cannot evaluate empty expression")
        except ZeroDivisionError:
            # if they try to divide by 0 shows err msg
            self.change_calculation("Cannot Divide by 0")


root = tk.Tk()
c = Calculator(root)
c.root.mainloop()

