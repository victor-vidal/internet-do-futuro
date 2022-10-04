import os
import sys

# ref: https://linuxhint.com/ping_command_ubuntu/
# ref: https://stackoverflow.com/questions/2953462/pinging-servers-in-python

if sys.argv[1] == 'master':
    #PACKAGE_COUNT = 62
    PACKAGE_HEADER_SIZE = 28
    PACKAGE_SIZE = 77 - PACKAGE_HEADER_SIZE
    PACKAGE_INTERVAL = 1
    
    print("Master script\n")
    command = ""
    for host in sys.argv[2:]:
        #command += f"ping -s {PACKAGE_SIZE} -i {PACKAGE_INTERVAL} {host} & "
        command += "ping -s " + str(PACKAGE_SIZE) + " -i " + str(PACKAGE_INTERVAL) + " " + host + " & "
    
    os.system(command)
    print("Terminou\n")
else:
    #PACKAGE_COUNT = 31
    PACKAGE_HEADER_SIZE = 28
    PACKAGE_SIZE = 88 - PACKAGE_HEADER_SIZE
    PACKAGE_INTERVAL = 2
    
    print("Slave script\n")
    #os.system(f"ping -s {PACKAGE_SIZE} -i {PACKAGE_INTERVAL} {sys.argv[2]}")
    os.system("ping -s " + str(PACKAGE_SIZE) + " -i " + str(PACKAGE_INTERVAL) + " " + sys.argv[2])
    print("\nTerminou\n")
