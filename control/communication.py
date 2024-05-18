import serial

class Communication:
    def __init__(self, port, baud_rate=9600):
        self.port = port
        self.baud_rate = baud_rate
        self.serial_conn = serial.Serial(port, baud_rate)
        
    def send_action(self, robot_id, action):
        message = f"{robot_id}:{action}"
        self.serial_conn.write(message.encode())
