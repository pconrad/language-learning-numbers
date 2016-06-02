#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Why -*- coding: utf-8 -*- ? See: http://python.org/dev/peps/pep-0263/ 

import language_learning_numbers as lln
import unittest

class TestLanguageLearningNumbers(unittest.TestCase):

    def test_expect_languages_supported_to_return_a_list(self):
        languages = lln.languages_supported()
        self.assertIsInstance(languages,list)

    def test_expect_Spanish_to_be_supported(self):
        languages = lln.languages_supported()
        self.assertIn("Spanish",languages)

    def test_expect_limit_for_Spanish_to_be_an_int(self):
        self.assertIsInstance(lln.limit("Spanish"),int)

    def test_expect_limit_for_Spanish_to_be_ge_10(self):
        self.assertGreaterEqual(lln.limit("Spanish"),10)


if __name__ == "__main__":
    unittest.main()
