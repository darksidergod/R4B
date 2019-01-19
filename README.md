# Reverse-Acess-Backdoor
It is a two-way python based program that can be used to gain full-control over the target. It uses ...

## Getting Started

### Basic Implemtation
Steps to get your program running. 

1. Clone the repository via SSH or by download the repo as a ZIP file.
2. Extract the ZIP files. (For SSH users, skip to step 3).
3. Copy the listener program on your attacker or control machine and backdoor on your target machine. 
4. In the "listener.py" file, open with a text editor and set the ip ="<Control Machine IP Address">.
5. Modify the port field to your accordance, set it to a valid port number that is not blocked.
6. Make the same changes to the "backdoor.py" file on the target machine.
7. Run the program on the attacker machine first as follows.
```
python listener.py
```
8. Repeat the previous step on the target machine but with the backdoor.
```
python backdoor.py
```

The attacker machine will show a successfull connection confirmation on the terminal window. Use the terminal as if you were on your host machine (sudo access not yet added, although it's in the works).


