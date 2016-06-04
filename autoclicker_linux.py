from pymouse import PyMouse
import time
from Tkinter import *
import tkMessageBox

my_mouse = PyMouse()
saved_x, saved_y = 0, 0
widget = None

def click_mouse(event):
	# click_speed = widget.get()
	# click_speed = float(click_speed)
	# print click_speed

	if saved_x == 0 and saved_y == 0:
		tkMessageBox.showwarning("No saved mouse position", "Press 'c' when you have your mouse pointer over the desired position.")
		return

	my_mouse.move(saved_x, saved_y)
	current_x, current_y = saved_x, saved_y

	print "saved:", saved_x, saved_y

	while current_x == saved_x and current_y == saved_y:
	    my_mouse.click(saved_x, saved_y, 1)
	    time.sleep(0.06)
	    print current_x, current_y
	    current_x, current_y = my_mouse .position()

	print "done"


def set_cursor_position(event):
	global saved_x, saved_y
	saved_x, saved_y = my_mouse .position() 
	tkMessageBox.showwarning("Position", "x:%d, y:%d" % (saved_x, saved_y))

def click_button():
	if saved_x == 0 and saved_y == 0:
		tkMessageBox.showwarning("No saved mouse position", "Press 'c' when you have your mouse pointer over the desired position.")
		return

	my_mouse.move(saved_x, saved_y)
	current_x, current_y = saved_x, saved_y

	print "saved:", saved_x, saved_y

	while current_x == saved_x and current_y == saved_y:
	    my_mouse.click(saved_x, saved_y, 1)
	    time.sleep(0.06)
	    print current_x, current_y
	    current_x, current_y = my_mouse .position()

	print "done"

def main():
	global widget

	my_gui = Tk()
	my_gui.title("Autoclicker")
	widget = Spinbox(my_gui, format="%.2f", increment=0.01, from_=0.01, to=100.0).pack()
	my_gui.geometry("350x200")
	Label(my_gui, text="Press  'c' to save mouse position.").pack()
	Label(my_gui, text="Choose autoclick click_speed, click every").pack()
	Label(my_gui, text="seconds.").pack()
	Label(my_gui, text="Press 'a' afterwards to autoclick at the saved position").pack()
	Label(my_gui, text="or press the 'Start Autoclick' button.").pack()
	Label(my_gui, text="Move your mouse to stop.").pack()
	my_gui.bind("a", click_mouse)
	my_gui.bind("c", set_cursor_position)
	Button(my_gui, text="Start Autoclick", command=click_button).pack()

	my_gui.mainloop()


if __name__ == '__main__':
	main()