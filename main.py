import tkinter as tk
from tkinter import ttk
from tkinterweb import HtmlFrame
import urllib.request

class SimpleWebBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Web Browser")

        # Create the toolbar frame
        toolbar = ttk.Frame(root)
        toolbar.pack(side="top", fill="x")

        # Back button
        self.back_button = ttk.Button(toolbar, text="Back", command=self.go_back)
        self.back_button.pack(side="left")

        # Forward button
        self.forward_button = ttk.Button(toolbar, text="Forward", command=self.go_forward)
        self.forward_button.pack(side="left")

        # URL entry
        self.url_entry = ttk.Entry(toolbar, width=50)
        self.url_entry.pack(side="left", fill="x", expand=True)

        # Go button
        self.go_button = ttk.Button(toolbar, text="Go", command=self.load_url)
        self.go_button.pack(side="left")
        
        # Initialize history (for back/forward functionality)
        self.history = []
        self.current_index = -1

        # Create an HtmlFrame to display the web page
        self.frame = HtmlFrame(root)
        self.frame.pack(fill="both", expand=True)

    def load_url(self):
        url = self.url_entry.get()
        self.load_website(url)

    def load_website(self, url):
        try:
            # Check if the URL is reachable
            response = urllib.request.urlopen(url)
            if response.status == 200:
                # Load the website if reachable
                self.frame.load_website(url)
                self.add_to_history(url)
            else:
                raise Exception("Website not found")
        except Exception as e:
            # Display custom "Website Not Found" message using load_html
            self.frame.load_html("<h1>Website Not Found</h1><p>The website you tried to access does not exist or is not reachable.</p>")

    def add_to_history(self, url):
        # Add the URL to history and update the current index
        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index += 1

    def go_back(self):
        if self.current_index > 0:
            self.current_index -= 1
            url = self.history[self.current_index]
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url)
            self.frame.load_website(url)

    def go_forward(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            url = self.history[self.current_index]
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url)
            self.frame.load_website(url)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    browser = SimpleWebBrowser(root)
    root.mainloop()
