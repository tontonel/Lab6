from ui.menus.main_menu import main_menu
from repository.points_repo import PointRepository
from point.point import MyPoints
from domain.point_operations import point_operations
from domain.repository_operations import repository_operations


def run():
	"""
	run the app
	:return:
	"""
	commands = [5]
	repo = PointRepository([])
	my_point = MyPoints(0, 0, "red")
	while not commands[0] == 0:
		try:
			commands = main_menu()
			if commands[0] == 1:
				if commands[1] == 1:
					if commands[2] == 1 or commands[2] == 2:
						coord = int(input("Enter the coordinate: "))  # for both coordinates
						point_operations(commands, my_point, coord)
					else:
						color = input("Enter color: ")
						point_operations(commands, my_point, color)
				elif commands[1] == 2:
					point_operations(commands, my_point)
				else:
					point_operations(commands, my_point)
			elif commands[0] == 2:
				if commands[1] == 1:
					coord_x = int(input("Enter the x coordinate: "))
					coord_y = int(input("Enter the y coordinate: "))
					color = input("Enter the color: ")
					new_point = MyPoints(coord_x, coord_y, color)
					repository_operations(commands, repo, new_point)
				elif commands[1] == 2:
					repository_operations(commands, repo)
				elif commands[1] == 3:
					index = int(input("Enter index: "))
					repository_operations(commands, repo, index)
				elif commands[1] == 4:
					color = input("Enter the color: ")
					repository_operations(commands, repo, color)
				elif commands[1] == 5:
					coord_x = int(input("Enter up left corner x coordinate: "))
					coord_y = int(input("Enter up left corner y coordinate: "))
					length = int(input("Enter the length of the square side: "))
					up_left_corner = MyPoints(coord_x, coord_y, "red")
					repository_operations(commands, repo, up_left_corner, length)
				elif commands[1] == 6:
					repository_operations(commands, repo)
				elif commands[1] == 7:
					index = int(input("Enter an index: "))
					coord_x = int(input("Enter the new x coordinate: "))
					coord_y = int(input("Enter the new y coordinate: "))
					color = input("Enter the new color: ")
					new_point = MyPoints(coord_x, coord_y, color)
					repository_operations(commands, repo, index, new_point)
				elif commands[1] == 8:
					index = int(input("Enter an index: "))
					repository_operations(commands, repo, index)
				elif commands[1] == 9:
					coord_x = int(input("Enter up left corner's x coordinate: "))
					coord_y = int(input("Enter up left corner's y coordinate: "))
					up_left_corner = MyPoints(coord_x, coord_y, "red")
					length = int(input("Enter square side's length: "))
					repository_operations(commands, repo, up_left_corner, length)
				elif commands[1] == 10:
					repository_operations(commands, repo)
				elif commands[1] == 11:
					coord_x = int(input("Enter x coordinate of center: "))
					coord_y = int(input("Enter y coordinate of center: "))
					radius = int(input("Enter radius of the circle: "))
					center = MyPoints(coord_x, coord_y, "red")
					repository_operations(commands, repo, center, radius)
				elif commands[1] == 12:
					color = input("Enter a color: ")
					repository_operations(commands, repo, color)
				elif commands[1] == 13:
					value = int(input("Enter a value: "))
					repository_operations(commands, repo, value)
		except TypeError as ty:
			print(f"\n{ty}\n")
		except ValueError as vl:
			print(f"\n{vl}\n")
		except IndexError as ir:
			print(f"\n{ir}\n")
	return None










