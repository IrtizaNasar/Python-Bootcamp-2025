# Importing Custom Tkinter
import customtkinter
import time
import serial
from serial.tools import list_ports
from servos.XL330 import XL330Comm, XL330Ctrl

# Sets dark mode - Indicates that a dark theme be used for UI elements
customtkinter.set_appearance_mode('dark') 



# creates a new instance of the CTk class from the customtkinter library 
# and assigns it to the variable window. This instance represents the main window 
window = customtkinter.CTk()

# This line sets the min size of the window. This means that the user won't
# be able to resize the window below this minimum size.
window.minsize(300,500)

# This sets the title of the root window. The title is displayed in the title
# bar of the window
window.title("Simple Servo Control")

#Creates a new instance of a CTk Label and sets it as the main heading within the GUI
header_label = customtkinter.CTkLabel(master = window, text= "Servo Recorder", font=(None,24))

# The .pack() method automatically positions and sizes the header based on the available space in the container.
header_label.pack(pady=20)


# Create an empty list to store our saved positions
saved_positions = []

# Variables for servo connection
serial_connection = None
servo = None


# Functions that do things when associated buttons are pressed 

def connect_to_port():
    # The 'global' keyword declares that these variables will be accessible outside this function in the global scope.
    global serial_connection, servo
    
    try:
        # Connect to the servo
        serial_connection = XL330Comm(port="ADD YOUR PORT")
        servo = XL330Ctrl(servo_id=ADD YOUR MOTOR ID)
        serial_connection.add_servo(servo=servo)
        
        # Make the motor free to move
        servo.torque_enabled(is_enabled=False)
        
        # Enable all the control buttons
        # move_button.configure(state="normal")
        save_button.configure(state="normal")
        play_button.configure(state="normal")
        status_label.configure(text="Connected")
        
        
        # Start updating position
        update_position()
        
    except Exception as e:
        status_label.configure(text="Connection Failed!")
        print(f"Error: {e}")

def save_current_position():
    if not servo:
        print("Please connect to a servo first!")
        return
        
    position = servo.get_position()
    saved_positions.append(position)
    positions_label.configure(text=f"Saved Positions: {len(saved_positions)}")
    print(f"Saved position: {position}")


def play_positions():
    if not servo or len(saved_positions) == 0:
        print("No positions saved yet!")
        return
    
    # Disable all buttons while playing
    save_button.configure(state="disabled")
    play_button.configure(state="disabled")
    
    # Enable the motor so it can move
    servo.torque_enabled(is_enabled=True)
    
    # Go through each saved position
    for position in saved_positions:
        print(f"Moving to position: {position}")
        servo.set_position(position)
        time.sleep(0.3)
    
    # Free the motor again
    servo.torque_enabled(is_enabled=False)
    
    # Re-enable all buttons
    save_button.configure(state="normal")
    play_button.configure(state="normal")

# Function to update the position display
def update_position():
    if servo:
        try:
            current_pos = servo.get_position()
            current_position_label.configure(text=f"Current Position: {current_pos}")
        except:
            current_position_label.configure(text="Current Position: Error")
    
    # 100: delay in milliseconds (0.1 seconds)
    # update_position: callback function to execute
    window.after(100, update_position)




# DRAWING GUI BUTTONS AND LABELS

# Status label
status_label = customtkinter.CTkLabel(
    master=window,
    text="Status: Not Connected"
)
status_label.pack(pady=10)

# # Connect ports button
connect = customtkinter.CTkButton(
    master=window,
    text="Connect to Port",
    command= connect_to_port
)
connect.pack(pady=10)


# Button to save positions (starts disabled)
save_button = customtkinter.CTkButton(
    master=window,
    text="Save Position",
    command=save_current_position,
    state="disabled"
)
save_button.pack(pady=50)

# Button to play back saved positions (starts disabled)
play_button = customtkinter.CTkButton(
    master=window,
    text="Play Saved Positions",
    command=play_positions,
    state="disabled"
)
play_button.pack(pady=10)

# Label to show current position
current_position_label = customtkinter.CTkLabel(
    master=window,
    text="Current Position: Not Connected"
)
current_position_label.pack(pady=20)

# Label to show number of saved positions
positions_label = customtkinter.CTkLabel(
    master=window,
    text="Saved Positions: 0"
)
positions_label.pack(pady=20)

# Pady extra space added above and below the text, default is 1

# .pack displays the pos_slider widget within its parent container(root in this instance). 
#  The .pack() method automatically positions and sizes the widget based on the available space in the container.





# .mainloop() is a method used to start the main event loop of a tkinter-based graphical 
#  user interface (GUI) application. Once .mainloop() is called, it initiates an infinite 
# loop that continuously waits for user interactions, such as mouse clicks or keyboard inputs, 
# and responds to those events by invoking the appropriate event handlers or callbacks associated 
# with the GUI elements in the application. The main event loop ensures that the GUI remain
window.mainloop()