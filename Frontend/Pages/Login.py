import tkinter as tk
import requests
import Config

class Login(tk.Frame):
    
    def __init__(self, parent, controller, title='Login'):
        super().__init__(parent)
        self.title_label = tk.Label(self, text=title, font=("Arial", 18))
        self.title_label.grid(row=0, column=1, columnspan=2, pady=10)
        self.controller = controller

        # Username label and input
        username_text = tk.Label(self, text='Username:')
        username_text.grid(row=1, column=0, sticky=tk.W, pady=2)
        
        self.username_input = tk.Entry(self)
        self.username_input.grid(row=1, column=1, pady=2)

        # Password label and input
        password_text = tk.Label(self, text='Password:')
        password_text.grid(row=2, column=0, sticky=tk.W, pady=2)
        
        self.password_input = tk.Entry(self)
        self.password_input.grid(row=2, column=1, pady=2)

        submit_button = tk.Button(self, text='Submit', command=self.submit_function)
        submit_button.grid(row=3, column=1)
        
        self.error_label = tk.Label(self, text='', fg='red')
        self.error_label.grid(row=4, column=1)

    def submit_function(self):
        if(self.validate_login()):
            self.controller.show_page('Explore Page')
            self.controller.pages['Explore Page'].show_posts()

    def validate_login(self):
        url = 'http://127.0.0.1:5000/login'
        headers = {'Content-Type': 'application/json'}
        body = {
            'username': self.username_input.get(),
            'password': self.password_input.get()
        }
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            Config.access_token = response.json()
            print(f"Login successful! Access token: {Config.access_token}")
            return True
        else:
            print(f"Login failed! Status code: {response.status_code}, Message: {response.json().get('msg')}")
            self.error_label.config(text='Invalid username or password')
            return False

    def show(self):
        self.tkraise()

    

    