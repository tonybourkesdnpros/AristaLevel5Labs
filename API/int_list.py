# Import the pyeapi library
import pyeapi


switches = ['leaf1-DC1', 'leaf2-DC1', 'leaf3-DC1', 'leaf4-DC1',]

# Open a session with leaf1-DC1 



for switch in switches:
    connect = pyeapi.connect_to(switch)
    connect.api("ipinterfaces").create('Ethernet7')
    result = connect.api("ipinterfaces").set_address('Ethernet7','7.7.7.7/24')
    if result == True:
        print("Completed")
    if result == False:
        print("Error")