#/usr/bin/python
import pygeoip
import os,sys

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
          return os.path.join(root, name)

try:
  gi = pygeoip.GeoIP('/home/rh0gue/Downloads/GeoLiteCity.dat')
except:
  gi = pygeoip.GeoIP(find('GeoLiteCity.dat','//'))

try:
  for i in range(1,len(sys.argv)):
    ip = sys.argv[i]
    print ip
    result = gi.record_by_addr(ip)
    for key,val in result.items():
      print "[*] "+str(key)+" : "+str(val)
    print "\n"
except:
  print "Usage: geolocate <ip address(s)>"
