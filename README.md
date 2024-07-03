# Keylogger
This repository contains a basic keylogger program written in Python. The keylogger records and logs keystrokes and saves them to a file.

## Prerequisites
Ensure you have Python installed on your system. This script requires the pynput library. You can install it using pip:

`pip install pynput`

## Usage
### 1. Clone the Repository
  `git clone https://github.com/dhar-un-raj/keylogger-example.git`
  
  `cd keylogger`

### 2. Run the Keylogger
 `python keylogger.py`

### 3. Stopping the Keylogger

Press the `ESC` key to stop the keylogger.

## Code Explanation
## Importing the `pynput` Library
The code begins by importing the keyboard module from the pynput library, which allows us to control and monitor input devices.

## Defining the Log File
A variable log_file is defined to specify the name of the file where the key logs will be saved (keylog.txt).

## Writing Keystrokes to the File
A function write_to_file(key) is defined to handle the logging of keystrokes. This function opens the log file in append mode and writes the character of the key pressed. Special keys like space, enter, and others are handled separately to ensure readability.

## Handling Key Press Events
A function on_press(key) is defined to handle what happens when a key is pressed. This function calls write_to_file(key) to log the key.

## Handling Key Release Events
A function on_release(key) is defined to handle what happens when a key is released. This function stops the listener if the ESC key is released, effectively stopping the keylogger.

## Setting Up the Listener
The keyboard.Listener is set up to monitor for key press and release events. The listener calls on_press when a key is pressed and on_release when a key is released. The listener.join() method starts the listener and keeps it running.

## Ethical Considerations
Creating and using a keylogger has serious ethical and legal implications. Please adhere to the following guidelines:

- Permissions: Obtain explicit permission from the device owner before installing or using a keylogger.
- Transparency: Be transparent about the purpose of the keylogger and how the collected data will be used.
- Legal Compliance: Ensure compliance with local laws and regulations regarding monitoring and data collection.

## Disclaimer
This code is for educational purposes only. Unauthorized use of keyloggers can violate privacy laws and ethical standards. Use responsibly and legally.

## Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements.

## License
This project is licensed under the MIT License
   
