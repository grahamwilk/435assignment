import tkinter as tk
class Post(tk.LabelFrame):
    def __init__(self, parent, userid, content):
        super().__init__(parent)
        self.userid=userid
        self.content=content

        title = tk.Label(self, text=userid)
        title.grid(row=1, column=0)

        body = tk.Label(self, text=content)
        body.grid(row=2, column=0, sticky="nsew")

