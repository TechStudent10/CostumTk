from UI import Window
from tkinter import *

class MainWindow(Window):
	def build(self):
		Label(self.surface, text="Hello, World!").pack()

if __name__ == "__main__":
	MainWindow(width=70).run()