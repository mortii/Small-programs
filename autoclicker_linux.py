from pymouse import PyMouse
from time import sleep
from Tkinter import *
import tkMessageBox


def main():
	app = application(None)
	app.mainloop()


class application(Tk):
	def __init__(self, parent):
		Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()


	def initialize(self):
		self.title("Autoclicker")
		self.geometry("370x250")
		self.click_speed = None
		self.saved_x = False;
		self.saved_y = False
		
		self.mouse = PyMouse()
		button = Button(self, text="Start Autoclick")


		self.spinVar = StringVar()
		self.widget = Spinbox(self, format="%.2f", increment=0.01, from_=0.06, to=100.0, 
						width=10, textvariable=self.spinVar)



		self.spinVar.trace('w', self.update_cps)
		
		button.bind("<Button-1>", self.click_mouse)
		self.bind("a", self.click_mouse)	
		self.bind("c", self.set_cursor_position)
		infoText = ("To get startet you have to save a cursor position,\n"
			"this is done by pressing the 'c' key.\n\n"
			"After that you have to set the click delay (seconds)\n"
			" in the box below")
		infoLabel = Label(self, text=infoText)

		self.cursor_pos_text = StringVar()
		self.cursor_pos_text.set("\nSaved cursor position: None")	
		cursor_pos_label = Label(self, textvariable=self.cursor_pos_text)

		self.cps_text = StringVar()
		self.update_cps()
		cps_label = Label(self, textvariable=self.cps_text)

		self.start_text = StringVar()
		self.start_text.set("\nTo start press the 'a' key or the button.\nTo stop just move your mouse.")
		start_label = Label(self, textvariable=self.start_text)


		infoLabel.pack()
		self.widget.pack()
		cursor_pos_label.pack()
		cps_label.pack()
		start_label.pack()
		button.pack()
		self.resizable(False, False)
	

	def update_cps(*args):
		self = args[0]
		self.click_speed = float(self.spinVar.get())
		cps = 1.0 / self.click_speed
		self.cps_text.set("Clicks per second: %.3f" % cps)


	def set_cursor_position(self, event):
		self.saved_x, self.saved_y = self.mouse .position() 
		self.cursor_pos_text.set("\nSaved cursor position: %dx, %dy" % (self.saved_x, self.saved_y)) 
	

	def click_mouse(self, event):
		if not self.saved_x  and not self.saved_y:
			tkMessageBox.showwarning("No saved cursor position", "Press the 'c' key when you have your cursor over the desired position.")
			return

		self.mouse.move(self.saved_x, self.saved_y)
		current_x, current_y = self.saved_x, self.saved_y

		while current_x == self.saved_x and current_y == self.saved_y:
		    self.mouse.click(self.saved_x, self.saved_y, 1)
		    sleep(self.click_speed)
		    current_x, current_y = self.mouse .position()

		print "done, moved mouse"


if __name__ == '__main__':
	main()