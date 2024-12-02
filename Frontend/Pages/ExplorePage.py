import tkinter as tk
from Components.Post import Post

class ExplorePage(tk.Frame):
    def __init__(self, parent, controller, title='Explore Page'):
        super().__init__(parent)
        self.title_label = tk.Label(self, text=title, font=("Arial", 18))
        self.title_label.grid(row=0, column=1, columnspan=2, pady=10)  # Display the title
        self.controller = controller

        self.show_posts()

        create_post_btn = tk.Button(self, text='Create Post', command=self.createPost)
        create_post_btn.grid()

    def createPost(self):
        # TODO: get the user ID instead of hardcoding
        popup = tk.Toplevel(self)
        popup.title('Create Post')

        post_input = tk.Entry(popup)
        post_input.grid()

        close_button = tk.Button(popup, text="Cancel", command=popup.destroy)
        close_button.grid()

        close_button = tk.Button(popup, text="Post", command=self.save_post)
        close_button.grid()

    def save_post(self):
        # TODO: store post after being created
        pass

    # TODO: Show saved posts
    def show_posts(self):
        post1=Post(self, 'user1', 'content1')
        post2=Post(self, 'user2', 'content2')
        post3=Post(self, 'user3', 'content3')
        post4=Post(self, 'user4', 'content4')
        post1.grid(row=1)
        post2.grid(row=2)
        post3.grid(row=3)
        post4.grid(row=4)

    def show(self):
        self.tkraise()
