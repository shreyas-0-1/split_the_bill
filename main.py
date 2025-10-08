import tkinter as tk
from tkinter import messagebox
import numpy as np

'''
    Version 1 complete
    - Tip handling to be added
    - Scrollbards to be added
'''

class BillSplitter:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.title("Bill Split Calculator")
        self.root.geometry("750x1000+500+50")

        # Variables
        self.grp_num = 0
        self.payers = 0
        self.payment_questions = []
        self.payment_answers = []
        self.ind_payments = []

        # User Interface
        self.title = tk.Label(self.root, text="Bill Splitting Calculator", font=('Georgia', 37))
        self.title.pack(pady=(35, 40))

        self.grp_num_question = tk.Label(self.root, text='How many people are in your group?', font=('Georgia', 20))
        self.grp_num_question.pack(pady=(0, 10))

        self.grp_num_answer = tk.Entry(self.root, justify='center', font=('Georgia', 20))
        self.grp_num_answer.pack(pady=(0, 20))

        self.payers_question = tk.Label(self.root, text='How many people paid for the bill?', font=('Georgia', 20))
        self.payers_question.pack(pady=(0, 10))

        self.payers_answer = tk.Entry(self.root, justify='center', font=('Georgia', 20))
        self.payers_answer.pack(pady=(0, 20))
        self.payers_answer.bind()

        self.button1 = tk.Button(self.root, text="Enter", command=self.get_inputs, font=('Georgia', 20))
        self.button1.pack(pady=(0, 30))

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.button2 = tk.Button(self.root, text='Enter', command=self.split, font=('Georgia', 20))

        self.output = None

    def get_inputs(self):
        '''
            Used to retrieve how many members are in the group and how many are paying.
            Complete with error handling.
        '''
        try:
            self.grp_num = int(self.grp_num_answer.get())
            self.payers = int(self.payers_answer.get())

            if self.grp_num < self.payers:
                messagebox.showwarning("Warning", "Number of people paying cannot be greater than group count.")
            else:
                for i in range(self.payers):
                    label = tk.Label(self.frame, text=f"Person {i+1} paid $", font=('Georgia', 20))
                    answer = tk.Entry(self.frame, justify='left', font=('Georgia', 20))
                    label.grid(row=i, column=0, padx=0, pady=(0, 10))
                    answer.grid(row=i, column=1, padx=0, pady=(0, 10))
                    self.payment_questions.append(label)
                    self.payment_answers.append(answer)
                
                self.grp_num_answer.config(state=tk.DISABLED)
                self.payers_answer.config(state=tk.DISABLED)
                self.button1.config(state=tk.DISABLED)

                self.button2.pack(pady=(10, 30))

        except ValueError:
            messagebox.showwarning("Warning", "Please enter numbers.")

    def split(self):
        '''
            Executes the check splitting logic.
            Complete with error handling.
        '''
        try:
            self.ind_payments = [float(x.get()) for x in self.payment_answers]
            total = np.sum(self.ind_payments)
            per_person = total/self.grp_num

            output = f"The total amount to be paid is ${total:.2f}.\n\n"
            
            if self.grp_num - self.payers != 0:
                if self.grp_num - self.payers == 1:
                    output += f"The 1 person who did not pay will give ${per_person:.2f} to the {self.payers} who paid.\n\n"
                else:
                    output += f"Each of the {self.grp_num - self.payers} people who did not pay will give ${per_person:.2f} to the {self.payers} who paid.\n\n"
                    
                output += f"Out of this sum of ${per_person * (self.grp_num - self.payers):.2f}:\n\n"
            
            still_owe = ''
            for i in range(self.payers):
                owed = self.ind_payments[i] - per_person
                
                if owed >= 0:
                   output += f"Person {i+1} gets ${owed:.2f}\n"
                else:
                    still_owe += f"Person {i+1} pays ${-1 * owed:.2f} to anyone who is still to receive money\n"

            output += still_owe

            self.output = tk.Label(self.root, text=output, font=('Georgia', 20), )
            self.output.pack(pady=(0, 10))

            self.button2.config(state=tk.DISABLED)
            for i in range(self.payers):
                self.payment_answers[i].config(state=tk.DISABLED)

        except ValueError:
            messagebox.showwarning("Warning", "Please enter numbers.")

# Start the app
if __name__ == '__main__':
    root = tk.Tk()
    bill_splitter = BillSplitter(root)
    root.mainloop()