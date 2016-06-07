from pymouse import PyMouse
from time import sleep
from Tkinter import *
import tkMessageBox
import re


def main():
	auto_clicker = Application(None)
	auto_clicker.mainloop()


class Application(Tk):
	def __init__(self, parent):
		Tk.__init__(self, parent)
		self.parent = parent
		self.bg_color = "#f6f6f6"
		self.initialize_window()
		self.initialize_variables()
		self.initialize_text()
		self.initialize_labels()
		self.initialize_widgets()
		self.bind_keys_and_widgets()
		self.pack_to_window()


	def initialize_window(self):
		self.title("Autoclicker")
		self.geometry("370x265")
		self.configure(bg=self.bg_color)
	

	def initialize_variables(self):
		self.click_delay = None
		self.saved_x = False;
		self.saved_y = False
		self.mouse = PyMouse()
	

	def initialize_text(self):
		self.click_delay_txt_prev = StringVar()
		self.click_delay_txt_curr = StringVar()
		self.start_clicker_text = StringVar()
		self.cursor_pos_text = StringVar()
		self.cps_text = StringVar()
		self.click_delay_txt_curr.set("0.06")
		self.click_delay_txt_prev.set(self.click_delay_txt_curr.get())
		self.update_cps()
		self.click_delay_txt_curr.trace('w', self.update_cps)
		self.cursor_pos_text.set("\nSaved cursor position: None")	
		self.info_text = ("To get startet you have to save a cursor position,\n"
			"this is done by pressing the 'c' key.\n\n"
			"After that you have to set the click delay (seconds)\n"
			"in the box below")
		self.start_clicker_text.set("\nTo start press the 'a' key or the button."
			"\nTo stop just move your mouse.\n")


	def update_cps(self,  *dummy):
		if self.valid_input():
			self.click_delay = float(self.click_delay_txt_curr.get())
			cps = 1.0 / self.click_delay
			self.cps_text.set("Clicks per second: %.3f" % cps)
	

	def valid_input(self):
		current_delay = self.click_delay_txt_curr.get()
		prev_delay = self.click_delay_txt_prev.get()
		regex_match = re.search(r'[^\d.]', self.click_delay_txt_curr.get())

		if regex_match == None:
			try:
				test_float = float(self.click_delay_txt_curr.get())
				self.click_delay_txt_prev.set(current_delay)
				return True
			except:
				tkMessageBox.showwarning("Invalid", "Invalid decimal number, try again.")
				self.click_delay_txt_curr.set(prev_delay)
				return False
		else:
			self.click_delay_txt_curr.set(prev_delay)
			return False
	

	def initialize_labels(self):
		self.button = Button(self, text="Start Autoclicker", bg="blue", fg="white")
		self.button.configure(activebackground="#8080ff", activeforeground="white")
		self.spinbox = Spinbox(self, format="%.3f", increment=0.005, from_=0.01, to=100.0)
		self.spinbox.configure(width=10, textvariable=self.click_delay_txt_curr)


	def initialize_widgets(self):
		self.info_label = Label(self, text=self.info_text, bg=self.bg_color)
		self.cursor_pos_label = Label(self, textvariable=self.cursor_pos_text, bg=self.bg_color, foreground="red")
		self.cps_label = Label(self, textvariable=self.cps_text, bg=self.bg_color, foreground="red")
		self.start_clicker_label = Label(self, textvariable=self.start_clicker_text, bg=self.bg_color)
	

	def bind_keys_and_widgets(self):
		self.bind("c", self.set_cursor_position)
		self.bind("a", self.click_mouse)	
		self.button.bind("<Button-1>", self.click_mouse)


	def set_cursor_position(self, event):
		self.saved_x, self.saved_y = self.mouse.position() 
		self.cursor_pos_text.set("\nSaved cursor position: %dx, %dy" % (self.saved_x, self.saved_y)) 


	def click_mouse(self, event):
		if not self.saved_x  and not self.saved_y:
			tkMessageBox.showwarning("No saved cursor position", "Press the 'c' key when you have your cursor over the desired position.")
			return

		if self.click_delay == 0.0:
			tkMessageBox.showwarning("No delay", "The click delay needs to be greater than 0.")
			return 

		self.mouse.move(self.saved_x, self.saved_y)
		current_x, current_y = self.saved_x, self.saved_y

		while current_x == self.saved_x and current_y == self.saved_y:
		    self.mouse.click(self.saved_x, self.saved_y, 1)
		    sleep(self.click_delay)
		    current_x, current_y = self.mouse .position()

		print "finished, moved mouse"


	def pack_to_window(self):
		self.info_label.pack()
		self.spinbox.pack()
		self.cursor_pos_label.pack()
		self.cps_label.pack()
		self.start_clicker_label.pack()
		self.button.pack()
		self.resizable(False, False)


if __name__ == '__main__':
	main()