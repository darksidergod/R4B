# Reverse-Acess-Backdoor
It is a two-way python based program that can be used to gain full-control over the target. It uses a reverse connection from the target computer so that the firewall would not block it as suspicious port opening since it opens the port on the target machine itself and then sends the connection request to the attacker machine/control machine as well.
Note - Based on python 2.7 (python 3 variant in the works !)

## Getting Started

### Basic Usage
##### (Linux)
Steps to get your program running. 

1. Clone the repo via SSH or by download the repo as a ZIP file.
2. Extract the ZIP files. (For SSH users, skip to step 3).
3. Copy the listener program on your attacker or control machine and backdoor on your target machine. 
4. In the "listener.py" file, open with a text editor and set the ip ="<Control Machine IP Address">.
5. Modify the port field to your accordance, set it to a valid port number that is not blocked.
6. Make the same changes to the "backdoor.py" file on the target machine.
7. Run the program on the attacker machine on the linux terminal first as follows.
```
python listener.py
```
8. Repeat the previous step on the target machine but with the backdoor. 
```
python backdoor.py
```

The attacker machine will show a successfull connection confirmation on the terminal window. Use the terminal as if you were on your host machine (sudo access not yet added, although it's in the works).


### Advanced Usage
#### (Target Windows Machine)
The basic mode was just to explain how the reverse backdoor is working. The advanced impelementaion focuses on how to use this program as an exploit with target computers. Packaging is the technique that we will be using to package our python code as executables which will look like any normal program that we desire. It can be packaged with a .pdf, .jpeg, .exe or any other extension. We will only need to package the backdoor since the attacker is knowingly running the listener.

-> It is advised to package from the same OS that the backdoor will be running on.

Steps to package backdoor.

1. Install python for windows on your linux computer from the link below.
```
https://www.python.org/downloads/windows/
```
2(a). Install wine on your packaging machine. 
```
sudo apt-get install wine 
```
2(b). For 32-bit systems.
```
sudo apt-get install wine32
```
3. Unpackage using Wine(Wine is not an emulator). 
```
root@kali:~/Downloads# wine msiexec /i python-2.7.15.amd64.msi 
```
It will install wine on your Linux.

4. List your hidden wine directory. By doing the following command in your root/home directory.
```
ls -a
```
5. Enter your python.exe path for wine and install pyinstaller as follows.
This will install pyinstaller.exe to your Python27/Scripts folder.
```
wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller
```
6. Package the file as follows to an .exe program which runs silently on a windows machine. (Run this command from the folder of your python program.
```
wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe <program.py> --onefile --noconsole
```

## Example
### Basic Implementation

![alt text](https://github.com/darksidergod/Reverse-Acess-Backdoor/blob/master/examples/Screenshot%20from%202019-01-19%2012-17-35.png)
![alt text](https://github.com/darksidergod/Reverse-Acess-Backdoor/blob/master/examples/Screenshot%20from%202019-01-19%2012-18-05.png)
![alt text](https://github.com/darksidergod/Reverse-Acess-Backdoor/blob/master/examples/Screenshot%20from%202019-01-19%2012-18-14.png)

