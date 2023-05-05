# File: tests/test_16_for.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake
from delta.semantics import SemanticMistake


class TestFor(TestCase):

    def setUp(self):
        self.c = Compiler('program_start')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('for i = 1 upto {}')

    def test_semantic_mistake1(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var for; 0')

    def test_semantic_mistake2(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var upto; 0')

    def test_semantic_mistake3(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var downto; 0')

    def test_for_fact(self):
        self.assertEqual(120,
                         self.c.realize(
                            '''
                            var r, i;
                            r = 1;
                            for i = 1 upto 5  {
                                r = r * i;
                            }
                            r
                            '''))

    def test_for_count_down(self):
        self.assertEqual(0,
                         self.c.realize(
                            '''
                            var i;
                            for i = 10 downto 1 {
                            }
                            i
                            '''))

    def test_for_skip_body(self):
        self.assertEqual(0,
                         self.c.realize(
                            '''
                            var i, s;
                            s = 0;
                            for i = 10 upto 1 {
                                s = s + 1;
                            }
                            s
                            '''))

    def test_for_fibo(self):
        self.assertEqual(55,
                         self.c.realize(
                            '''
                            var n, a, b, i;
                            n = 10;
                            a = 0;
                            b = 1;
                            for i = 0 upto n - 1 {
                                var t;
                                t = b;
                                b = a + b;
                                a = t;
                            }
                            a
                            '''))

    def test_for_nested(self):
        self.assertEqual(1500,
                         self.c.realize(
                            '''
                            var r, i, j, k;
                            r = 0;
                            for i = 1 upto 10 {
                                for j = 50 downto 1 {
                                    for k = 1 upto 3 {
                                        r = r + 1;
                                    }
                                }
                            }
                            r
                            '''))
