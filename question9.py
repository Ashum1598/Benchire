import os
#from pythonping import ping

ip = input("Enter IP:")
res = os.system("ping " + ip)
#x = ping(ip, verbose=True, count=2)
#print(x.success)
if res == 0:   
      print('IP is Active')
else:
      print('IP is Inactive')
