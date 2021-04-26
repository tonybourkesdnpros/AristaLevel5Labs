# Import the pyeapi library
import pyeapi


switches = ['leaf1-DC1', 'leaf2-DC1', 'leaf3-DC1', 'leaf4-DC1']

# Open a session with leaf1-DC1 



connect = pyeapi.connect_to('leaf1-DC1')


# "Create" sets the port as a Layer 3 port (no switchport)

connect.api("ipinterfaces").create('Ethernet7')

# Set Ethernet4 for the IP address of 4.4.4.4 and put the result into the variable (boolean) result




result = connect.api("ipinterfaces").set_address('Ethernet7','7.7.7.7/24')

# Very basic error handling here, basically gives a yes or no answer. 

if result == True:
    print("Completed!")

if result == False:
    print("Error!")