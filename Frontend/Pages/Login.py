import tkinter as tk

class Login(tk.Frame):
    
    def __init__(self, parent, controller, title='Login'):
        super().__init__(parent)
        self.title_label = tk.Label(self, text=title, font=("Arial", 18))
        self.title_label.grid(row=0, column=1, columnspan=2, pady=10)
        self.controller = controller

        # Username label and input
        username_text = tk.Label(self, text='Username:')
        username_text.grid(row=1, column=0, sticky=tk.W, pady=2)
        
        username_input = tk.Entry(self)
        username_input.grid(row=1, column=1, pady=2)

        # Password label and input
        password_text = tk.Label(self, text='Password:')
        password_text.grid(row=2, column=0, sticky=tk.W, pady=2)
        
        password_input = tk.Entry(self)
        password_input.grid(row=2, column=1, pady=2)

        submit_button = tk.Button(self, text='Submit', command=self.submit_function)
        submit_button.grid(row=3, column=1)

    def submit_function(self):
        if(self.validate_login()):
            self.controller.show_page('Explore Page')

    # TODO: Update this to actually validate users
    def validate_login(self):
        return True

    def show(self):
        self.tkraise()

    

    