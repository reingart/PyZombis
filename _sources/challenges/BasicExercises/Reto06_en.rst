========
String-1
========


.. tabbed:: quiz1

    .. tab:: Exercise 1

        .. activecode:: q1_1_reto6_
            :nocodelens:

            Given an int count of a number of donuts, return a string of the form 'Number of donuts: <count>', where <count> is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count. 

            ~~~~
            def donuts(count):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(donuts(4), 'Number of donuts: 4', "Expected: 'Number of donuts: 4'")
                    self.assertEqual(donuts(9), 'Number of donuts: 9', "Expected: 'Number of donuts: 9'")
                    self.assertEqual(donuts(10), 'Number of donuts: many', "Expected: 'Number of donuts: many'")
                    self.assertEqual(donuts(99), 'Number of donuts: many', "Expected: 'Number of donuts: many'")

            myTests().main()

    .. tab:: Exercise 2

        .. activecode:: q1_2_an
            :nocodelens:

            Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than 2, return instead the empty string.

            ~~~~
            def both_ends(s):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(both_ends('spring'), 'spng', "Expected: 'spng'")
                    self.assertEqual(both_ends('Hello'), 'Helo', "Expected: 'Helo'")
                    self.assertEqual(both_ends('a'), '', "Expected: ''")
                    self.assertEqual(both_ends('xyz'), 'xyyz', "Expected: 'xyyz'")

            myTests().main()

    .. tab:: Exercise 3

        .. activecode:: q1_3_an
            :nocodelens:

            Given a string s, return a string where all occurrences of its first char have been changed to '*', except do not change the first char itself. 

            ~~~~
            def fix_start(s):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(fix_start('babble'), 'ba**le', "Expected: 'ba**le'")
                    self.assertEqual(fix_start('aardvark'), 'a*rdv*rk', "Expected: 'a*rdv*rk'")
                    self.assertEqual(fix_start('google'), 'goo*le', "Expected: 'goo*le'")
                    self.assertEqual(fix_start('donut'), 'donut', "Expected: 'donut'")

            myTests().main()

    .. tab:: Exercise 4

        .. activecode:: q1_4_an
            :nocodelens:

            Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap the first 2 chars of each string. 

            ~~~~
            def mix_up(a, b):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(mix_up('mix', 'pod'), 'pox mid', "Expected: 'pox mid'")
                    self.assertEqual(mix_up('dog', 'dinner'), 'dig donner', "Expected: 'dig donner'")
                    self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort', "Expected: 'spash gnort'")
                    self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm', "Expected: 'fizzy perm'")

            myTests().main()

