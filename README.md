# Control-Capture
My project for turning XBOX or any Gamepad input into PPM
# Project Overview

This project aims to create a system that allows you to control a device, such as a drone or a model vehicle, using a joystick connected to your computer. The control commands from the joystick are transmitted to an Arduino, which then converts them into a PPM (Pulse Position Modulation) signal. This PPM signal is commonly used to control radio-controlled devices, like those using the TBS Crossfire system.

Components:

1. Python Script:
Purpose: The Python script captures input from a connected joystick (like those used for gaming) and sends this input data to the Arduino via a USB connection.
How it works: It continuously reads the joystick's axes values, formats them, and sends the data as a string to the Arduino over a serial connection.

2. Arduino Code:
Purpose: The Arduino code receives the joystick data from the Python script, processes it, and generates a PPM signal that is compatible with devices like the TBS Crossfire.
How it works: It reads the joystick data, maps it to PPM values, and generates a PPM signal on a specific pin (pin 9). This PPM signal can be used to control devices that accept PPM input.
# How To Use
Usage:

1. Connect Joystick: Connect a compatible joystick to your computer. (If you would like to use a Logitech Wheel or to remap functions, go to https://github.com/x360ce/x360ce)

2. Install Python from: https://www.python.org/downloads/ and then run install libraries file

3. Connect the Arduino to your computer via USB.
Upload the Arduino code to the board using the Arduino IDE.
The Arduino will receive the joystick data and convert it into a PPM signal.

4. Connect to Device:
Connect the PPM output pin (pin 9) from the Arduino to the PPM input on your drone, model vehicle, or other devices.

5. To discover what COM port your device is on, please run the [COM SCANNER](#COM-SCANNER)

6. Run [ControlCapture v1](#ControlCapture-V1)
Execute the Python script on your computer. It will detect the connected joystick, capture its movements, and send the data to the Arduino.

7. Control Device:
The joystick movements are translated into PPM signals, allowing you to control your device by manipulating the joystick.

Notes:
Ensure that the baud rate in both the Python script and Arduino code matches.
Adjustments to the mapping and configuration might be needed based on your specific joystick and device requirements.
This system enables you to control your device remotely using a joystick and facilitates integration with devices compatible with PPM input.
# About Me
Hi there! 👋 I'm a 13-year-old tech and drone enthusiast known as skunkfpv. I embarked on a cool project because I wanted to drive an RC car using my Logitech G920 steering wheel. When I couldn't find existing software to make this happen, I decided to take matters into my own hands and develop my own solution.

[skunkfpv's Linktree](https://linktr.ee/skunkfpv)

🛠️ Tech Enthusiast | Drone Pilot | DIY Developer 🚀
