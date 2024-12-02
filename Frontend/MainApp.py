import tkinter as tk
from Pages.Login import Login
from Pages.ExplorePage import ExplorePage

# RUN THIS FILE TO START THE APPLICATION

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Forum')
        self.geometry('400x300')

        self.container = tk.Frame(self)
        self.container.grid()

        # Pages
        self.pages = {}
        self.add_page('Login', Login)
        self.add_page('Explore Page', ExplorePage)

        # Show initial page
        self.show_page('Login')

    def add_page(self, name, page_class):
        page = page_class(self.container, self, title=name)
        page.grid(row=0, column=0, sticky='nsew')
        self.pages[name] = page

    # Call this to show a new page
    def show_page(self, name):
        page = self.pages.get(name)
        if page:
            page.show()

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
