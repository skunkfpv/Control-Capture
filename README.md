# Project Overview

This project aims to create a system that allows you to control a device, such as a drone or a model vehicle, using a joystick connected to your computer. The control commands from the joystick are transmitted to an Arduino, which then converts them into an NRF24L01 signal.

## Components

### 1. Python Script

- **Purpose:** The Python script captures input from a connected joystick (like those used for gaming) and sends this input data to the Arduino via a USB connection.
- **How it works:** It continuously reads the joystick's axes values, formats them, and sends the data as a string to the Arduino over a serial connection.

### 2. Arduino Code

- **Purpose:** The Arduino code receives the joystick data from the Python script, processes it, and sends signals to the NRF24L01 for controlling the vehicle.
- **How it works:** It reads the joystick data and maps it to NRF24L01 values.

# How To Help

If you would like to support this and many other of my projects, here is the PayPal donation link.

[PayPal Donation Link](https://www.paypal.com/donate/?hosted_button_id=5FPENFPCJKS3Q)

# PCB
I am developing a PCB. To purchase one, send an email to skunkfpv@yahoo.com
![image](https://github.com/skunkfpv/Control-Capture/assets/148094195/89c407be-d423-4e60-a4ec-089a5cd624a8)
![image](https://github.com/skunkfpv/Control-Capture/assets/148094195/adc73fa6-d152-405e-8567-86a32c9c9ad7)


# How To Use

## Installation Video

[Watch Installation Video](https://youtu.be/Rfy2kiX_o94)

### Usage

1. **Connect Joystick:** Connect a compatible joystick to your computer. (For Logitech Wheel or remapping functions, visit [x360ce GitHub](https://github.com/x360ce/x360ce))

2. **Install Python:**
   - Download and install Python from [python.org](https://www.python.org/downloads/)
   - Run the "install_libraries" file.

3. **Connect the Arduino:**
   - Connect the Arduino to your computer via USB.
   - Upload the Arduino code to the board using the Arduino IDE.
   - The Arduino will receive the joystick data and convert it into an NRF24L01 signal.

4. **Connect to Device:**
   - Connect the NRF24L01 to your Arduino and your vehicle.

5. **Discover COM Port:**
   - Run the [COM SCANNER](https://github.com/skunkfpv/Control-Capture/blob/main/COM%20SCANNER.py) to find the COM port your device is on.

6. **Run ControlCapture Script:**
   - Execute the Python script [ControlCapture V1](https://github.com/skunkfpv/Control-Capture/blob/main/ControlCapture%20V1.py)
   - It will detect the connected joystick, capture its movements, and send the data to the Arduino.

7. **Control Device:**
   - The joystick movements are translated into NRF24L01 signals, allowing you to control your device by manipulating the joystick.

**Notes:**
- Ensure that the baud rate in both the Python script and Arduino code matches.
- Adjustments to the mapping and configuration might be needed based on your specific joystick and device requirements.
- This system enables you to control your device remotely using a joystick and facilitates integration with devices compatible with NRF24L01 input.

# About Me

Hi there! 👋 I'm a 13-year-old tech and drone enthusiast known as skunkfpv. I embarked on a cool project because I wanted to drive an RC car using my Logitech G920 steering wheel. When I couldn't find existing software to make this happen, I decided to take matters into my own hands and develop my own solution.

[skunkfpv's Linktree](https://linktr.ee/skunkfpv)

🛠️ Tech Enthusiast | Drone Pilot | DIY Developer 🚀
