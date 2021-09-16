from unittest import TestCase
from shapes_library.shapes_package.shapes_module import Circle
from shapes_library.shapes_package.shapes_module import Rectangle
from shapes_library.shapes_package.shapes_module import validateCircleRadius


class CircleTests(TestCase):
    """
    Contains all unit tests for the shapes_module.Circle class
    """
    def test_circle_area_returns_correct_result_with_valid_radius(self):
        """
        Tests that a Circle object with a radius > 0 returns the correct area
        """
        mock_radius = 5.0
        expected_area = 78.54
        mock_circle = Circle(radius=mock_radius)
        self.assertEqual(mock_circle.area(), expected_area)

    def test_circle_area_raises_ValueError_with_negative_radius(self):
        """
        Tests that a circle object with a negative raises a value error
        """
        with self.assertRaises(ValueError):
            mock_circle = Circle(radius = -1.0)


    def test_validateCircleRadius_is_handling_errors_properly(self):
        
        mock_radius = "string"
        with self.assertRaises(TypeError):
            validateCircleRadius(mock_radius)


class RectangleTests(TestCase):
    """
    Contains all the unit tests for the shapes_module.Rectangle class
    """
    def test_rectangle_area_returns_correct_result_with_valid_height_and_width(self):
        """
        Tests that a Rectangle object with a height > 0 and a width > 0 returns the correct area
        """
        mock_height, mock_width = 10., 10.
        expected_area = 100.
        mock_rectangle = Rectangle(height=mock_height, width=mock_width)
        self.assertEqual(mock_rectangle.area(), expected_area)

    def test_rectangle_area_raises_ValueError_with_negative_width_and_height(self):
        """
        Tests that a circle object with a negative raises a value error
        """
        with self.assertRaises(ValueError):
            mock_height = Rectangle(height = -1.0)
            mock_width = Rectangle(width = -1.0)


class CapitalTests(TestCase):
    """
    Contains all the unit tests for the shapes_module.Name class
    """
    def test_name_spelling_starts_with_capital_letter(self):
       """
       Tests if first letter of name is Capital
       """
       with self.assertRaises(ValueError):
            mock_name = "Abcd"
            mock_name[0].islower()
