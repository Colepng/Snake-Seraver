import socket

import sqlite3 as sql
from time import time
import _thread
def calc_in_grid(num_to_round, grid_size):
    return round(num_to_round/grid_size)*grid_size

def main(conn,adrr):
    while 1:
        data = conn.recv(1024)

        if data != None or data != b'':
            # print(data)
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
                        
                        size = 35
                        win_x = calc_in_grid(1000,size)
                        win_y = calc_in_grid(800,size)
                        print(win_x/2, win_y/2, win_x, win_y)
                        starting_x = calc_in_grid(win_x/2,size)
                        starting_y = calc_in_grid(win_y/2,size)
                        print(starting_x, starting_y)
                        length = 6
                        head_colour_rgb = [0, 0, 255]
                        snake_colour_1_rgb = [0, 255, 0]
                        snake_colour_2_rgb = [0,150,0]
                        head_colour_hex = "#0000ff"
                        snake_colour_1_hex = "#00ff00"
                        snake_colour_2_hex = "#009600"
                        speed = 8
                        if_hex = False
                        write_default_settings = f"""INSERT INTO Settings VALUES ('{username}', '{win_x}', '{win_y}', '{starting_x}', '{starting_y}', '{size}', '{length}', 
                        '{head_colour_rgb}', '{snake_colour_1_rgb}', '{snake_colour_2_rgb}', '{head_colour_rgb}', '{snake_colour_1_rgb}', '{snake_colour_2_rgb}', 
                        '{head_colour_hex}', '{snake_colour_1_hex}', '{snake_colour_2_hex}', '{speed}', '{if_hex}')"""
                        cur.execute(write_default_settings)
                        con.commit()
                        con.close()
                        conn.sendall(b"created_user")
                
                else: conn.sendall(f"invaild_valid {username_good_bad} {p_username_good_bad}".encode("utf-8"))
                        
                # con.commit()
                # con.close()             #added sepernt command for inserting into the database

            elif command == "sync":
                conn.sendto(b"sync",addr)
                with open("Snake.sqlite3","rb") as f:
                    while 1:
                        f_reading = f.read(4096)
                        if not f_reading:    
                            conn.shutdown(socket.SHUT_WR)
                            break
                        conn.sendto(f_reading,addr)
            # elif command == "update_highscore":
            #     username = data_split[1]
            #     highscore = data_split[2]
            #     print(username, highscore)
            #     con = sql.connect("Snake.sqlite3")
            #     cur = con.cursor()
            #     update_highscore = f"UPDATE Snake SET highscore = '{highscore}' WHERE username = '{username}'"
            #     cur.execute(update_highscore)
            #     con.commit()
            #     con.close()



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

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8081


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(5)
while 1:
    print(f"Listening on {HOST}:{PORT}")
    conn, addr = server.accept()
    # print(conn,addr)
    _thread.start_new_thread(main, (conn,addr))
    # # # # # # # filesize = os.path.getsize("test.txt")
    print(f"Connected by {addr}")

