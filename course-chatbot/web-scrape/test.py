"""
Module for testing the web scraper.

Dependencies:
  - data.py: contains the article_text variable used in testing.

Tests:
  - TestArticleText: verifies that the required text is present in article_text.
  - ...
"""
import unittest
from data import article_text

# Define a test case class for verifying that the required text is present in article_text
class TestArticleText(unittest.TestCase):
    """
    Test case class for verifying that the required text is present in an article.
    Usage:
      - Instantiate the class wherever needed.
      - Call test_article_text() method to verify that article_text contains the required text.
    """

    def test_article_text(self):
        self.assertTrue('Amjad has a plan.' in article_text,
                    'missing text in article')

# If this script is being run directly, run the test case
if __name__ == '__main__':
  unittest.main()