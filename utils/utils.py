def check_color(color_1):
	"""
	this function checks if the color is valid
	:param color_1:
	:return:
	"""
	colors = ["yellow", "red", "green", "blue", "magenta"]
	for col in colors:
		if col == color_1:
			return True
	return False

