MacInfo Readme
This repo contains a script that gets Company Name information by providing MAC address as argument 

Build Docker Image:
1. Clone macinfo project
2. Go to macinfo directory in terminal
3. docker build -t macinfo:1 .

Run Docker Image:
1. In Terminal, docker run -it macinfo:1 sh
2. Run one of following command
    python3 find_mac_info.py BC-92-6B-A0-00-01
    python3 find_mac_info.py BC:92:6B:A0:00:01
