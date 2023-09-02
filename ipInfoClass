#############################
# Created by Nicholas Howland
# On day: 2023-09-02
# Purpose: to make a class that will return specific
# geographic information about IP addresses supplied

# Import urlopen the URL Library
from urllib.request import urlopen

# Create the class
class ipInfo():
    # function to return the City of the supplied IP address
    def getCity(self,addr=''):
                # Check to see if there is no IP address supplied if not then 
                # just get information about the current IP address
                if addr == '':
                        url = 'https://ipinfo.io/city'
                else:
                        url = 'https://ipinfo.io/' + addr + '/city'
                # Open the URL
                res = urlopen(url)
                # Read the url and decode it into utf-8
                data = res.read().decode("utf-8");
                # return the city informaiton without a trailing newline
                return data[0:-1];
        def getRegion(self,addr=''):
                if addr == '':
                        url = 'https://ipinfo.io/region'
                else:
                        url = 'https://ipinfo.io/' + addr + '/region'
                res = urlopen(url)
                data = res.read().decode("utf-8");
                return data[0:-1];
        def getCountry(self,addr=''):
                if addr == '':
                        url = 'https://ipinfo.io/country'
                else:
                        url = 'https://ipinfo.io/' + addr + '/country'
                res = urlopen(url)
                data = res.read().decode("utf-8");
                return data[0:-1];


# Useage
# creat a variuble for the class
ip=ipInfo();
print("Current IP addres information:")
print(ip.getCountry());
print(ip.getRegion());
print(ip.getCity());

print("IP addres information about 8.8.8.8:")
print(ip.getCountry("8.8.8.8");
print(ip.getRegion("8.8.8.8");
print(ip.getCity("8.8.8.8");

