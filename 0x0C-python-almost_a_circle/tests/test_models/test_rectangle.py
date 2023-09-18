#!/usr/bin/python3
"""defines classe"""


import unittest
from unittest.mock import patch
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """TestRectangleMethods"""

    @classmethod
    def setUp(self):
        """setUp"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """tearDown"""
        pass

    def test_docstring(self):
        """test_docstring"""
        self.assertIsNotNone(Rectangle.__doc__)

    def test_randos_id(self):
        """test_randos_id"""
        r1 = Rectangle(20, 4)
        r2 = Rectangle(4, 20)
        r3 = Rectangle(20, 4, 0, 0, 24)
        r4 = Rectangle(4, 20)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 4)
        self.assertEqual(r3.id, 22)
        self.assertEqual(r4.id, 6)

    def test_class(self):
        """test_class"""
        self.assertEqual(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_class_inheritance(self):
        """test_class_inheritance"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_arg_passed(self):
        """test_arg_passed"""
        with self.assertRaises(TypeError):
            Rectangle(20)
            Rectangle()

    def test_constructor_no_args(self):
        """test_constructor_no_args"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "missing 2 required positional arguments: 'width' \ and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_constructor_one_arg(self):
        """test_constructor_one_arg"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_width_height_1(self):
        """test_width_height_1"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Chris", 18)
            Rectangle('c', 18)
            Rectangle(True, 16)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(15, "Breezy")
            Rectangle(15, 'c')
            Rectangle(True, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 8, "CB")
            Rectangle(10, 8, 'c')
            Rectangle(True, 4, 8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 4, 2, 'c')
            Rectangle(6, 4, 2, "CB")
            Rectangle(True, 2, 4, 6)

    def test_width_height_2(self):
        """test_width_height_2"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-14, 4)
            Rectangle(0, 2)
            Rectangle(0, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(12, -10)
            Rectangle(4, 0)
            Rectangle(2, 0)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 8, -4)
            Rectangle(13, 4, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(14, 12, 10, -10)
            Rectangle(8, 4, 1, 0)

    def test_area_1(self):
        """test_area_1"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 2 * 3)
        self.assertEqual(r2.area(), 2 * 10)
        self.assertEqual(r3.area(), 8 * 7)

    def test_area_2(self):
        """test_area_2"""
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.area(), 4)
        r1.width = 5
        self.assertEqual(r1.area(), 10)
        r1.height = 5
        self.assertEqual(r1.area(), 25)

    def test_area_no_args(self):
        """test_area_no_args"""
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        s = "missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_basic_display(self):
        """test_basic_display"""
        r1 = Rectangle(6, 8)
        result = "####\n####\n####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_basic_display_2(self):
        """test_basic_display_2"""
        r1 = Rectangle(5, 4, 1, 1)
        result = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_4(self):
        """test_display_4"""
        r1 = Rectangle(3, 2)
        result = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

        r1.x = 4
        result = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

        r1.y = 2
        result = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_no_args(self):
        """test_display_no_args"""
        r = Rectangle(9, 8)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        s = "missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_complex_display(self):
        """test_complex_display"""
        r1 = Rectangle(2, 2)
        result = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

        r1.width = 6
        result = "######\n######\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):
        """test_str"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        result = "[Rectangle] (12) 2/1 - 4/6\n"
        result2 = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(r2.__str__(), result2)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_no_args(self):
        """test_str_no_args"""
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        s = "missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_update_args(self):
        """test_update_args"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """test_update_kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(height=10)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/10")
        r.update(width=11, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 11/10")
        r.update(y=3, width=4, x=5, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 5/3 - 4/10")
        r.update(x=6, height=7, y=8, width=9)
        self.assertEqual(str(r), "[Rectangle] (89) 6/8 - 9/7")

    def test_to_dictonary_1(self):
        """test_to_dictonary_1"""
        r1 = Rectangle(10, 2, 1, 9)
        d1 = r1.to_dictionary()
        j1 = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        r2 = Rectangle(1, 1)
        d2 = r2.to_dictionary()
        j2 = {'x': 0, 'y': 0, 'id': 2, 'height': 1, 'width': 1}
        self.assertEqual(d1, j1)
        self.assertEqual(d2, j2)
        self.assertEqual(type(d1), dict)
        self.assertEqual(type(d2), dict)

    def test_save_to_file_1(self):
        """test_save_to_file_1"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_save_to_file_2(self):
        """test_save_to_file_2"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_save_to_file_3(self):
        """test_save_to_file_3"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s2f = [r1, r2]
        Rectangle.save_to_file(s2f)
        rf = Rectangle.load_from_file()
        self.assertNotEqual(s2f, rf)

    def test_create(self):
        """test_create"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (1) 1/0 - 3/5", str(r2))
        self.assertNotEqual(r1, r2)

    def test_load_from_file_1(self):
        """test_load_from_file_1"""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r1, r2])
        Base._Base__nb_objects = 0
        lff = Rectangle.load_from_file()
        self.assertEqual(lff[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(lff[1].to_dictionary(), r2.to_dictionary())
