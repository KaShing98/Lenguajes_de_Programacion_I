import unittest
from BuddySystem import BuddySystem

class VectorTests(unittest.TestCase):

    def test_allocate_success(self):
        a = BuddySystem(1024)
        self.assertEqual(a.Reservar("b", 512), "Block under name {} was reserved".format("b"))
        self.assertEqual(a.Reservar("c", 256), "Block under name {} was reserved".format("c"))
        self.assertEqual(a.Reservar("d", 256), "Block under name {} was reserved".format("d"))

    def test_unallocate_success(self):
        a = BuddySystem(1024)
        self.assertEqual(a.Reservar("b", 512), "Block under name {} was reserved".format("b"))
        self.assertEqual(a.Liberar("b"), "Block under name {} was free".format("b"))

    def test_unallocate_fail(self):
        a = BuddySystem(1024)
        self.assertEqual(a.Reservar("b", 512), "Block under name {} was reserved".format("b"))
        self.assertEqual(a.Liberar("b"), "Block under name {} was free".format("b"))
        self.assertEqual(a.Liberar("b"), "Block under name {} does not exists".format("b"))

    def test_print(self):
        a = BuddySystem(1024)
        self.assertEqual(a.Reservar("b", 512), "Block under name {} was reserved".format("b"))
        self.assertEqual(a.Reservar("c", 256), "Block under name {} was reserved".format("c"))
        self.assertEqual(a.Reservar("d", 256), "Block under name {} was reserved".format("d"))

        text  = "[USED] Name: b, Size: 512\n"
        text += "[USED] Name: c, Size: 256\n"
        text += "[USED] Name: d, Size: 256\n"
        self.assertEqual(a.Mostrar(), text)

    def test_allocate_same_name(self):
        a = BuddySystem(1024)
        self.assertEqual(a.Reservar("b", 512), "Block under name {} was reserved".format("b"))
        self.assertEqual(a.Reservar("b", 256), "Block under name {} was already reserved".format("b"))

    def test_not_enough_space(self):
        a = BuddySystem(512)
        self.assertEqual(a.Reservar("b", 1024), "Block under name {} cannot be reserved".format("b"))

    def test_allocate_success_multiple(self):
        a = BuddySystem(1024)
        self.assertEqual(a.Reservar("b", 512), "Block under name {} was reserved".format("b"))
        self.assertEqual(a.Reservar("c", 256), "Block under name {} was reserved".format("c"))
        self.assertEqual(a.Reservar("d", 128), "Block under name {} was reserved".format("d"))
        self.assertEqual(a.Reservar("df", 125), "Block under name {} was reserved".format("df"))

if __name__ == '__main__':
    unittest.main()