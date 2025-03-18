# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from src.white_box import (
    VendingMachine,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_email,
    validate_login,
    validate_password,
    verify_age,
    validate_date,
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


class TestWhiteBoxCalculateOrderTotal(unittest.TestCase):
    """White-box unittest class - #4 calculate_order_total."""

    # Test cases 4 = "calculate_order_total(items)"
    def test_calculate_order_total_empty(self):
        """Checks if an empty items list returns zero total."""
        self.assertEqual(calculate_order_total([]), 0)

    def test_calculate_order_total_single_item_no_discount(self):
        """Checks calculation for a single item with quantity in the no-discount range (1-5)."""
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items), 30)

    def test_calculate_order_total_single_item_small_discount(self):
        """Checks calculation for a single item with quantity in the 5% discount range (6-10)"""
        items = [{"quantity": 8, "price": 10}]
        self.assertEqual(calculate_order_total(items), 76)

    def test_calculate_order_total_single_item_large_discount(self):
        """Checks calculation for a single item with quantity in the 10% discount range (> 10)."""
        items = [{"quantity": 15, "price": 10}]
        self.assertEqual(calculate_order_total(items), 135)

    def test_calculate_order_total_zero_quantity(self):
        """Checks Handling of zero quantity items"""
        items = [{"quantity": 0, "price": 10}]
        self.assertEqual(calculate_order_total(items), 0)


class TestWhiteBoxCalculateItemsShipingCost(unittest.TestCase):
    """White-box unittest class - #5 calculate_items_shipping_cost."""

    # Test cases 5 = "calculate_items_shipping_cost(items)"
    def test_calculate_items_shipping_cost_standard_low_weight(self):
        """Checks standard shipping cost for weight <= 5."""
        items = [{"weight": 2}, {"weight": 1}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_standard_medium_weight(self):
        """Checks standard shipping cost for weight between 5 and 10"""
        items = [{"weight": 3}, {"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_high_weight(self):
        """Checks standard shipping cost for weight > 10"""
        items = [{"weight": 11}, {"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_low_weight(self):
        """Checks express shipping cost for weight <= 5"""
        items = [{"weight": 2}, {"weight": 2.5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_express_medium_weight(self):
        """Checks express shipping cost for weight between 5 and 10"""
        items = [{"weight": 3}, {"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_exppress_high_weight(self):
        """Checks express shipping cost for weight > 10"""
        items = [{"weight": 11}, {"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_empty_items(self):
        """Check shipping cost for an empty items list"""
        self.assertEqual(calculate_items_shipping_cost([], "standard"), 10)


class TestWhiteBoxValidateLogin(unittest.TestCase):
    """White-box unittest class - #6 validate_login."""

    # Test cases 6 = "validate_login(username, password)"
    def test_validate_login_successful(self):
        """Checks if valid username and password combination returns 'Login Successful'."""
        self.assertEqual(validate_login("validuser", "password123"), "Login Successful")

    def test_validate_login_username_too_short(self):
        """Checks if username shorter than 5 characters returns 'Login Failed'."""
        self.assertEqual(validate_login("user", "password123"), "Login Failed")

    def test_validate_login_username_too_long(self):
        """Checks if username longer than 20 characters returns 'Login Failed'."""
        self.assertEqual(
            validate_login("thisusernameiswaytoolong", "password123"), "Login Failed"
        )

    def test_validate_login_password_too_short(self):
        """Checks if password shorter than 5 characters returns 'Login Failed'."""
        self.assertEqual(validate_login("validuser", "pass"), "Login Failed")

    def test_validate_login_password_too_long(self):
        """Checks if password longer than 15 characters returns 'Login Failed'."""
        self.assertEqual(validate_login("validuser", "pass"), "Login Failed")

    def test_validate_login_boundary_username_min(self):
        """Checks login with username at minimum length boundary (5 characters)."""
        self.assertEqual(validate_login("user1", "password123"), "Login Successful")

    def test_validate_login_boundary_username_max(self):
        """Checks login with username at maximum length boundary (20 characters)."""
        self.assertEqual(
            validate_login("usernameistwentychar", "password123"), "Login Successful"
        )

    def test_validate_login_boundary_password_min(self):
        """Checks login with password at minimum length boundary (8 characters)."""
        self.assertEqual(validate_login("validuser", "pass1234"), "Login Successful")

    def test_validate_login_boundary_password_max(self):
        """Checks login with password at maximum length boundary (15 characters)."""
        self.assertEqual(
            validate_login("validuser", "passwordfifteen"), "Login Successful"
        )


class TestWhiteBoxVerifyAge(unittest.TestCase):
    """White-box unittest class - #7 verify_age."""

    # Test cases 7 = "verify_age(age)"
    def test_verify_age_eligible_minimum(self):
        """Checks if age at lower boundary (18) returns 'Eligible'."""
        self.assertEqual(verify_age(18), "Eligible")

    def test_verify_age_eligible_maximum(self):
        """Checks if age at upper boundary (65) returns 'Eligible'."""
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_not_elegible_below(self):
        """Checks if age below lower boundary (17) returns 'Not Eligible'."""
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_zero(self):
        """Checks if age zero returns 'Not Eligible'."""
        self.assertEqual(verify_age(0), "Not Eligible")

    def test_verify_age_very_old(self):
        """Checks if age above upper boundary (100) returns 'Not Eligible'."""
        self.assertEqual(verify_age(100), "Not Eligible")


class TestWhiteBoxCategorizeProduct(unittest.TestCase):
    """White-box unittest class - #8 categorize_product."""

    # Test cases 8 = "categorize_product(product_name)"
    def test_categorize_product_lower_boundary(self):
        """Checks if price at lower boundary of Category A (10) returns 'Category A'."""
        self.assertEqual(categorize_product(10), "Category A")

    def test_categorize_product_a_upper_boundary(self):
        """Checks if price at upper boundary of Category A (50) returns 'Category A'."""
        self.assertEqual(categorize_product(50), "Category A")

    def test_categorize_product_b_lower_boundary(self):
        """Checks if price at lower boundary of Category B (51) returns 'Category B'."""
        self.assertEqual(categorize_product(51), "Category B")

    def test_categorize_product_b_upper_boundary(self):
        """Checks if price at upper boundary of Category B (100) returns 'Category B'."""
        self.assertEqual(categorize_product(100), "Category B")

    def test_categorize_product_c_lower_boundary(self):
        """Checks if price at lower boundary of Category C (101) returns 'Category C'."""
        self.assertEqual(categorize_product(101), "Category C")

    def test_categorize_product_c_upper_boundary(self):
        """Checks if price at upper boundary of Category C (200) returns 'Category C'."""
        self.assertEqual(categorize_product(200), "Category C")

    def test_categorize_product_d_below(self):
        """Checks if price below lower boundary of Category D (9) returns 'Category D'."""
        self.assertEqual(categorize_product(9), "Category D")

    def test_categorize_product_d_above(self):
        """Checks if price above upper boundary of Category D (201) returns 'Category D'."""
        self.assertEqual(categorize_product(201), "Category D")


class TestWhiteBoxValidateEmail(unittest.TestCase):
    """White-box unittest class - #9 validate_email."""

    # Test cases 9 = "validate_email(email)"
    def test_validate_email_valid(self):
        """Checks if a properly formatted email returns  'Valid Email'."""
        self.assertEqual(validate_email("test@example.com"), "Valid Email")

    def test_validate_email_too_short(self):
        """Checks if email shorter than 5 characters returns 'Invalid Email'."""
        self.assertEqual(validate_email("t@e."), "Invalid Email")

    def test_validate_email_too_long(self):
        """Checks if email longer than 50 characters returns 'Invalid Email'."""
        self.assertEqual(
            validate_email(
                "thisisaverylongemailthatexceedsfiftycharacters@example.com"
            ),
            "Invalid Email",
        )

    def test_validate_email_no_at_symbol(self):
        """Checks if email without @ symbol returns 'Invalid Email'."""
        self.assertEqual(validate_email("testexample.com"), "Invalid Email")

    def test_validate_email_no_dot(self):
        """Checks if email without dot returns 'Invalid Email'."""
        self.assertEqual(validate_email("test@examplecom"), "Invalid Email")

    def test_validate_email_minium_length(self):
        """Checks if email with exact minium length (5) returns 'Valid Email'."""
        self.assertEqual(validate_email("test@.com"), "Valid Email")

    def test_validate_email_maxium_length(self):
        """Checks if email with exact maximum length (50) returns 'Valid Email'."""
        self.assertEqual(
            validate_email("testemailexampleforlongcharacterssssss@example.com"),
            "Valid Email",
        )

    def test_validate_email_empty_string(self):
        """Checks if empty string returns 'Invalid Email'."""
        self.assertEqual(validate_email(""), "Invalid Email")


class TestWhiteBoxCelsiusToFahrenheit(unittest.TestCase):
    """White-box unittest class - #10 celsius_to_fahrenheit."""

    # Test cases 10 = "celsius_to_fahrenheit(celsius)"
    def test_celsius_to_fahrenheit_zero(self):
        """Checks conversion of 0°C to Fahrenheit"""
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_positive(self):
        """Checks conversion of positive Celsius temperature to Fahrenheit"""
        self.assertEqual(celsius_to_fahrenheit(20), 68)

    def test_celsius_to_fahrenheit_negative(self):
        """Checks conversion of negative Celsius temperature to Fahrenheit"""
        self.assertEqual(celsius_to_fahrenheit(-10), 14)

    def test_celsius_to_fahrenheit_lower_boundary(self):
        """Checks conversion at lower boundary (-100°C) of valid range"""
        self.assertEqual(celsius_to_fahrenheit(-100), -148)

    def test_celsius_to_fahrenheit_upper_boundary(self):
        """Checks conversion at upper boundary (100°C) of valid range"""
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_below_range(self):
        """Checks handling of temperature below valid range."""
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_above_range(self):
        """Checks handling of temperature above valid range."""
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")


class TestWhiteBoxValidateCreditCard(unittest.TestCase):
    """White-box unittest class - #11 validate_credit_card."""

    # Test cases 11 = "validate_credit_card(card_number)"
    def test_validate_credit_card_valid_min(self):
        """Checks if credit card with minimum valid length (13 digits) return 'Valid Card'."""
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_validate_credit_card_valid_max(self):
        """Checks if credit card with maximum valid length (16 digits) return 'Valid Card'."""
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_validate_credit_card_too_short(self):
        """Checks if credit card number too short (12 digits) returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_valdiate_credit_card_too_long(self):
        """Checks if credit card number too long (17 digits) returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_credit_card_non_digit(self):
        """Checks if credit card with non-digit characters returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card("a1234567890123"), "Invalid Card")

    def test_validate_credit_card_with_spaces(self):
        """Checks if credit card with spaces returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card(" 12345 6789 0123"), "Invalid Card")

    def test_validate_credit_card_empty_string(self):
        """Checks if empty string returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card(""), "Invalid Card")


class TestWhiteBoxValidateDate(unittest.TestCase):
    """White-box unittest class - #12 validate_date."""
    # Test cases 12 = "validate_date(date_string)"
    def test_validate_date_valid(self):
        """Checks if a valid date returns 'Valid Date'. """
        self.assertEqual(validate_date(2022, 1, 1), "Valid Date")

    def test_validate_date_year_too_early(self):
        """Checks if year before 1900 returns 'Invalid Date'."""
        self.assertEqual(validate_date(1899, 5 ,15), "Invalid Date")

    def test_validate_date_year_too_late(self):
        """Checks if year after 2100 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2101, 5, 15), "Invalid Date")

    def test_validate_date_month_too_low(self):
        """Checks if month below 1 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 0, 15), "Invalid Date")

    def test_validate_date_month_too_high(self):
        """Checks if mont above 12 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 13, 15), "Invalid Date")

    def test_validate_date_day_too_low(self):
        """Checks if day below 1 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 5, 0), "Invalid Date")

    def test_validate_date_day_too_high(self):
        """Checks if day above 31 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 5, 32), "Invalid Date")

    def test_validate_date_year_boundary_min(self):
        """Checks if year lower boundary (1900) returns 'Valid Date'"""
        self.assertEqual(validate_date(1900, 5 ,15), "Valid Date")

    def test_validate_date_year_boundary_max(self):
        """Checks if year upper boundary (2100) returns 'Valid Date"""
        self.assertEqual(validate_date(2100, 5, 15), "Valid Date")

    def test_validate_date_month_boundary_min(self):
        """Checks if month at lower boundary (1) returns 'Valid Date'."""
        self.assertEqual(validate_date(2000, 1, 15), "Valid Date")

    def test_validate_date_month_boundary_max(self):
        """Checks if month at upper boundary (12) return 'Valid Date'."""
        self.assertEqual(validate_date(2000, 12, 15), "Valid Date")

    def test_validate_date_day_boundary_min(self):
        """Checks if day at lower boundary (1) returns 'Valid Date'."""
        self.assertEqual(validate_date(2000, 5, 1), "Valid Date")

    def test_validate_date_day_boundary_max(self):
        """Checks if day at upper boundary (31) returns 'Valid Date. """
        self.assertEqual(validate_date(2000, 5, 31), "Valid Date")


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
