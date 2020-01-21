# MacInfo Application

MacInfo Application outputs Company Name information by providing MAC address as input

Note: Only Traditional 12-digit MAC addresses are considered in this script

## Build Docker Image

1. Clone macinfo repo<br>
```git clone https://github.com/bopini/macinfo```
2. Run following docker command in macinfo directory<br>
```docker build -t macinfo:1 . ```

## Run Docker Image
1. Run the container <br>
```docker run -it macinfo:1 sh```
2. Run the script<br>
    ```python3 find_mac_info.py --mac_address=BC-92-6B-A0-00-01``` <br>
   Mac address arguments supported in the format of<br>```BC-92-6B-A0-00-01 or BC:92:6B:A0:00:01 or BC926BA00001```

## Run Doc Test - Limited coverage

1. Limited coverage for doc test (not fully implemented): <br>
   ```python3 -m doctest -v find_mac_info.py```

## Enhancements:

1. Security : Need to use  hardened docker image. For time being selected alpine image since it is light weight
2. Support 64 bit MAC address