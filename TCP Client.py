import socket

target_host = "www.google.com"
target_port = "80"

#creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting the client
client.connect((target_host,target_port))

#Sending some data
client.send("GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

#Recieving some data
response = client.recv(4096)

print response 