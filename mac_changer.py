import subprocess
interface = input("enter your interface :")
mac = input("type mac address you want :")


subprocess.run("ifconfig " + interface + " down" ,shell=True) 
subprocess.run("ifconfig " + interface + " hw ether " + mac , shell=True)
subprocess.run("ifconfig " + interface + " up",shell=True)

print ("mac address changed successfully")
