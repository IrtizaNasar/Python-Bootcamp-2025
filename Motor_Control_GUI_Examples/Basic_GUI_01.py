# Importing Custom Tkinter
import customtkinter
import time
from servos.XL330 import XL330Comm, XL330Ctrl


# Starting communication for Dynamixel servo
serial = XL330Comm(port="ADD YOUR PORT")

# Declaring a servo object
servo1 = XL330Ctrl(servo_id=ADD YOUR MOTOR ID)

# Adding servo to start communication
serial.add_servo(servo=servo1)

# Enabling torque for a single servo
servo1.torque_enabled(is_enabled=True)

servo1.set_position(0)




# Sets dark mode - Indicates that a dark theme be used for UI elements
customtkinter.set_appearance_mode('dark') 



# creates a new instance of the CTk class from the customtkinter library 
# and assigns it to the variable root. This instance represents the main window 
root = customtkinter.CTk()

# This line sets the min size of the window. This means that the user won't
# be able to resize the window below this minimum size.
root.minsize(400,400)

# This sets the title of the root window. The title is displayed in the title
# bar of the window
root.title("Controller GUI")

#Creates a new instance of a CTk Label and sets it as the main heading
header_label = customtkinter.CTkLabel(master = root, text= "GUI Demo", font=(None,24))

# The .pack() method automatically positions and sizes the header based on the available space in the container.
header_label.pack(pady=20)

#Create a function which can be called everytime the slider value updates
def demo(pos):
    print(pos)
    servo1.set_position(pos)



# 1. Adding A Slider

# master=root allows us to specify where we want the slider added. In this case to the GUI root.
# from_ and to arguments allows us to specify the min and max range for the slider.
# with number_of_steps you can determine the values that you can select with the slider. In this insatnce 99 allows us to get whole numbers.
# command= allows us to connect a function to be called. In this case the function is called when the values of a slider change.
pos_slider = customtkinter.CTkSlider(master=root, from_=0, to=350, 
                                        number_of_steps=350,
                                        command=demo) 

# The set methods allows us to give the slider an initial value.
pos_slider.set(0)

# .pack displays the pos_slider widget within its parent container(root in this instance). 
#  The .pack() method automatically positions and sizes the widget based on the available space in the container.
pos_slider.pack()




# .mainloop() is a method used to start the main event loop of a tkinter-based graphical 
#  user interface (GUI) application. Once .mainloop() is called, it initiates an infinite 
# loop that continuously waits for user interactions, such as mouse clicks or keyboard inputs, 
# and responds to those events by invoking the appropriate event handlers or callbacks associated 
# with the GUI elements in the application. The main event loop ensures that the GUI remain
root.mainloop()