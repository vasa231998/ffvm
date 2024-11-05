send_msg_via_socket = True

terminal_server_ip   = '100.106.178.97'
terminal_server_port = 12345
socket_initialized   = False
client_socket        = None

import socket

def showStatusMsg(msg):
    global terminal_server_ip, terminal_server_port, send_msg_via_socket, socket_initialized, client_socket
    try :
        if send_msg_via_socket == False:
            print(msg)
            return
        
        # Send via socket
        if socket_initialized == False:
            # Create socket object
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to the server
            client_socket.connect((terminal_server_ip, terminal_server_port))
            print(f"Connected to terminal server at {terminal_server_ip}:{terminal_server_port}")
            socket_initialized = True

        client_socket.send(msg.encode())
    except Exception as e:
        print(f"error in connecting server {e}")
        pass
showStatusMsg("Client Connected")