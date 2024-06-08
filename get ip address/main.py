import socket 
hostname = input('Enter website url: \n ')

print(f'The {hostname} IP address is {socket.gethostbyname(hostname)}')