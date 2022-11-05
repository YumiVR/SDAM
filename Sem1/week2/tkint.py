import tkinter
rows = []
for i in range (5):
	cols = []
	for i in range(4):
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=j, stickey=NSEW)
		e.insert(END, '%d.%d' % (i,j))
		cols.append(e)
		rows.append(cols)
