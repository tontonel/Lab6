def set_value_menu():
	"""
	menus for set values
	:return:
	"""
	print("1.Set x value")
	print("2.Set y value")
	print("3.Set color")
	command = int(input("Enter command: "))
	if not 1 <= command <= 3:
		raise TypeError("Your command is invalid")
	return command
