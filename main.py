import tkinter as tk
from tkinter import messagebox
import numpy as np

class BillSplitter:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.title("Bill Split Calculator")
        self.root.geometry("750x1500+500+500")

        self.grp_num = 0
        self.payers = 0
        self.payment_questions = []
        self.payment_answers = []
        self.ind_payments = []

        self.grp_num_question = tk.Label(self.root, text='How many people are in your group?')
        self.grp_num_question.pack(pady=20)

        self.grp_num_answer = tk.Entry(self.root, justify='center')
        self.grp_num_answer.pack(pady=0)

        self.payers_question = tk.Label(self.root, text='How many people paid for the bill?')
        self.payers_question.pack(pady=20)

        self.payers_answer = tk.Entry(self.root, justify='center')
        self.payers_answer.pack(pady=0)
        self.payers_answer.bind()

        self.button1 = tk.Button(self.root, text="Submit", command=self.get_inputs_1)
        self.button1.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.button2 = tk.Button(self.root, text='Submit', command=self.get_inputs_2)
        self.button2.pack(pady=10)

    def get_inputs_1(self):
        try:
            self.grp_num = int(self.grp_num_answer.get())
            self.payers = int(self.payers_answer.get())

            for i in range(self.payers):
                label = tk.Label(self.frame, text=f"Person {i+1} paid $")
                answer = tk.Entry(self.frame, justify='left')
                label.grid(row=i, column=0, padx=0, pady=5)
                answer.grid(row=i, column=1, padx=0, pady=5)
                self.payment_questions.append(label)
                self.payment_answers.append(answer)
            
            self.grp_num_answer.config(state=tk.DISABLED)
            self.payers_answer.config(state=tk.DISABLED)
            self.button1.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showwarning("Warning", "Please enter numbers.")

if __name__ == '__main__':
    root = tk.Tk()
    bill_splitter = BillSplitter(root)
    root.mainloop()