with open("text.txt", "w") as textfile:
	textfile.write("Python is so annoying!")

	if textfile.closed == False:
	    textfile.close()

	print my_file.closed
