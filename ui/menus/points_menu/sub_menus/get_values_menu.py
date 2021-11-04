def get_values_menu():
	"""
	prints the menus
	:return:
	"""
	print("1.Get the value x")
	print("2.Get the value y")
	print("3.Get the color")
	command = int(input("Enter command: "))
	if not 1 <= command <= 3:
		raise TypeError("Your command is invalid")
	return command

