======
List-1
======

.. tabbed:: quiz1

    .. tab:: Exercise 1

        .. activecode:: q1_1_reto8_
            :nocodelens:

            Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.

            ~~~~
            def match_ends(words):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3, "Expected: 3")
                    self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2, "Expected: 2")
                    self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1, "Expected: 1")

            myTests().main()

    .. tab:: Exercise 2

        .. activecode:: q1_2_cn
            :nocodelens:

            Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.

            ~~~~
            def front_x(words):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'], "Expected: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']")
                    self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'], "Expected: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']")
                    self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'], "Expected: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']")

            myTests().main()

    .. tab:: Exercise 3

        .. activecode:: q1_3_cn
            :nocodelens:

            Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple. 

            ~~~~
            def sort_last(tuples):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)], "Expected: [(2, 1), (3, 2), (1, 3)]")
                    self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)], "Expected: [(3, 1), (1, 2), (2, 3)]")
                    self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)], "Expected: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]")

            myTests().main()