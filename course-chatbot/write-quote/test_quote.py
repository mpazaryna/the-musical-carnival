"""
test_quotes.py

This module contains unit tests for a "quote.txt" file. The file should include a quote by Victor Frankl.

"""

import unittest
import os


class TestQuoteFile(unittest.TestCase):

  def setUp(self):
    self.filename = "quotes.txt"

  def test_quote_file_exists(self):
    self.assertTrue(os.path.exists(self.filename))

  def test_quote_is_correct_author(self):
    with open(self.filename, "r") as file:
      content = file.read()
    self.assertIn("Victor Flubba", content)

  def test_quote_is_non_empty(self):
    with open(self.filename, "r") as file:
      content = file.read()
    self.assertGreater(len(content), 0)
