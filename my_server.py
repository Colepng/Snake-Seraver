import socket

import sqlite3 as sql


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
# # # # # # # filesize = os.path.getsize("test.txt")
# # # # # # print(f"Connected by {addr}")
# # # # # # # server.send(f"test.txt {filesize}".encode())
# # # # # # with open("Snake.sqlite3","rb") as f:
# # # # # #     while 1:
# # # # # #         f_reading = f.read(4096)
# # # # # #         if not f_reading:    
# # # # # #             conn.shutdown(socket.SHUT_WR)
# # # # # #             break
# # # # # #         conn.sendto(f_reading,addr)

while 1:
    data = conn.recv(1024)

    if data != None or data != b'':
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
            

            #check if username is taken
            con = sql.connect("Snake.sqlite3")
            cur = con.cursor()


            check_username_available = f"SELECT username FROM Snake WHERE username = '{username}';"
            check_public_username_available= f"SELECT public_username FROM Snake WHERE public_username = '{public_username}';"
            for i in range(1):
                cur.execute(check_username_available)
                username_available = cur.fetchone()
                print(username_available)

                if username_available == None:
                    print("username good")
                    username_good_bad = "good"
                    # conn.sendall(b"username good")
                else:
                    print("username bad")
                    username_good_bad = "bad"
                    # conn.sendall(b"username bad")
                    # run in till username good
                    # while 1:
                    #     conn.rect
                    #     pass
            
            

                cur.execute(check_public_username_available)
                public_username_available = cur.fetchone()
                print(public_username_available)


                if public_username_available == None:
                    print("public username good")
                    p_username_good_bad = "good"
                    # conn.sendall(b"public_username good")
                    # insert_public_username = f"INSERT INTO Snake (public_username )VALUES ('{public_username}')"
                    # cur.execute(insert_public_username)
                else: 
                    print("public username bad")
                    p_username_good_bad = "bad"
                    # conn.sendall(b"public_username bad")

            if public_username_available == None and username_available == None:
                    add_new_user = f"INSERT INTO Snake VALUES ('{username}','{password}','{public_username}','{highscore}')"
                    cur.execute(add_new_user)
                    conn.sendall(b"created_user")
            else: conn.sendall(f"invaild_valid {username_good_bad} {p_username_good_bad}".encode("utf-8"))

            con.commit()
            con.close()             #added sepernt command for inserting into the database

                #     print("username good")
                #     break
                # else:
                #     print("username or public_username not a")
                    


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
    

