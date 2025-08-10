import ast
import unittest

import asttest

class InputHelper(asttest.ASTTest):

    def replace_input(self, text):
        self.input_text = text.split("\n")
        self.input_line = 0
    
    def input_replacement(self,prompt=""):
        self.input_line += 1
        try:
            self.input_text[self.input_line-1]
        except:
            raise Exception("Input Exhausted - your code is asking for input but the grader doesn't have more")
        return self.input_text[self.input_line-1]
    def exec_solution(self):
        """Executes the student submission."""
        print = self.print_replacement
        input=self.input_replacement
        self.printed_lines=[]
        exec(self.file,{"print":print,"input":input})