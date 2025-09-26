import tkinter as tk

class StarWarsScroll:
    def __init__(self, root):
        self.root = root
        self.root.title("Star Wars Scroll")
        
        # Create a Text widget
        self.text_widget = tk.Text(self.root, height=10, width=40)
        self.text_widget.pack(fill="both", expand=True)
        
        # Create a vertical Scrollbar
        self.scrollbar = tk.Scrollbar(self.root, command=self.text_widget.yview)
        self.scrollbar.pack(side="right", fill="y")
        
        # Link the Text widget to the Scrollbar
        self.text_widget.configure(yscrollcommand=self.scrollbar.set)
        
        # Add some initial text (you can replace this with your own content)
        self.add_initial_text()
        
        # Start the automatic scrolling
        self.auto_scroll()
    
    def add_initial_text(self):
        self.text_widget.insert("end", "A long time ago in a galaxy far, far away...\n")
        self.text_widget.see("end")  # Scroll to the end
    
    def auto_scroll(self):
        # Add new lines of text periodically (you can customize this interval)
        self.text_widget.insert("end", "Episode IX: The Rise of Copilot\n")
        self.text_widget.see("end")  # Scroll to the end
        self.root.after(2000, self.auto_scroll)  # Repeat every 2 seconds

if __name__ == "__main__":
    root = tk.Tk()
    app = StarWarsScroll(root)
    root.mainloop()