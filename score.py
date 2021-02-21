#!/usr/bin/env python3


import requests
import bs4
from tkinter import *

class window(Frame):
	def __init__(self, master=None):
		Frame.__init__self(self,master)
		self.master = master
		self.pack(fill=BOTH,expand=1)
		text = Label(self,text=st)



link = 'https://www.cricbuzz.com/live-cricket-scores/31449/5th-match-csa-t20-challenge-2021	'

res = requests.get(link)


bs = bs4.BeautifulSoup(res.text,'html.parser')

score = bs.select('.cb-col-100 .cb-col .cb-col-scores')
current = bs.select('.cb-key-lst-wrp .cb-font-12')

for i in score:
	print(i.getText().strip())


root = TK()
app = window(root)
root.wm_title("Score")
root.geometry("100x100")
root.mainloop()

