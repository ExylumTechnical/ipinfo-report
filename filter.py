from os import system
from platform import system as os_type


# put all of the IP addresses into a list and return a sorted list
def list_data():
    ip_log=open("ip.txt","r")
    ip_raw_list=ip_log.readlines()
    ip_raw_list.sort()
    ip_log.close()
    return ip_raw_list

# create a result list that contains no duplicate IP addresses
def unique_ip(ip_list):
    count=0
    ip_result=[]
    for i in ip_list:
        if(count<=len(ip_list)):
            try:
                if(i!=ip_list[count-1]):
                    ip_result.append(i)
            finally:
                count=count
        count=count+1
    return ip_result

# pull IPinfo data for processing
def pull_data(ip_result):
    for i in ip_result:
        cmd_str="curl ipinfo.io/"+i+" > "+i+".ipinfo"
        system(cmd_str)

ip_list=list_data()
ip_result=unique_ip(ip_list)
pull_dec=input("Pull information about the ip addresses from ipinfo.io? (Y/N)")
valid=0
while(valid==0):
    if(pull_dec=="Y"):
        pull_data(ip_result)
        valid=1
    elif(pull_dec=="N"):
        valid=1
    else:
        pull_dec=""
        print("Please only enter Y or N")

os=os_type()
if(os=="Windows"):
    if(pull_dec=="N"):
        for i in ip_result:
            cmd="copy archive\\"+i+".ipinfo .\\"
            system(cmd)
    system("echo > fullreport.txt")
    system("type *.ipinfo >> fullreport.txt")
    system("""
    type fullreport.txt | find \"region\" && echo ##########################################&& echo see fullreport.txt for detailed information about the IP addresses listed && echo courtisy of ipinfo.io && echo ########################################## && pause
    """)
    system("mkdir archive && move *.ipinfo archive")
elif(os=="Linux"):
    if(pull_dec=="N"):
        for i in ip_result:
            cmd="cp archive/"+i+".ipinfo ./"
            system(cmd)
    system("echo > fullreport.txt")
    system("cat *.ipinfo >> fullreport.txt")
    system("""
    cat fullreport.txt | grep \"region\"; echo ##########################################; echo see fullreport.txt for detailed information about the IP addresses listed; echo courtisy of ipinfo.io && echo ##########################################;
    """)
    system("mkdir archive; mv *.ipinfo archive")
else:
    print("""
        Looks like your OS is unknown... maybe MacOS? Maybe some embeded device?
        Who knows... however all hope is not lost, there is raw data you can
        parse out all on your own. the files are
            {ip address}.ipinfo - for curled ipinfo.io files
            fullreport.txt - for the cumulitive data that is in each of those
                             ipinfo.io results
          """)




    
