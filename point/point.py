class MyPoints:
	def __init__(self, coord_x, coord_y, color):
		"""
		constructor function for a given point
		:param coord_x: x coordinate
		:param coord_y: y coordinate
		:param color: the color of the point
		"""
		self.__coord_x = coord_x
		self.__coord_y = coord_y
		self.__color = color

	def set_x(self, coord_x):
		"""
		set a x coordinate to my point
		:param coord_x: coordinate x
		:return:
		"""
		self.__coord_x = coord_x

	def set_y(self, coord_y):
		"""
		set a y coordinate to my point
		:param coord_y: y coordinate
		:return:
		"""
		self.__coord_y = coord_y

	def set_color(self, color):
		"""
		set the color of a  point
		:param color: color of point
		:return:
		"""
		self.__color = color

	def get_x(self):
		"""
		get the x coordinate
		:return:
		"""
		return self.__coord_x

	def get_y(self):
		"""
		get y coordinate
		:return:
		"""
		return self.__coord_y

	def get_color(self):
		"""
		get the color of the point
		:return:
		"""
		return self.__color

	def __str__(self):
		"""
		returns the string representation of a point
		:return:
		"""
		return f"Point ({self.__coord_x}, {self.__coord_y}) of color {self.__color}"
