import ast
import unittest

import asttest

class TestFindIndex(asttest.ASTTest):

    def setUp(self):
        super().setUp("find_index.py")

    def test_required_syntax(self):
        pass

    def test_correct_result(self):
        self.exec_solution()

if __name__ == "__main__":
    unittest.main()
