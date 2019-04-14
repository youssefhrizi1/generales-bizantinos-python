import socket
import select
import errno
import sys
import time

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Client Name: ")

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
#client_socket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

#list of IP 
#toIP =  "192.168.0.101"
packip =["192.168.0.100", "192.168.0.102"]
clientIP =  "192.168.0.101"
#on register the all msg received with key and value
all_msg_client_name=['server']
#list of order receave
ordlist = []

while True:
    #code = client_socket.recv(HEADER_LENGTH).decode('utf-8')
    # Print message
    #print(code)

	
    code_header = client_socket.recv(HEADER_LENGTH)
    code_length = int(code_header.decode('utf-8').strip())
    codemessage = client_socket.recv(code_length).decode('utf-8')

    # Print message
    print(f'Order Received From Server :: {codemessage}')
    ordlist.append(codemessage)
    for x in packip:
         print("Set Order to :> ",x)
         message = input(f'{my_username} > ')
         #message=''
         # If message is not empty - send it
         if message:

             # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
             message = message.encode('utf-8')+x.encode('utf-8')
             message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
             client_socket.send(message_header + message)

    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:

            # Receive our "header" containing username length, it's size is defined and constant
            username_header = client_socket.recv(HEADER_LENGTH)

            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            # Convert header to int value
            username_length = int(username_header.decode('utf-8').strip())

            # Receive and decode username
            username = client_socket.recv(username_length).decode('utf-8')

            # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            #if the addr equal to this add client then print msg
            if clientIP==str(message[1:]):
                # Print message
                print(f'Receive From {username} : {message[0]}')
                #print(socket.gethostname())
                ordlist.append(message[0])
                all_msg_client_name.append(username)
            print("All Order Received ",ordlist)
            print("************************************")
            print(all_msg_client_name)

            #**************************************** Trator******************************************
            #Now we will detect the trator
            listof_Names=all_msg_client_name
            listof_order=ordlist
            my_list_order_len = len(listof_order)

            # count element 'i'
            count = listof_order.count(listof_order[0])
            count2=listof_order.count(listof_order[1])
            i=0
            if(count==3):
                print('No trator')
            elif(count==1):
                if(count2==1):
                    print('The server is the traitor')
                else:
                    print('Count of ',listof_order[0],' = ', count, ' So the trator is ',listof_Names[0])
            else:
                for x in range(1, my_list_order_len):
                    if(listof_order[x]!=listof_order[0]):
                        i=x
                        print('Count of ',listof_order[x],' = ', count-1, ' So the trator is ',listof_Names[x])
						

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()
