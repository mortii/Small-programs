import win32api, win32con
import time
import Tkinter as tk
import tkMessageBox


saved_x, saved_y = 0, 0
speed = 0.05 # in seconds


def click(event):
	"""
	sets the cursor to where you want (this is done with setCur previously),
	then keeps clicking until the mouse is moved.
	"""
	global speed

	eget = e.get()
	print eget

	speed = float(eget)

	if saved_x == 0 and saved_y == 0:
		tkMessageBox.showwarning("No saved mouse position", "Press 'c' when you have your mouse pointer over the desired position.")
		return

	win32api.SetCursorPos((saved_x, saved_y))
	x, y = saved_x, saved_y

	while x == saved_x and y == saved_y:
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	    time.sleep(speed)
	    print x, y
	    x, y = updateCur()


def click_button():
	click("")


def setCur(event):
	global saved_x, saved_y
	saved_x, saved_y = win32api.GetCursorPos()
	tkMessageBox.showinfo("Cursor position", "Position saved, x: %s, y: %s" % (saved_x, saved_y))


def updateCur():
	x, y = win32api.GetCursorPos()
	return x, y


my_gui = tk.Tk()

my_gui.title("Autoclicker")
my_gui.geometry("350x200")

my_gui.bind("a", click)
my_gui.bind("c", setCur)

tk.Label(my_gui, text="Press  'c' to save mouse position.").pack()
tk.Label(my_gui, text="Choose autoclick speed, click every").pack()

e = tk.Spinbox(my_gui, format="%.2f", increment=0.01, from_=0.01, to=100.0)
e.pack()

tk.Label(my_gui, text="seconds.").pack()
tk.Label(my_gui, text="Press 'a' afterwards to autoclick at the saved position").pack()
tk.Label(my_gui, text="or press the 'Start Autoclick' button.").pack()
tk.Label(my_gui, text="Move your mouse to stop.").pack()

tk.Button(my_gui, text="Start Autoclick", command=click_button).pack()

my_gui.mainloop()