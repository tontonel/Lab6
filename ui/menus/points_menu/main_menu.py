from ui.menus.points_menu.sub_menus.get_values_menu import get_values_menu as get_val
from ui.menus.points_menu.sub_menus.set_value_menu import set_value_menu as set_val


def main_menu():
	"""
	prints the main menus
	:return:
	"""
	print("1.Set the values for my point")
	print("2.Get the values for my point")
	print("3.Get a string representation for my point")
	command = int(input("Enter a command: "))
	subcommand = None
	if command == 1:
		subcommand = set_val()
	elif command == 2:
		subcommand = get_val()
	elif command == 3:
		return [command]
	elif command != 0:
		raise ValueError("Your command is invalid")
	return command, subcommand
