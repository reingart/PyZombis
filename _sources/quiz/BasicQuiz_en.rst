===============
Basic Exercises
===============

+  Basic Exercises from Google's Python Class

.. |br| raw:: html

    <br />


.. tabbed:: basicExercises

    .. tab:: Exercise 1

        .. activecode:: basic_q1
            :nocodelens:

            Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first. For example: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'] |br|
            
            ~~~~
            def front_x(words):

            ====

            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'], "Expected: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']")
                    self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'], "Expected: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']")
                    self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'], "Expected: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']")

            myTests().main()



    .. tab:: Exercise 2

        .. activecode:: basic_q2
            :nocodelens:

            Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same. |br|

            ~~~~
            def match_ends(words):


            ====
            from unittest.gui import TestCaseGui

            class MyTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3, "Expected: 3")
                    self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2, "Expected: 2")
                    self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1, "Expected: 1")

            MyTests().main()


    .. tab:: Exercise 3

        .. activecode:: basic_q3
            :nocodelens:

            Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple. |br|

            ~~~~
            # Extract the last element from a tuple -- used for custom sorting below.
            def last(a):
            
            def sort_last(tuples):

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)], "Expected: [(2, 1), (3, 2), (1, 3)]")
                    self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)], "Expected: [(3, 1), (1, 2), (2, 3)]")
                    self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)], "Expected: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]")

            myTests().main()



    .. tab:: Exercise 4

        .. activecode:: basic_q4
            :nocodelens:

            Given an int count of a number of donuts, return a string of the form 'Number of donuts: <count>', where <count> is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count. |br|

            ~~~~
            def donuts(count):

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(donuts(4), 'Number of donuts: 4', "Expected: 'Number of donuts: 4'")
                    self.assertEqual(donuts(9), 'Number of donuts: 9', "Expected: 'Number of donuts: 9'")
                    self.assertEqual(donuts(10), 'Number of donuts: many', "Expected: 'Number of donuts: many'")
                    self.assertEqual(donuts(99), 'Number of donuts: many', "Expected: 'Number of donuts: many'")

            myTests().main()



    .. tab:: Exercise 5

        .. activecode:: basic_q5
            :nocodelens:

            Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than 2, return instead the empty string. |br|

            ~~~~
            def both_ends(s):

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(both_ends('spring'), 'spng', "Expected: 'spng'")
                    self.assertEqual(both_ends('Hello'), 'Helo', "Expected: 'Helo'")
                    self.assertEqual(both_ends('a'), '', "Expected: ''")
                    self.assertEqual(both_ends('xyz'), 'xyyz', "Expected: 'xyyz'")

            myTests().main()




    .. tab:: Exercise 6

        .. activecode:: basic_q6
            :nocodelens:

            Given a string s, return a string where all occurrences of its first char have been changed to '*', except do not change the first char itself. For example, 'babble' yields 'ba**le'. Assume that the string is length 1 or more. |br|

            ~~~~
            def fix_start(s):

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(fix_start('babble'), 'ba**le', "Expected: 'ba**le'")
                    self.assertEqual(fix_start('aardvark'), 'a*rdv*rk', "Expected: 'a*rdv*rk'")
                    self.assertEqual(fix_start('google'), 'goo*le', "Expected: 'goo*le'")
                    self.assertEqual(fix_start('donut'), 'donut', "Expected: 'donut'")

            myTests().main()



    .. tab:: Exercise 7

        .. activecode:: basic_q7
            :nocodelens:

            Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap the first 2 chars of each string. |br|

            ~~~~
            def mix_up(a, b):

            ====    
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(mix_up('mix', 'pod'), 'pox mid', "Expected: 'pox mid'")
                    self.assertEqual(mix_up('dog', 'dinner'), 'dig donner', "Expected: 'dig donner'")
                    self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort', "Expected: 'spash gnort'")
                    self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm', "Expected: 'fizzy perm'")

            myTests().main()
