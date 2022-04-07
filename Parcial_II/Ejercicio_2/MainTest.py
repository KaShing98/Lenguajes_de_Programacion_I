import unittest
from Main import REPL

class VectorTests(unittest.TestCase):

    def test_eval_1(self):
        repl = REPL()
        ans = repl.parser.eval("PRE", "+ 1 2")
        assert(ans == 3)

    def test_eval_2(self):
        repl = REPL()
        ans = repl.parser.eval("PRE", "+ * + 3 4 5 7")
        assert(ans == 42)

    def test_eval_3(self):
        repl = REPL()
        ans = repl.parser.eval("POST", "1 2 +")
        assert(ans == 3)

    def test_eval_4(self):
        repl = REPL()
        ans = repl.parser.eval("POST", "8 3 - 8 4 4 + * +")
        assert(ans == 69)

    def test_eval_5(self):
        repl = REPL()
        try:
            repl.parser.eval("PRE", "")
            assert(False)
        except:
            assert(True)

    def test_eval_5(self):
        repl = REPL()
        try:
            repl.parser.eval("POST", "")
            assert(False)
        except:
            assert(True)

    def test_eval_6(self):
        repl = REPL()
        ans = repl.parser.show("PRE", "+ * + 3 4 5 7")
        assert(ans == "(3 + 4) * 5 + 7")

    def test_eval_7(self):
        repl = REPL()
        ans = repl.parser.show("POST", "8 3 - 8 4 4 + * +")
        assert(ans == "8 - 3 + 8 * (4 + 4)")

    def test_eval_8(self):
        repl = REPL()
        ans = repl.eval("EVAL POST 8 3 - 8 4 4 + * +")
        assert(ans == 69)

    def test_eval_9(self):
        repl = REPL()
        ans = repl.eval("EVAL POST 8 (3) -")
        assert(ans == 5)

if __name__ == '__main__':
    unittest.main()