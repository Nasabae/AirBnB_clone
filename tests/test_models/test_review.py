#!/usr/bin/python3
"""
Tests for Review Module
"""

import unittest
import pep8
from datetime import datetime
from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    """Unit Tests"""

    def setUp(self):
        self.review = Review()

    def test_place_id(self):
        """
        1. tests if the place_id attribute of the
           Review object is an instance of the str class
        2. tests if  the place_id attribute has the value of an empty string
        """
        self.assertIsInstance(self.review.place_id, str)
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        """
        1. test if the user_id attribute of the
           Review object is an instance of the str class
        2. test if the user_id attribute has the value of an empty string
        """
        self.assertIsInstance(self.review.user_id, str)
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        """
        1. test if the text attribute of the
           Review object is an instance of the str class
        2. test if the text attribute has the value of an empty string
        """
        self.assertIsInstance(self.review.text, str)
        self.assertEqual(self.review.text, "")

    def test_review_pep8(self):
        """test if review.py is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        """test if this file is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
    unittest.main()
