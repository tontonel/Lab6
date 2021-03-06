from utils.utils import check_color
from repository.points_repo import PointRepository


def repository_operations(commands, *args):
	"""
	make operations on repository
	:return:
	"""
	if commands[1] == 1:
		(repo, new_point) = args
		if not check_color(new_point.get_color()):
			raise ValueError("The color is invalid you can choose only from these colors: yellow, red, green, blue, magenta")
		repo.add(new_point)
	elif commands[1] == 2:
		(repo,) = args
		elements = PointRepository(repo.get_all_points())
		if elements.length == 0:
			print("\nThere are no points in repository\n")
		else:
			print(elements)
	elif commands[1] == 3:
		(repo, index) = args
		print(f"\n{repo.get_point_index(index)}\n")
	elif commands[1] == 4:
		(repo, color) = args
		if not check_color(color):
			raise ValueError("The color is invalid you can choose only from these colors: yellow, red, green, blue, magenta")
		color_points = repo.get_points_of_color(color)
		if color_points.length() == 0:
			print(f"\nThere are no {color} points in repository\n")
		else:
			print(color_points)
	elif commands[1] == 5:
		(repo, up_left_corner, length) = args
		if length <= 0:
			raise ValueError("\nThe length of the square has to be positive\n")
		elements = repo.get_points_from_square(up_left_corner, length)
		if length <= 0:
			raise ValueError("\nThe length is not positive\n")
		if elements.length() == 0:
			raise Exception("\nThere are no elements in this square\n")
		else:
			print(elements)
	elif commands[1] == 6:
		(repo,) = args
		print(f"\n{repo.minimum_distance()}\n")
	elif commands[1] == 7:
		(repo, index, point) = args
		if not check_color(point.get_color()):
			raise ValueError("\nThe color is invalid you can choose only from these colors: yellow, red, green, blue, magenta\n")
		repo.update_point_index(index, point)
	elif commands[1] == 8:
		(repo, index) = args
		repo.delete_point_index(index)
	elif commands[1] == 9:
		(repo, up_left_corner, length) = args
		if length <= 0:
			raise ValueError("\nThe length of the square has to be positive\n")
		repo.delete_points_from_square(up_left_corner, length)
	elif commands[1] == 10:
		(repo,) = args
		repo.plot_the_points()
	elif commands[1] == 11:
		(repo, center, radius) = args
		circle_points = repo.all_points_circle(center, radius)
		if circle_points.length() == 0:
			raise Exception("There are no points in this circle")
		print(circle_points)
	elif commands[1] == 12:
		(repo, color) = args
		if not check_color(color):
			raise ValueError("\nThe color is invalid you can choose only from these colors: yellow, red, green, blue, magenta\n")
		print(f"\n{repo.counter_points_color(color)}\n")
	elif commands[1] == 13:
		(repo, value) = args
		repo.shift_y_points(value)






