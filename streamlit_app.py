import streamlit as st
import serial
import time

# Set up serial connection (adjust port & baudrate if needed)
SERIAL_PORT = 'COM3'  # Replace with your actual COM port (e.g. 'COM4' or '/dev/ttyUSB0')
BAUD_RATE = 9600

# Try to establish the serial connection once
@st.cache_resource
def get_serial_connection():
    return serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)

ser = get_serial_connection()

st.title("Valve Controller")

# Button for Open
if st.button("Open Valve"):
    ser.write(b"open\n")
    st.write("Opening valve...")
    time.sleep(4)
    st.write("Valve opened. Power on.")

# Button for Close
if st.button("Close Valve"):
    ser.write(b"close\n")
    st.write("Closing valve...")
    time.sleep(4)
    st.write("Valve closed. Power off.")

# Button for Distance
if st.button("Get Distance"):
    ser.write(b"distance\n")
    time.sleep(0.5)
    output = ser.readline().decode().strip()
    if "Distance:" in output:
        st.success(output)
    else:
        st.warning("No distance response received.")
