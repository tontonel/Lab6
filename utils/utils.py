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


def compare(pt1, pt2):
	if pt1.get_color() == pt2.get_color() and pt1.get_x() == pt2.get_x() and pt1.get_y() == pt2.get_y():
		return True
	return False


def compare_repo(rep1, rep2):
	list_1 = rep1.get_all_points()
	list_2 = rep2.get_all_points()
	if len(list_2) != len(list_1):
		return False
	for i in range(len(list_1)):
		if not compare(list_1[i], list_2[i]):
			return False
	return True
