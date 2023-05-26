# File: tests/test_19_loop_exit.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake
from delta.semantics import SemanticMistake


class TestLoopExit(TestCase):

    def setUp(self):
        self.c = Compiler('program_start')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('loop {')

    def test_semantic_mistake1(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var loop; 0')

    def test_semantic_mistake2(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var exit; 0')

    def test_semantic_mistake3(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var when; 0')

    def test_loop_exit_zero(self):
        self.assertEqual(0,
                         self.c.realize(
                            '''
                            var x, y;
                            x = 1;
                            y = 0;
                            loop {
                                x = x - 1;
                                exit when !x;
                                y = 1;
                            }
                            x + y
                            '''))

    def test_loop_exit_fact(self):
        self.assertEqual(120,
                         self.c.realize(
                            '''
                            var n, r, i;
                            n = 5;
                            r = 1;
                            i = 0;
                            loop {
                                i = i + 1;
                                exit when !((n + 1) - i);
                                r = r * i;
                            }
                            r
                            '''))

    def test_loop_exit_count_down(self):
        self.assertEqual(0,
                         self.c.realize(
                            '''
                            var i;
                            i = 10;
                            loop {
                                exit when !i;
                                i = i - 1;
                            }
                            i
                            '''))

    def test_loop_exit_skip_body(self):
        self.assertEqual(9,
                         self.c.realize(
                            '''
                            var n;
                            n = 10;
                            loop {
                                n = n - 1;
                                if false {
                                } else {
                                    exit when n;
                                }
                            }
                            n
                            '''))

    def test_loop_exit_fibo(self):
        self.assertEqual(55,
                         self.c.realize(
                            '''
                            var n, a, b;
                            n = 10;
                            a = 0;
                            b = 1;
                            loop {
                                exit when !n;
                                var t;
                                t = b;
                                b = a + b;
                                a = t;
                                n = n - 1;
                            }
                            a
                            '''))

    def test_loop_exit_nested(self):
        self.assertEqual(1500,
                         self.c.realize(
                            '''
                            var r, i;
                            r = 0;
                            i = 10;
                            loop {
                                var j;
                                j = 50;
                                loop {
                                    var k;
                                    k = 3;
                                    loop {
                                        r = r + 1;
                                        k = k - 1;
                                        exit when !k;
                                    }
                                    j = j - 1;
                                    exit when !j;
                                }
                                i = i - 1;
                                exit when !i;
                            }
                            r
                            '''))

    def test_loop_exit_multiple_exits(self):
        self.assertEqual(9,
                         self.c.realize(
                            '''
                            var r, i;
                            r = 0;
                            i = 10;
                            loop {
                                i = i - 1;
                                if i {
                                    exit when !(i % 2);
                                } else {
                                    exit when true;
                                }
                                r = r + i;
                                exit when !i;
                            }
                            r
                            '''))
