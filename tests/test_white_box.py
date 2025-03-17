# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from src.white_box import (
    VendingMachine,
    calculate_total_discount,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_password,
)

# from src.white_box import VendingMachine, divide, get_grade, is_even, is_triangle


class TestWhiteBoxIsEven(unittest.TestCase):
    """White-box unittest class."""

    # Test cases 0.1 = "is_even(num)"
    def test_is_even_with_even_number(self):
        """Checks if a number is even."""
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """Checks if a number is not even."""
        self.assertFalse(is_even(7))

    def test_is_even_with_zero(self):
        """Check if zero is considered even"""
        self.assertTrue(is_even(0))

    def test_is_even_with_negative_even_number(self):
        """Check if a negative even number is even"""
        self.assertTrue(is_even(-4))

    def test_is_even_with_negative_odd_number(self):
        """Checks if a negative odd number is not event."""
        self.assertFalse(is_even(-3))


class TestWhiteBoxDivide(unittest.TestCase):
    """White-box unittest class."""

    # Test cases 0.2 = "divide(a, b)"
    def test_divide_by_non_zero(self):
        """Checks the divide function works as expected."""
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """Checks the divide function returns 0 when dividing by 0."""
        self.assertEqual(divide(10, 0), 0)

    def test_divide_positive_numbers(self):
        """Check division of two positive numbers."""
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        """Checks division of two negative numbers"""
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_positive_by_negative(self):
        """Checks division of a positive numbers by a negative number."""
        self.assertEqual(divide(10, -2), -5)

    def test_divide_negative_by_positive(self):
        """Checks division of a negative number by a positive number."""
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_one(self):
        """Checks division of a number by one"""
        self.assertEqual(divide(10, 1), 10)

    def test_divide_zero_by_number(self):
        """Checks division of zero by any number returns zero."""
        self.assertEqual(divide(0, 10), 0)


class TestWhiteBoxGrades(unittest.TestCase):
    """White-box unittest class."""

    # Test cases 0.3 = "get_grade(score)"
    def test_get_grade_a(self):
        """Checks if a score of 90 or higher returns grade 'A'."""
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """Checks if a score between 80-89 returns grade 'B'."""
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """Checks if a score between 70-79 returns grade 'C'."""
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """Checks if a score below 70 returns grade 'F'."""
        self.assertEqual(get_grade(65), "F")


class TestWhiteBoxTriangle(unittest.TestCase):
    """White-box unittest class."""

    # Test cases 0.4 = "is_triangle(a, b, c)"
    def test_is_triangle_yes(self):
        """Checks the three inputs can form a triangle."""
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """Checks the three inputs can't form a triangle when C is greater or equal than A + B."""
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """Checks the three inputs can't form a triangle when B is greater or equal than A + C."""
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """Checks the three inputs can't form a triangle when A is greater or equal than B + C."""
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")

    def test_is_triangle_equilateral(self):
        """Checks if three equal sides form a valid triangle."""
        self.assertEqual(is_triangle(1, 1, 1), "Yes, it's a triangle!")

    def test_is_triangle_zero_side(self):
        """Checks behaivor when one side is zero"""
        self.assertEqual(is_triangle(0, 4, 5), "No, it's not a triangle.")


class TestWhiteBoxCheckNum(unittest.TestCase):
    """White-box unittest class."""

    # Test cases 1 = "check_number_status(number)"
    def test_check_number_status_positive(self):
        """Checks if a positive number returns "Positive"."""
        self.assertEqual(check_number_status(10), "Positive")

    def test_check_number_status_negative(self):
        """Checks if a negative number returns "Negative"."""
        self.assertEqual(check_number_status(-10), "Negative")

    def test_check_number_status_decimal_positive(self):
        """Checks if a positive number returns "Positive"."""
        self.assertEqual(check_number_status(0.1), "Positive")

    def test_check_number_status_decimal_negative(self):
        """Checks if a negative number returns "Negative"."""
        self.assertEqual(check_number_status(-0.1), "Negative")

    def test_check_number_status_zero(self):
        """Checks if zero returns "Zero"."""
        self.assertEqual(check_number_status(0), "Zero")


class TestWhiteBoxValidatePass(unittest.TestCase):
    """White-box unittest class - #2 Validate_password."""

    # Test cases 2 = "validate_password(password)"
    def test_validate_password_valid(self):
        """Checks if a valid password thats meets all requerimetns returns True."""
        self.assertTrue(validate_password("Password1!"))

    def test_validate_password_too_short(self):
        """Checks if a password with less than 8 characters returns False"""
        self.assertFalse(validate_password("Pa1!"))

    def test_validate_password_no_uppercase(self):
        """Check if a password without uppercase letters returns False"""
        self.assertFalse(validate_password("password1!"))

    def test_validate_password_no_lowercase(self):
        """Check if a password without lowercase letters returns False"""
        self.assertFalse(validate_password("PASSWORD1!"))

    def test_validate_password_no_digit(self):
        """Check if a password without digits returns False"""
        self.assertFalse(validate_password("Password!"))

    def test_validate_password_no_special_char(self):
        """Check if a password without special characters returns False"""
        self.assertFalse(validate_password("Password1"))

    def test_validate_password_exact_length(self):
        """Check if a password with exactly 8 characters returns True"""
        self.assertTrue(validate_password("Password1!"))

    def test_validate_password_long_password(self):
        """Check if a password with more than 8 characters returns True"""
        self.assertTrue(validate_password("Password1!Password1!"))

    def test_validate_password_with_invalid_special_char(self):
        """Checks if a password with special characters not in the required set returns False."""
        self.assertFalse(validate_password("Password1*"))


class TestWhiteBoxCalculatorTotalDiscount(unittest.TestCase):
    """White-box unittest class - #3 Calculator_total_discount."""

    # Test cases 3 = "calculate_total_discount(total_amount)"
    def test_calculate_total_discount_below_shreshold(self):
        """Checks if amounts below 100 receive no discount."""
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_at_lower_threshould(self):
        """Checks if amount exactly at 100 receives 10% discount."""
        self.assertEqual(calculate_total_discount(100), 10)

    def test_calculate_total_discount_in_first_range(self):
        """Checks if amount in the first range (100-500) range receives 10% discount."""
        self.assertEqual(calculate_total_discount(200), 20)

    def test_calculate_total_discount_at_upper_threshold(self):
        """Checks if amount exactly at 500 receives 10% discount."""
        self.assertEqual(calculate_total_discount(500), 50)

    def test_calculate_total_discount_above_threshold(self):
        """Checks if amount above 500 receive 20% discount."""
        self.assertEqual(calculate_total_discount(600), 120)

    def test_calculate_total_discount_large_amount(self):
        """Checks if very large amounts receive 20% discount correctly"""
        self.assertEqual(calculate_total_discount(10000), 2000)

    def test_calculate_total_discount_zero(self):
        """Checks if zero amount receives no discount"""
        self.assertEqual(calculate_total_discount(0), 0)

    def test_calculate_total_discount_negative(self):
        """Checks handling of negative amounts."""
        self.assertEqual(calculate_total_discount(-100), 0)


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """Checks the vending machine can accept coins."""
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """Checks the vending machine fails to accept coins when it's not ready."""
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")
