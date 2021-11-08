import matplotlib.pyplot as plt


class PointRepository:
	def __init__(self, point_list = None):
		"""
		constructor for the points repository object
		:param point_list:
		"""
		if point_list is None:
			point_list = []
		self.points = point_list

	def add(self, point):
		"""
		add a point to repository
		:param point:
		:return:
		"""
		self.points.append(point)

	def get_all_points(self):
		"""
		get all the points
		:return:
		"""
		return self.points

	def get_point_index(self, index):
		"""
		get the point at a given index
		:param index: index from which we modify value
		:return:
		"""
		if 0 <= index <= len(self.points):
			return self.points[index]
		raise IndexError("Your index is not in the repository")

	def get_points_of_color(self, color):
		"""
		gets all points of given color
		:param color:
		:return:
		"""
		color_points = []
		for point in self.points:
			if point.color == color:
				color_points.append(point)
		return color_points

	def get_points_from_square(self, up_left_corner, length):
		"""
		returns all the points inside of a square which is given by the up corner and length
		:param up_left_corner: up corner coordinate
		:param length: length of a square side
		:return:
		"""
		points_in_square_list = []
		for point in self.points:
			if up_left_corner.coord_x + length >= point.coord_x >= up_left_corner.coord_x and up_left_corner.coord_y - length <= point.coord_y <= up_left_corner.coord_y:
				points_in_square_list.append(point)
		return points_in_square_list

	def minimum_distance(self):
		"""
		calculate the minimum distance between any two points
		:return:
		"""
		def calculate_distance(point_1, point_2):
			"""
			calculates the distance between two points
			:param point_1: first point
			:param point_2: second point
			:return:
			"""
			return ((point_1.coord_x - point_2.coord_x) ** 2 + (point_1.coord_y - point_2.coord_y) ** 2) ** (1 / 2)

		minimum = None
		if len(self.points) >= 2:
			minimum = calculate_distance(self.points[0], self.points[1])
		for i in range(len(self.points)):
			for j in range(i + 1, len(self.points)):
				minimum = min(minimum, calculate_distance(self.points[i], self.points[j]))
		if minimum is None:
			raise ValueError("The repository does not have enough points")
		return minimum

	def update_point_index(self, index, point):
		"""
		update a point at a given index
		:param index: index
		:param point: point to change with
		:return:
		"""
		if 0 <= index < len(self.points):
			self.points[index] = point
		else:
			raise IndexError("The index is invalid")

	def delete_point_index(self, index):
		"""
		delete a point at specific index
		:param index: the index
		:return:
		"""
		if 0 <= index < len(self.points):
			self.points.pop(index)
		else:
			raise IndexError("The index is invalid")

	def delete_points_from_square(self, up_left_corner, length):
		"""
		delete all point inside a square
		:param up_left_corner: coordinate of up left corner of square
		:param length: length of the sides of square
		:return:
		"""
		new_points = []
		for point in self.points:
			if not up_left_corner.coord_x + length >= point.coord_x >= up_left_corner.coord_x and up_left_corner.coord_y - length <= point.coord_y <= up_left_corner.coord_y:
				new_points.append(point)
		self.points = new_points

	def plot_the_points(self):
		"""
		plot all the point in a chart
		:return:
		"""
		for point in self.points:
			plt.scatter(point.coord_x, point.coord_y, 100, point.color)
		plt.show()

	def __str__(self):
		"""
		printing function
		:return:
		"""
		printing = "\n"
		for point in self.points:
			printing += point.__str__() + "\n"
		return printing

	def length(self):
		"""
		return the length of points list
		:return:
		"""
		return len(self.points)

	def all_points_circle(self, center, radius):
		"""
		get all points in a given circle
		:param center:
		:param radius:
		:return:
		"""
		def check_inside_circle(point):
			if (point.coord_x - center.coord_x) ** 2 + (point.coord_y - center.coord_y) ** 2 <= radius ** 2:
				return True
			return False
		circle_points = []
		for pt in self.points:
			if check_inside_circle(pt):
				circle_points.append(pt)
		return circle_points

	def counter_points_color(self, color):
		"""
		get the number of points with a given color
		:param color:
		:return:
		"""
		counter = 0
		for point in self.points:
			if point.color == color:
				counter += 1
		return counter

	def shift_y_points(self, value):
		"""
		shifts all y coordinates by a given value
		:param value:
		:return:
		"""
		for point in self.points:
			point.set_y(point.get_y() + value)
