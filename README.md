MacInfo ReadmeMacInfo Readme:<br>
This repo contains a script that gets Company Name information by providing MAC address as argument <br>
Note: Only Traditional 12-digit MAC addresses are considered in this script

Build Docker Image:
1. Clone macinfo project
2. Go to macinfo directory in terminal
3. docker build -t macinfo:1 .

Run Docker Image:
1. In Terminal, docker run -it macinfo:1 sh
2. Run one of following command<br>
    python3 find_mac_info.py BC-92-6B-A0-00-01<br>
    python3 find_mac_info.py BC:92:6B:A0:00:01<br>

Enhancements:
Priority:
1. Security : Need to use  hardened docker image. For time being selected alpine image since it is light weight
2. Support 64 bit MAC address
Low:
1. Handle more exceptions
2. Shall be written in object oriented
3. Improve arg parser for usage, for now using simple print statement