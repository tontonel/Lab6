def point_operations(commands, *args):
	"""
	make operations on points
	:return:
	"""
	if commands[1] == 1:
		if commands[2] == 1:
			print(1)
			(point, coord) = args
			point.set_x(coord)
		elif commands[2] == 2:
			(point, coord) = args
			point.set_y(coord)
		else:
			(point, color) = args
			point.set_color(color)
	elif commands[1] == 2:
		(point,) = args
		if commands[2] == 1:
			print(f"\n{point.get_x()}\n")
		elif commands[2] == 1:
			print(f"\n{point.get_y()}\n")
		else:
			print(f"\n{point.get_color()}\n")
	else:
		(point,) = args
		print(f"\n{point}\n")

