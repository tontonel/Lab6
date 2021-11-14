from unittest import TestCase, main
from point.point import MyPoints
from utils.utils import compare


class PointTest(TestCase):

	def setUp(self):
		self.point = MyPoints(1, 1, "blue")

	def test_set_x(self):
		self.point.set_x(2)
		self.assertTrue(compare(self.point, MyPoints(2, 1, "blue")))
		self.point.set_x(1)
		self.assertTrue(compare(self.point, MyPoints(1, 1, "blue")))
		self.point.set_x(-10)
		self.assertTrue(compare(self.point, MyPoints(-10, 1, "blue")))

	def test_set_y(self):
		self.point.set_y(2)
		self.assertTrue(compare(self.point, MyPoints(1, 2, "blue")))
		self.point.set_y(1)
		self.assertTrue(compare(self.point, MyPoints(1, 1, "blue")))
		self.point.set_y(-10)
		self.assertTrue(compare(self.point, MyPoints(1, -10, "blue")))

	def test_set_color(self):
		with self.assertRaises(ValueError):
			self.point.set_color("purple")
		self.point.set_color("green")
		self.assertTrue(compare(self.point, MyPoints(1, 1, "green")))
		self.point.set_color("yellow")
		self.assertTrue(compare(self.point, MyPoints(1, 1, "yellow")))

	def test_get_x(self):
		x_coord = self.point.get_x()
		self.assertTrue(x_coord == 1)
		self.point.set_x(2)
		x_coord = self.point.get_x()
		self.assertTrue(x_coord == 2)
		self.point.set_x(0)
		x_coord = self.point.get_x()
		self.assertTrue(x_coord == 0)

	def test_get_y(self):
		y_coord = self.point.get_y()
		self.assertTrue(y_coord == 1)
		self.point.set_y(2)
		y_coord = self.point.get_y()
		self.assertTrue(y_coord == 2)
		self.point.set_y(0)
		y_coord = self.point.get_y()
		self.assertTrue(y_coord == 0)

	def test_get_color(self):
		color = self.point.get_color()
		self.assertTrue(color == "blue")
		self.point.set_color("yellow")
		color = self.point.get_color()
		self.assertTrue(color == "yellow")
		self.point.set_color("magenta")
		color = self.point.get_color()
		self.assertTrue(color == "magenta")


if __name__ == "__main__":
	main()
