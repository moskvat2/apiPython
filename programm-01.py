import os
import paramiko
import platform
import time
import pwinput
from tkinter import *

class SSHClient:
    def __init__(self, master):
        self.master = master
        master.title("SSH Client")

        # Labels
        self.ip_label = Label(master, text="IP Address")
        self.ip_label.grid(row=0, column=0)

        self.user_label = Label(master, text="Username")
        self.user_label.grid(row=1, column=0)

        self.pass_label = Label(master, text="Password")
        self.pass_label.grid(row=2, column=0)

        self.command_label = Label(master, text="Command")
        self.command_label.grid(row=3, column=0)

        # Entries
        self.ip_entry = Entry(master)
        self.ip_entry.grid(row=0, column=1)

        self.user_entry = Entry(master)
        self.user_entry.grid(row=1, column=1)

        self.pass_entry = Entry(master, show="*")
        self.pass_entry.grid(row=2, column=1)

        self.command_entry = Entry(master)
        self.command_entry.grid(row=3, column=1)

        # Buttons
        self.ping_button = Button(master, text="Ping", command=self.ping)
        self.ping_button.grid(row=0, column=2)

        self.execute_button = Button(master, text="Execute", command=self.execute)
        self.execute_button.grid(row=3, column=2)

        # Output
        self.output_text = Text(master, height=10, width=50)
        self.output_text.grid(row=4, columnspan=3)

    def ping(self):
        ip = self.ip_entry.get()
        response = os.system("ping -c 1 " + ip)

        if response == 0:
            self.output_text.insert(END, "Ping successful: " + ip + "\n")
        else:
            self.output_text.insert(END, "Ping unsuccessful: " + ip + "\n")

    def execute(self):
        ip = self.ip_entry.get()
        user = self.user_entry.get()
        passwd = pwinput.pwinput(prompt='Password: ', stream=None)
        command = self.command_entry.get()

        # SSH Connection with Command Execution
        ssh = paramiko.SSHClient()