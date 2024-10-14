======
List-2
======

.. tabbed:: quiz2

    .. tab:: Exercise 1

        .. activecode:: q2_1_reto9_
            :nocodelens:

            Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list. 

            ~~~~
            def remove_adjacent(nums):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3], "Expected: [1, 2, 3]")
                    self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3], "Expected: [2, 3]")
                    self.assertEqual(remove_adjacent([]), [], "Expected: []")

            myTests().main()

    .. tab:: Exercise 2

        .. activecode:: q2_2_dn
            :nocodelens:

            Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order. You may modify the passed in lists. Ideally, the solution should work in "linear" time, making a single pass of both lists.

            ~~~~
            def linear_merge(list1, list2):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'], "Expected: ['aa', 'bb', 'cc', 'xx', 'zz']")
                    self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'], "Expected: ['aa', 'bb', 'cc', 'xx', 'zz']")
                    self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'], "Expected: ['aa', 'aa', 'aa', 'bb', 'bb']")

            myTests().main()