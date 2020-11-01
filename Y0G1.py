#!/usr/bin/env python3

import socket   #Module that simplifies the task of writing network servers
import os       #Module that provides a portable way of using operating system dependent functionality

HOST = "10.0.2.15"  #The Private IP address of the Host Machine
PORT = 2000         #The port that you choose to act as an open target

print(" Y88b   d88P  .d8888b.   .d8888b. 8888888")      #Ascii of Y0G1
print("  Y88b d88P  d88P  Y88b d88P  Y88b   888  ")
print("   Y88o88P   888    888 888    888   888  ")
print("    Y888P    888    888 888          888  ")
print("     888     888    888 888  88888   888  ")
print("     888     888    888 888    888   888  ")
print("     888     Y88b  d88P Y88b  d88P   888  ")
print("     888       Y8888P    Y8888P88 8888888 ")  

print("        (())___(() ")            #Ascii of mascot
print("        /      \\\\")
print("       ( /    \ \\\\")
print("        \ o o    /")
print("        (_()_)__/  \\")
print("       / _,==.____\\")
print("      (   |--|      )")
print("      /\_.|__|'-.__/\_")
print("     / (        /     \\")
print("     \  \      (      /")
print("      )  '._____)    /")
print("   (((____.--(((____/")


print("YogiBear Honeypot Initialized")      #The indication that the Honeypot is now activated

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

while True:
    conn, addr = server.accept()
    print("Honeypot has been visited by", addr)
    conn.send(("Welcome to Ubuntu 18.04.4 LTS (GNU/LINUX 4.18.0-15-generic x86_64)").encode())
    conn.send(("\n").encode())
    conn.send((" * Documentation:   https://help.ubuntu.com").encode())
    conn.send(("\n").encode())
    conn.send((" * Management:       https://landscape.canonical.com").encode())
    conn.send(("\n").encode())
    conn.send((" * Support:         https://ubuntu/com/advantage").encode())
    conn.send(("\n").encode())
    conn.send(("\n").encode())
    conn.send((" * Kubernetes 1.19 is out! Get it in one command with:").encode())
    conn.send(("\n").encode())
    conn.send(("\n").encode())
    conn.send(("    sudo snap install microk8s --channel=1.19 --classic").encode())
    conn.send(("\n").encode())
    conn.send(("\n").encode())
    conn.send(("    https://microk8s.io/ has docs and details.").encode())
    conn.send(("\n").encode())
    conn.send(("\n").encode())
    conn.send((" * Cannoical Livepatch is available for installation.").encode())
    conn.send(("\n").encode())
    conn.send(("   - Reduce system reboots and improve kernel security. Activate at:").encode())
    conn.send(("\n").encode())
    conn.send(("    https://ubuntu.com/livepatch").encode())
    conn.send(("\n").encode())
    conn.send(("\n").encode())
    conn.send(("Your Hardware Enablement Stack (HWE) is supported until April 2023").encode())
    conn.send(("\n").encode())
    conn.send(("\n").encode())
    conn.send(("-----------------------------------------------------------------").encode())
    conn.send(("\n").encode())
    conn.send(("    Ubuntu 18.04.LTS                          built 2019-12-16   ").encode())
    conn.send(("\n").encode())
    conn.send(("-----------------------------------------------------------------").encode())
    conn.send(("\n").encode())
    conn.send(("Welcome Ubuntu User").encode())
    conn.send(("\n").encode())
    conn.send(("sansforensics@siftworkstation:~$").encode())
    conn.send(("\n").encode())
    os.system("/usr/bin/wireshark")
conn.close()

