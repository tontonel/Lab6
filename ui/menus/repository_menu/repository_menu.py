def repo_menu():
	"""
	printing the repository menu
	:return:
	"""
	print("1.Add a point to the repository")
	print("2.Get all points")
	print("3.Get a point at a given index")
	print("4.Get all points of a given color")
	print("5.Get all points that are inside a given square(up-left corner and length given)")
	print("6.Get the minimum distance between two points")
	print("7.Update a point at a given index")
	print("8.Delete a point by index")
	print("9.Delete all points that are inside a given square")
	print("10.Plot all points in a chart")
	print("11.Get all points in a given circle (center and radius)")
	print("12.Get the counter of number of given color")
	print("13.Shift all the y coordinates with a given value")
	command = int(input("Enter a command: "))
	if not 1 <= command <= 13:
		raise TypeError("Your command is invalid")
	return command
