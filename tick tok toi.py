#importing Packages from tkinter
from tkinter import *
from tkinter import messagebox 

Player = 'X'
stop_game = False

def clicked(a,b):
	
	#player
	global Player
	# global stop_game

	if Player == "X" and states[a] == 0 and stop_game == False:
		b[a].configure(text = "X")
		states[a] = 'X'
		Player='O'

	
	if Player == 'O' and states[a] == 0 and stop_game == False:
		b[a].configure(text = 'O')
		states[a] = "O"
		Player = "X"

	check_if_win()
	# check_if_tie()
	# if check_if_win() == False:
	#	 tie = messagebox.showinfo("tie","its tie")
	#	 return tie
def check_if_win():
	global stop_game
	# count = 0

	for i in range(4):
		if states[i][0] == states[i][1] == states[i][2] ==states[i][3]!=0:
			stop_game = True

			winner = messagebox.showinfo("Winner", states[i][0] + " Won")
			# disableAllButton()
			break

	# for j in range(4):
		elif states [0][i] == states[1][i] == states[2][i] ==states[3][i] != 0:
			stop_game = True

			winner = messagebox.showinfo("Winner", states[0][i]+ " Won!")
			break

		elif states[0][0] == states[1][1] == states[2][2] ==states[3][3] !=0:
			stop_game = True

			winner = messagebox.showinfo("Winner", states[0][0]+ " Won!")
			break

		elif states[0][3] == states[1][1] == states[2][0] == states[3][0] !=0:
			stop_game = True

			winner = messagebox.showinfo("Winner" , states[0][3]+ " Won!")
			break

		elif states[0][0] and states[0][1] and states[0][2]  and states [0][3]and states[1][0] and states[1][1] and states[1][2] and states[1][3] and states[2][0] and states[2][1] and states[2][2]and states[2][3] != 0:
			stop_game = True

			winner = messagebox.showinfo("tie", "Tie")

# Design window
#Creating the Canvas 
root = Tk()
# Title of the window			 
root.title("Tic Tac Toe") 
root.resizable(0,0)

#Button
b = [
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]]

#text for buttons
states = [
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]]

for i in range(3):
	for j in range(3): 
									
		b[i][j] = Button(
						height = 4, width = 8, 
						font = ("Helvetica","10"), 
						command = lambda r = i, c = j : clicked(a,b))
		b[i][j].grid(row = i, column = j)


mainloop()		 
