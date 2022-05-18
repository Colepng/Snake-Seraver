import socket
import os
import sqlite3 as sql
import sys


HOST = socket.gethostbyname(socket.gethostname())
PORT = 8081


def update_highscore(username,highscore):
    con = sql.connect("Snake.sqlite3")
    cur = con.cursor()


    get_highscore = f"SELECT highscore FROM Snake WHERE username = '{username}'"

    cur.execute(get_highscore)
    fetch = cur.fetchone()
    print(fetch[0])

    update_highscore = f"UPDATE Snake set highscore = WHERE username = '{username}' VALUES ('{highscore}')"

    cur.execute(update_highscore)
    con.commit()
    cur.execute(get_highscore)
    fetch = cur.fetchone()
    print(fetch[0])


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
conn, addr = server.accept()
# filesize = os.path.getsize("test.txt")
print(f"Connected by {addr}")
# server.send(f"test.txt {filesize}".encode())
with open("Snake.sqlite3","rb") as f:
    while 1:
        f_reading = f.read(4096)
        if not f_reading:    
            conn.shutdown(socket.SHUT_WR)
            break
        conn.sendto(f_reading,addr)


while 1:
    data = conn.recv(1024)

    if data != None and data != b'':
        print(data)
        data_decoded = data.decode()
        data_split = data_decoded.split(" ")
        command = data_split[0]
        
        if command == "create_user":
            username = data_split[1]
            public_username = data_split[2]
            password = data_split[3]
            highscore = data_split[4]
            print(username,public_username,password,highscore)




        elif command == "hello":
            print("hello command")
        elif command == "updated":
            print("update command")
        # update_highscore(username,10)
        # print("updated highscore")


conn.close()
# server.close()
# while 1:
#     data = conn.recv(1024)
#     if not data:
#         break
    

