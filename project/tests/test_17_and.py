# File: tests/test_17_and.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake


class TestAnd(TestCase):

    def setUp(self):
        self.c = Compiler('program_start')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('1 &&')

    def test_and1(self):
        self.assertEqual(1,
                         self.c.realize('true && true'))

    def test_and2(self):
        self.assertEqual(0,
                         self.c.realize('true && false'))

    def test_and3(self):
        self.assertEqual(0,
                         self.c.realize('false && true'))

    def test_and4(self):
        self.assertEqual(0,
                         self.c.realize('false && false'))

    def test_and5(self):
        self.assertEqual(1,
                         self.c.realize('1 && 2 && 3 && 4 && 5'))

    def test_and6(self):
        self.assertEqual(0,
                         self.c.realize('1 && 2 && 0 && 4 && 5'))

    def test_and7(self):
        self.assertEqual(0,
                         self.c.realize('!1 && !2 && !3'))

    def test_and8(self):
        self.assertEqual(1,
                         self.c.realize('!!1 && !!2 && !!3'))

    def test_and9(self):
        self.assertEqual(0,
                         self.c.realize('3 * 4 && 8 - 4 * 2'))

    def test_and10(self):
        self.assertEqual(1,
                         self.c.realize('3 * 4 && !(8 - 4 * 2)'))
