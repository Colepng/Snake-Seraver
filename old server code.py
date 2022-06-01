# HOST = socket.gethostbyname(socket.gethostname())
# PORT = 8081


# # def update_highscore(username,highscore):
# #     con = sql.connect("Snake.sqlite3")
# #     cur = con.cursor()


# #     get_highscore = f"SELECT highscore FROM Snake WHERE username = '{username}'"

# #     cur.execute(get_highscore)
# #     fetch = cur.fetchone()
# #     print(fetch[0])

# #     update_highscore = f"UPDATE Snake set highscore = WHERE username = '{username}' VALUES ('{highscore}')"

# #     cur.execute(update_highscore)
# #     con.commit()
# #     cur.execute(get_highscore)
# #     fetch = cur.fetchone()
# #     print(fetch[0])


# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST,PORT))
# server.listen()
# conn, addr = server.accept()
# # # # # # # # filesize = os.path.getsize("test.txt")
# print(f"Connected by {addr}")
# # # # # # # server.send(f"test.txt {filesize}".encode())
# # # # # # with open("Snake.sqlite3","rb") as f:
# # # # # #     while 1:
# # # # # #         f_reading = f.read(4096)
# # # # # #         if not f_reading:    
# # # # # #             conn.shutdown(socket.SHUT_WR)
# # # # # #             break
# # # # # #         conn.sendto(f_reading,addr)