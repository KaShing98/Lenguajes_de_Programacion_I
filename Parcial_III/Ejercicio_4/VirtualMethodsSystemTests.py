import io
import sys
import unittest
from REPL import REPL

class VectorTests(unittest.TestCase):

    def test_eval_1(self):
        repl = REPL()
        ans = repl.eval("DESCRIBIR A")

        assert(ans == "ERROR: DESCRIBIR A ==> La clase A no se encuentra en el sistema.")

    def test_eval_2(self):
        repl = REPL()
        ans = repl.eval("CLASS A f g")
        ans = repl.eval("DESCRIBIR A")
        
        assert(ans == "f -> A :: f\ng -> A :: g")

    def test_eval_3(self):
        repl = REPL()
        ans = repl.eval("CLASS B : A f h")

        assert(ans == "ERROR: CLASS B : A f h ==> La super clase A no se encuentra en el sistema.")

    def test_eval_4(self):
        repl = REPL()
        ans = repl.eval("CLASS A f g")
        ans = repl.eval("CLASS B : A f h")
        ans = repl.eval("DESCRIBIR B")

        assert(ans == "f -> B :: f\ng -> A :: g\nh -> B :: h")

    def test_eval_6(self):
        repl = REPL()
        ans = repl.eval("CLASS A f g")
        ans = repl.eval("CLASS A k o")

        assert(ans == "ERROR: CLASS A k o ==> La clase A ya se encuentra en el sistema.")

    def test_eval_7(self):
        repl = REPL()
        ans = repl.eval("CLASS A f g j k km lk f")

        assert(ans == "ERROR: CLASS A f g j k km lk f ==> La declaración contiene métodos repetidos.")

if __name__ == '__main__':
    unittest.main()