import unittest
from MemoryManager import REPL
import io
import sys

class VectorTests(unittest.TestCase):

    def test_eval_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 

        repl = REPL()
        repl.eval("RESERVAR hotel trivago")
        repl.eval("IMPRIMIR hotel")

        sys.stdout = sys.__stdout__ 
        assert(capturedOutput.getvalue() == "Asociated value to hotel is trivago\n")

    def test_eval_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 

        repl = REPL()
        repl.eval("RESERVAR hotel trivago")
        repl.eval("RESERVAR casa grande")
        repl.eval("ASIGNAR casa hotel")
        repl.eval("IMPRIMIR casa")

        sys.stdout = sys.__stdout__ 
        assert(capturedOutput.getvalue() == "Asociated value to casa is trivago\n")

    def test_eval_3(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 

        repl = REPL()
        repl.eval("RESERVAR hotel trivago")
        repl.eval("ASIGNAR casa hotel")

        sys.stdout = sys.__stdout__ 
        assert(capturedOutput.getvalue() == "Not declared: casa\n")

    def test_eval_4(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 

        repl = REPL()
        repl.eval("RESERVAR hotel trivago")
        repl.eval("LIBERAR hotel")
        repl.eval("IMPRIMIR hotel")

        sys.stdout = sys.__stdout__ 
        assert(capturedOutput.getvalue() == "hotel has no value associated\n")

    def test_eval_5(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 

        repl = REPL()
        repl.eval("LIBERAR hotel")

        sys.stdout = sys.__stdout__ 
        assert(capturedOutput.getvalue() == "Not declared: hotel\n")

    def test_eval_6(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput 

        repl = REPL()
        repl.eval("RESERVAR hotel trivago")
        repl.eval("RESERVAR casa grande")
        repl.eval("ASIGNAR casa hotel")
        repl.eval("RESERVAR hotel notTrivago")
        repl.eval("IMPRIMIR casa")

        sys.stdout = sys.__stdout__ 
        print(capturedOutput.getvalue())
        assert(capturedOutput.getvalue() == "Asociated value to casa is notTrivago\n")



if __name__ == '__main__':
    unittest.main()