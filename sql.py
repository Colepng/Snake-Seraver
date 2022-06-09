import sqlite3 as sql


con = sql.connect("Snake.sqlite3")
cur = con.cursor()
def calc_in_grid(num_to_round, grid_size):  
    return round(num_to_round/grid_size)*grid_size




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
username = "test"
write_default_settings = f"""INSERT INTO Settings ('username', 'win_x', 'win_y', 'starting_x', 'starting_y', 'size', 'length', 'head_colour', 'snake_colour_1', 'snake_colour_2', 'head_colour_rgb', 'snake_colour_1_rgb', 'snake_colour_2_rgb', 'head_colour_hex', 'snake_colour_1_hex', 'snake_colour_2_hex', 'speed', 'if_hex') VALUES ( '{username}', '{win_x}', '{win_y}', '{starting_x}', '{starting_y}', '{size}', '{length}', '{head_colour_rgb}', '{snake_colour_1_rgb}', '{snake_colour_2_rgb}', '{head_colour_rgb}', '{snake_colour_1_rgb}', '{snake_colour_2_rgb}', '{head_colour_hex}', '{snake_colour_1_hex}', '{snake_colour_2_hex}', '{speed}', '{if_hex}')"""
add_new_user = "INSERT INTO Snake VALUES ('test','test','test','123')"
cur.execute(add_new_user)
#cur.execute(write_default_settings)
# cur.execute(delete_table)
# cur.execute(create_table)
con.commit()
con.close()



delete_table = '''DROP TABLE IF EXISTS Settings;'''
create_table = '''CREATE TABLE "Settings" (
	username	TEXT NOT NULL,
	win_x	INTEGER NOT NULL,
	win_y	INTEGER NOT NULL,
	size	INTEGER NOT NULL,
	length	INTEGER NOT NULL,
	head_colour	INTEGER NOT NULL,
	snake_colour_1	INTEGER NOT NULL,
	snake_colour_2	INTEGER NOT NULL,
	head_colour_rgb TEXT NOT NULL,
	snake_colour_1_rgb TEXT NOT NULL,
	snake_colour_2_rgb TEXT NOT NULL,
	head_colour_hex TEXT NOT NULL,
	snake_colour_1_hex TEXT NOT NULL,
	snake_colour_2_hex TEXT NOT NULL,
	speed	INTEGER NOT NULL,
	if_hex INTEGER NOT NULL
);'''