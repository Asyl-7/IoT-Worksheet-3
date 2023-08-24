# IoT-Worksheet-3
IoT Worksheet 3 – Webserver to send Realtime sensory Data
Aim of this project is to send sensory data from the microbit , in this example the light level, to a simple web server in real time. This project involves three things, the microbit, and its serial data connection and the webserve.

# How it works:
1.	The microbit sends data through uart module which makes use of the serial usb connection 
2.	The data is received through the python pyseries module by making a connection to the usb port. (PLEASE NOTE THAT you need to change the ‘COM3’ to your usb port. To do this go to device manager and go to Ports and check which one has Microsoft one then change accordingly )
3.	The data is received from a flask application. Flask is used to create a webserver
4.	Flask then updates the html in real time with the sensory data received 
5.	The light level is displayed on your webpage


# Libraries Used
* `pyserial`
* `flask`
* `flask_socketio`
* `threading`

# How to run
*	Create a virtual environment
* python -m venv venv           # Create a virtual environment
* source venv/bin/activate     # Activate the virtual environment (Linux/macOS)
*	pip install Flask
*	once its done to run the app, run the code python app.py

  

