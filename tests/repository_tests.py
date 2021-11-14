from unittest import TestCase, main
from point.point import MyPoints
from repository.points_repo import PointRepository
from utils.utils import compare, compare_repo


class RepositoryTest(TestCase):

	def setUp(self):
		self.points = PointRepository([MyPoints(3, 2, "blue"), MyPoints(4, 5, "red"), MyPoints(1, 1, "green")])

	def test_add(self):
		with self.assertRaises(ValueError):
			self.points.add(MyPoints(3, 3, "purple"))
			self.points.add(MyPoints(4, 5, "red"))
		self.points.add(MyPoints(2, 1, "blue"))
		self.assertEqual(self.points.length(), 4)

	def test_get_all_points(self):
		self.assertEqual(len(self.points.get_all_points()), 3)
		no_points = PointRepository().get_all_points()
		self.assertEqual(no_points, [])
		self.assertEqual(self.points.get_all_points(), self.points.get_all_points())

	def test_get_point_index(self):
		with self.assertRaises(IndexError):
			self.points.get_point_index(-1)
			self.points.get_point_index(5)
		self.assertTrue(compare(self.points.get_point_index(1), MyPoints(4, 5, "red")))

	def test_get_points_of_color(self):
		with self.assertRaises(ValueError):
			self.points.get_points_of_color("purple")
		self.assertTrue(compare_repo(self.points.get_points_of_color("red"), PointRepository([MyPoints(4, 5, "red")])))
		self.assertTrue(compare_repo(self.points.get_points_of_color("yellow"), PointRepository()))

	def test_points_from_square(self):
		up_left_corner = MyPoints(3, 5, "blue")
		length = -1
		with self.assertRaises(ValueError):
			self.points.get_points_from_square(up_left_corner, length)
		length = 5
		self.assertEqual(self.points.get_points_from_square(up_left_corner, length).length(), 2)
		up_left_corner = MyPoints(-1, -1, "red")
		length = 5
		self.assertEqual(self.points.get_points_from_square(up_left_corner, length).length(), 0)

	def test_minimum_distance(self):
		empty_repo = PointRepository()
		with self.assertRaises(ValueError):
			empty_repo.minimum_distance()
		self.assertEqual(self.points.minimum_distance(), 5 ** (1 / 2))
		self.points.add(MyPoints(1, 0, "blue"))
		self.assertEqual(self.points.minimum_distance(), 1)

	def test_update_point_index(self):
		with self.assertRaises(ValueError):
			self.points.update_point_index(1, MyPoints(1, 1, "purple"))
			self.points.update_point_index(-1, MyPoints(1, 1, "red"))
			self.points.update_point_index(10, MyPoints(1, 1, "red"))

	def test_delete_point_index(self):
		with self.assertRaises(IndexError):
			self.points.delete_point_index(-1)
			self.points.delete_point_index(19)
		self.points.delete_point_index(1)
		self.assertTrue(compare_repo(self.points, PointRepository([MyPoints(3, 2, "blue"), MyPoints(1, 1, "green")])))

	def test_delete_points_from_square(self):
		with self.assertRaises(ValueError):
			self.points.delete_points_from_square(MyPoints(1, 1, "red"), - 1)
		self.points.delete_points_from_square(MyPoints(1, 1, "red"), 1)
		self.assertTrue(compare_repo(self.points, PointRepository([MyPoints(3, 2, "blue"), MyPoints(4, 5, "red")])))

	def test_all_points_circle(self):
		with self.assertRaises(ValueError):
			self.points.all_points_circle(MyPoints(1, 1, "blue"), -1)
		new_repo = self.points.all_points_circle(MyPoints(0, 0, "blue"), 10)
		self.assertTrue(compare_repo(new_repo, self.points))
		new_repo = self.points.all_points_circle(MyPoints(0, 0, "blue"), 2)
		self.assertEqual(new_repo.length(), 1)

	def test_counter_points_color(self):
		with self.assertRaises(ValueError):
			self.points.counter_points_color("purple")
		self.assertEqual(self.points.counter_points_color("yellow"), 0)
		self.assertEqual(self.points.counter_points_color("red"), 1)

	def test_shift_y_points(self):
		self.points.shift_y_points(0)
		self.assertTrue(compare_repo(self.points, PointRepository([MyPoints(3, 2, "blue"), MyPoints(4, 5, "red"), MyPoints(1, 1, "green")])))
		self.points.shift_y_points(-1)
		self.assertTrue(compare_repo(self.points, PointRepository([MyPoints(3, 1, "blue"), MyPoints(4, 4, "red"), MyPoints(1, 0, "green")])))
		new_repo = PointRepository()
		new_repo.shift_y_points(10)
		self.assertTrue(compare_repo(new_repo, PointRepository()))


if __name__ == "__main__":
	main()
