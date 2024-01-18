import serial
import pygame
import tkinter as tk
from tkinter import ttk

class ControllerConverter:
    def __init__(self):
        self.ser = None
        self.joystick = None
        self.capture_active = False

    def start_capture(self, selected_port, joystick_index):
        # Connect to Arduino via serial
        self.ser = serial.Serial(selected_port, 9600)

        # Detect and initialize the selected joystick
        self.joystick = pygame.joystick.Joystick(joystick_index)
        self.joystick.init()

        # Start the main loop for reading controller input
        self.capture_active = True
        self.capture_loop()

    def stop_capture(self):
        # Stop the main loop for reading controller input
        self.capture_active = False

        # Close the serial connection
        if self.ser:
            self.ser.close()

    def capture_loop(self):
        while self.capture_active:
            pygame.event.get()

            # Read joystick axes
            axis_values = [self.joystick.get_axis(i) for i in range(self.joystick.get_numaxes())]

            # Convert and send data to Arduino
            data_to_send = ','.join(map(str, axis_values))
            self.ser.write((data_to_send + '\n').encode())

    def create_gui(self):
        root = tk.Tk()
        root.title("Control Capture")
        root.geometry("400x400")  # Set window size to 400x400 pixels

        # Create and pack widgets
        ttk.Label(root, text="Select COM Port:").pack(pady=10)

        ports = [f"COM{i+1}" for i in range(256)]
        port_combobox = ttk.Combobox(root, values=ports)
        port_combobox.pack(pady=10)
        port_combobox.set(ports[0])

        # Check if any joysticks are detected
        if pygame.joystick.get_count() > 0:
            ttk.Label(root, text="Select Joystick:").pack(pady=10)

            joysticks = [f"Joystick {i}" for i in range(pygame.joystick.get_count())]
            joystick_combobox = ttk.Combobox(root, values=joysticks)
            joystick_combobox.pack(pady=10)
            joystick_combobox.set(joysticks[0])

            start_button = ttk.Button(root, text="Start Capture", command=lambda: self.start_capture(port_combobox.get(), joystick_combobox.current()))
            start_button.pack(pady=10)

            stop_button = ttk.Button(root, text="Stop Capture", command=self.stop_capture)
            stop_button.pack(pady=10)
        else:
            ttk.Label(root, text="No joysticks detected.").pack(pady=10)

        root.mainloop()

# Initialize Pygame for controller input
pygame.init()
pygame.joystick.init()

# Create an instance of the ControllerConverter class
converter = ControllerConverter()

# Create the GUI
converter.create_gui()
