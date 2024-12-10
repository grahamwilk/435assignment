import random
import tkinter as tk
from Components.Post import Post
import requests
import Config

class ExplorePage(tk.Frame):
    def __init__(self, parent, controller, title='Explore Page'):
        super().__init__(parent)
        self.title_label = tk.Label(self, text=title, font=("Arial", 18))
        self.title_label.grid(row=0, column=1, columnspan=2, pady=10)  # Display the title
        self.controller = controller

        self.displayed_posts = []

        create_post_btn = tk.Button(self, text='Create Post', command=self.createPost)
        create_post_btn.grid()
        
        refresh_btn = tk.Button(self, text='Refresh', command=self.show_posts)
        refresh_btn.grid()

        self.response_message = tk.Label(self, text='', fg='blue')
        self.response_message.grid()
        

    def createPost(self):
        # TODO: get the user ID instead of hardcoding
        popup = tk.Toplevel(self)
        popup.title('Create Post')

        self.post_input = tk.Entry(popup)
        self.post_input.grid()

        close_button = tk.Button(popup, text="Cancel", command=popup.destroy)
        close_button.grid()

        close_button = tk.Button(popup, text="Post", command=self.save_post)
        close_button.grid()


    def save_post(self):
        # TODO: store post after being created
        url = 'http://127.0.0.1:5000/post'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + Config.access_token
        }
        body = {
            'object_id': random.randint(0, 10000000000),
            'content': self.post_input.get()
        }
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            self.response_message.config(text='Post created with object ID: ' + response.json().get('object_id'))
            print('Post created with object ID: ' + response.json().get('object_id'))
            self.show_posts()
            return True
        else:
            self.response_message.config(text='Post creation failed!')
            print(f"Post creation failed! Status code: {response.status_code}, Message: {response.text}")
            return False

    # TODO: Show saved posts
    def show_posts(self):
        for posts in self.displayed_posts:
            posts.destroy()
        self.displayed_posts.clear()


        url = 'http://127.0.0.1:5000/get'
        headers = {
            'Authorization': 'Bearer ' + Config.access_token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            rowCounter = 4
            posts = response.json()
            for post in posts:
                delete_button = tk.Button(self, text='Delete', command=lambda obj_id=post.get('object_id'): self.delete_post(obj_id))
                delete_button.grid(row=rowCounter, column=1)
                self.displayed_posts.append(delete_button)
                post = Post(self, post.get('object_id'), post.get('content'))
                post.grid(row = rowCounter, column = 0)
                self.displayed_posts.append(post)
                rowCounter += 1
            print("Posts fetched successfully")
            return True
        else:
            self.response_message.config(text='Post refresh failed!')
            print(f"Post fetch failed! Status code: {response.status_code}, Message: {response.text}")
            return False

    def delete_post(self, object_id):
        url = 'http://127.0.0.1:5000/delete'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + Config.access_token
        }
        body = {
            'object_id': object_id,
        }
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            self.response_message.config(text='Post with object ID ' + str(object_id) + ' deleted')
            print('Post with object ID ' + str(object_id) + ' deleted')
            self.show_posts()
            return True
        else:
            self.response_message.config(text='Post deletion failed!')
            print(f"Post deletion failed! Status code: {response.status_code}, Message: {response.text}")
            return False

    def show(self):
        self.tkraise()
