======
List-1
======

.. tabbed:: quiz1

    .. tab:: Ejercicio 1

        .. activecode:: q1_1_lln
            :nocodelens:

            Dada una lista de cadenas, devuelve el recuento del número de cadenas donde la longitud de la cadena es de 2 o más y los primeros y últimos caracteres de la cadena son iguales. 

            ~~~~
            def match_ends(words):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3, "Esperado: 3")
                    self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2, "Esperado: 2")
                    self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1, "Esperado: 1")

            myTests().main()

    .. tab:: Ejercicio 2

        .. activecode:: q1_2_lln
            :nocodelens:

            Dada una lista de cadenas, devuelve una lista con las cadenas en orden ordenado, excepto agrupa todas las cadenas que comienzan con 'x' primero.

            ~~~~
            def front_x(words):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'], "Esperado: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']")
                    self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'], "Esperado: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']")
                    self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'], "Esperado: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']")

            myTests().main()

    .. tab:: Ejercicio 3

        .. activecode:: q1_3_lln
            :nocodelens:

            Dada una lista de tuplas no vacías, devuelve una lista ordenada en orden creciente por el último elemento de cada tupla.

            ~~~~
            def sort_last(tuples):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)], "Esperado: [(2, 1), (3, 2), (1, 3)]")
                    self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)], "Esperado: [(3, 1), (1, 2), (2, 3)]")
                    self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)], "Esperado: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]")

            myTests().main()
