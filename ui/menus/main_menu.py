from ui.menus.points_menu.main_menu import main_menu as points_menu
from ui.menus.repository_menu.repository_menu import repo_menu


def main_menu():
	"""
	printing the menu
	:return:
	"""
	print("1.Points operations")
	print("2.Repository operations")
	print("0.Exit")
	command = int(input("Enter a command: "))
	commands = [command]
	if command == 1:
		commands.append(points_menu())
	elif command == 2:
		commands.append(repo_menu())
	elif command == 0:
		pass
	else:
		raise TypeError("Your command is invalid")
	return commands
