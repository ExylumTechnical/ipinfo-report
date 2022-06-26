# ipinfo-report
This project sorts ip addresses into a single list, then pulls data from ipinfo.io about each corrosponding ip address. A final report is made that contains the raw data for each ip address in ip.txt


# Prerequisites
- connection to the internet and the site ipinfo.io
- a windows or linux machine with python installed

# General Strucutre
1) script looks in the ip.txt file and sorts the ip addresses contained
2) the user is prompted if they want to pull data from ip info
  a) if they do not then all files with the extension .ipinfo will be looked at instead of the new data
4) all files with an .ipinfo extension in the working directory will be put into a final report file
5) The regions found will be output to the screen for further decision making
6) All .ipinfo files will be put into the archive directory


# updates that need to be made
- If the user declines a pull request then the archive files should be used as a reference
