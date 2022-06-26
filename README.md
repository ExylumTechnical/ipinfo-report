# ipinfo-report
This project sorts ip addresses into a single list, then pulls data from ipinfo.io about each corresponding ip address. A final report is made that contains the raw data for each ip address in ip.txt

# Prerequisites
- connection to the internet and the site ipinfo.io
- a windows or linux machine with python installed

# General Structure
1) script looks in the ip.txt file and sorts the ip addresses contained
2) the user is prompted if they want to pull data from ip info
   - if N is selected .ipinfo files in the archive directory will be used
   - if Y is selected fresh info from ipinfo.io will be used
4) all files with an .ipinfo extension in the working directory will be used in the final report
5) A final report is generated and put into the report.txt file and regions are output to assist in spotting irregularities off the bat
6) All .ipinfo files will be put into the archive directory for later use


# Considerations
- the ip.txt file must only be ip addresses, comments are not supported
- this is free code and a proof of concept project not ment for commercial purposes, however it works under the following conditions
  - the filter.py file is run in its own directory
  - the ip.txt file is present and filled with valid data
- there is little to no input validation so be careful with the ip.txt file and any file with a .ipinfo extension

This is inteded at a tooling foundation and not as a complete project.
