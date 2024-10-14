=========================
Python Wordcount Exercise
=========================


.. tabbed:: quiz3

    .. tab:: Exercise 1

        .. activecode:: q3_1_reto10_
            :nocodelens:

            For the --count flag, implement a print_words(filename) function that counts how often each word appears in the text and prints: word1 count1, word2 count2, ... Print the above list in order sorted by word (python will sort punctuation to come before letters -- that's fine). Store all the words as lowercase, so 'The' and 'the' count as the same word. 

            ~~~~
            def print_words(filename):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                # Add your tests here
                pass

            myTests().main()

    .. tab:: Exercise 2

        .. activecode:: q3_2_wcn
            :nocodelens:

            For the --topcount flag, implement a print_top(filename) which is similar to print_words() but which prints just the top 20 most common words sorted so the most common word is first, then the next most common, and so on. 

            ~~~~
            def print_top(filename):
                # +++your code here+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                # Add your tests here
                pass

            myTests().main()