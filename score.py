#!/usr/bin/env python3


import requests
import bs4
from tkinter import *
import time

class window(Frame):
	def __init__(self, master=None):
		Frame.__init__self(self,master)
		self.master = master
		self.pack(fill=BOTH,expand=1)
		text = Label(self,text=st)



while True:
	link = 'https://www.cricbuzz.com/live-cricket-scores/32258/ind-vs-eng-3rd-test-england-tour-of-india-2021'
	res = requests.get(link)
	bs = bs4.BeautifulSoup(res.text,'html.parser')
	score = bs.select('.cb-col-100 .cb-col .cb-col-scores')
	cur = bs.select('.cb-min-itm-rw')


	for i in score:
		print(i.getText())

	for i in cur:
		print(i.div.div.getText())

	print('')
	time.sleep(300)
"""root = TK()
app = window(root)
root.wm_title("Score")
root.geometry("100x100")
root.mainloop()"""

