from tkinter import *

class Window(Frame):
	def __init__(self, transparentcolor="red", width=90, height=50, **kwargs):
		self.transparentcolor = transparentcolor
		self.window = Tk()
		self.window.wm_attributes("-transparentcolor", self.transparentcolor)
		self.window.wm_attributes("-fullscreen", 1)
		self.windowFrame = Frame(self.window, bg=self.transparentcolor)
		self.windowFrame.pack(fill=BOTH, expand=1)

		self.title = "Window"
		self.width = width
		self.height = height

		super().__init__(self.windowFrame, width=self.width, height=self.height, **kwargs)
		
		self.surface = Frame(self)
		self.grip = Label(self, text=self.title, width=self['width'], bg="grey")

		self.place(x=0, y=0)

	def build(self):
		pass

	def loadTopBtns(self):
		self.extButton = Button(self, text="X", bd=200000000000000000000000000000000000000000000000000000, bg=self.grip['bg'], command=self.destroy)
		self.maxButton = Button(self, text="|_|", bd=200000000000000000000000000000000000000000000000000000, bg=self.grip['bg'])
		self.minButton = Button(self, text="-", bd=200000000000000000000000000000000000000000000000000000, bg=self.grip['bg'], command=self.window.iconify)

		self.minButton.place(relx=1, x=0, y=-1, anchor=NE)
		self.maxButton.place(relx=1, x=100, y=-1, anchor=SE)
		self.extButton.place(relx=1, x=200, y=-1, anchor=SE)

	def packGrip(self):
		self.grip.pack(side=TOP, fill=X, expand=1)

	def unbindMovement(self):
		self.grip.unbind("<Button-1>")
		self.grip.unbind("<B1-Motion>")

	def bindMovement(self):
		self.grip.bind("<Button-1>", self.onclick)
		self.grip.bind("<B1-Motion>", self.onmove)

	def maximize(self):
		self.maximizeBtn.config(command=self.un_maximize)
		self.pack(fill=BOTH, expand=1)
		self.unbindMovement()
		self.packGrip()

	def un_maximize(self):
		self.config(width=self.width, height=self.height)
		self.pack()
		self.packGrip()
		self.bindMovement()
		self.maximizeBtn.config(command=self.maximize)

	def destroy(self):
		super().destroy()
		self.window.destroy()

	def onclick(self, event):
		self._drag_start_x = event.x
		self._drag_start_y = event.y

	def onmove(self, event):
		self.x = self.winfo_x() - self._drag_start_x + event.x
		self.y = self.winfo_y() - self._drag_start_y + event.y
		self.place(x=self.x, y=self.y)

	def run(self, n=0):
		self.build()
		
		self.packGrip()
		self.loadTopBtns()
		self.surface.pack()
		self.bindMovement()
		
		self.window.mainloop(n)