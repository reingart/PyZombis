========
String-2
========


.. tabbed:: quiz2

    .. tab:: Exercise 1

        .. activecode:: q2_1_reto7_
            :nocodelens:

            Given a string, if its length is at least 3, add 'ing' to its end. Unless it already ends in 'ing', in which case add 'ly' instead. If the string length is less than 3, leave it unchanged. Return the resulting string.

            ~~~~
            def verbing(s):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(verbing('hail'), 'hailing', "Expected: 'hailing'")
                    self.assertEqual(verbing('swiming'), 'swimingly', "Expected: 'swimingly'")
                    self.assertEqual(verbing('do'), 'do', "Expected: 'do'")

            myTests().main()

    .. tab:: Exercise 2

        .. activecode:: q2_2_bn
            :nocodelens:

            Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'. Return the resulting string. So 'This dinner is not that bad!' yields: 'This dinner is good!' 

            ~~~~
            def not_bad(s):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good', "Expected: 'This movie is good'")
                    self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!', "Expected: 'This dinner is good!'")
                    self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot', "Expected: 'This tea is not hot'")
                    self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not", "Expected: 'It's bad yet not'")

            myTests().main()

    .. tab:: Exercise 3

        .. activecode:: q2_3_bn
            :nocodelens:

            Consider dividing a string into two halves. If the length is even, the front and back halves are the same length. If the length is odd, we'll say that the extra char goes in the front half. e.g. 'abcde', the front half is 'abc', the back half 'de'. Given 2 strings, a and b, return a string of the form a-front + b-front + a-back + b-back. 

            ~~~~
            def front_back(a, b):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy', "Expected: 'abxcdy'")
                    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez', "Expected: 'abcxydez'")
                    self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut', "Expected: 'KitDontenut'")

            myTests().main()