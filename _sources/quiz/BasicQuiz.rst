==================
Ejercicios básicos
==================

+  Ejercicios básicos de la clase de Python de Google

.. |br| raw:: html

    <br />


.. tabbed:: basicExercises

    .. tab:: Ejercicio 1

        .. activecode:: basic_q1es
            :nocodelens:

            Dada una lista de cadenas, devuelve una lista con las cadenas en orden ordenado, excepto agrupa todas las cadenas que comienzan con 'x' primero. Por ejemplo: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] produce ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'] |br|
            
            ~~~~
            def front_x(words):

            ====

            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'], "Esperado: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']")
                    self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'], "Esperado: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']")
                    self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'], "Esperado: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']")

            myTests().main()



    .. tab:: Ejercicio 2

        .. activecode:: basic_q2es
            :nocodelens:

            Dada una lista de cadenas, devuelve el recuento del número de cadenas donde la longitud de la cadena es 2 o más y el primer y último caracteres de la cadena son iguales. |br|

            ~~~~
            def match_ends(words):


            ====
            from unittest.gui import TestCaseGui

            class MyTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3, "Esperado: 3")
                    self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2, "Esperado: 2")
                    self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1, "Esperado: 1")

            MyTests().main()


    .. tab:: Ejercicio 3

        .. activecode:: basic_q3es
            :nocodelens:

            Dada una lista de tuplas no vacías, devuelve una lista ordenada en orden creciente por el último elemento en cada tupla. |br|

            ~~~~
            # Extraer el último elemento de una tupla, utilizado para ordenación personalizada a continuación
            def last(a):

            def sort_last(tuples):

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)], "Esperado: [(2, 1), (3, 2), (1, 3)]")
                    self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)], "Esperado: [(3, 1), (1, 2), (2, 3)]")
                    self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)], "Esperado: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]")

            myTests().main()



    .. tab:: Ejercicio 4

        .. activecode:: basic_q4es
            :nocodelens:

            Dado un entero que representa el número de donuts, devuelve una cadena de la forma 'Número de donuts: <count>', donde <count> es el número pasado. Sin embargo, si el recuento es 10 o más, use la palabra 'muchos' en lugar del recuento real. |br|

            ~~~~
            def donuts(count):

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(donuts(4), 'Número de donuts: 4', "Esperado: 'Número de donuts: 4'")
                    self.assertEqual(donuts(9), 'Número de donuts: 9', "Esperado: 'Número de donuts: 9'")
                    self.assertEqual(donuts(10), 'Número de donuts: muchos', "Esperado: 'Número de donuts: muchos'")
                    self.assertEqual(donuts(99), 'Número de donuts: muchos', "Esperado: 'Número de donuts: muchos'")

            myTests().main()



    .. tab:: Ejercicio 5

        .. activecode:: basic_q5es
            :nocodelens:

            Dada una cadena s, devuelve una cadena hecha de los primeros 2 y los últimos 2 caracteres de la cadena original, por lo que 'spring' produce 'spng'. Sin embargo, si la longitud de la cadena es menor que 2, devuelva en su lugar la cadena vacía. |br|

            ~~~~
            def both_ends(s):

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(both_ends('spring'), 'spng', "Esperado: 'spng'")
                    self.assertEqual(both_ends('Hello'), 'Helo', "Esperado: 'Helo'")
                    self.assertEqual(both_ends('a'), '', "Esperado: ''")
                    self.assertEqual(both_ends('xyz'), 'xyyz', "Esperado: 'xyyz'")

            myTests().main()




    .. tab:: Ejercicio 6

        .. activecode:: basic_q6es
            :nocodelens:

            Dada una cadenas, devuelve una cadena donde todas las ocurrencias de su primer carácter se han cambiado a '*', excepto no cambie el primer carácter en sí. Por ejemplo, 'babble' produce 'ba**le'. Suponga que la cadena tiene una longitud de 1 o más. |br|

            ~~~~
            def fix_start(s):

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(fix_start('babble'), 'ba**le', "Esperado: 'ba**le'")
                    self.assertEqual(fix_start('aardvark'), 'a*rdv*rk', "Esperado: 'a*rdv*rk'")
                    self.assertEqual(fix_start('google'), 'goo*le', "Esperado: 'goo*le'")
                    self.assertEqual(fix_start('donut'), 'donut', "Esperado: 'donut'")

            myTests().main()



    .. tab:: Ejercicio 7

        .. activecode:: basic_q7es
            :nocodelens:

            Dadas las cadenas a y b, devuelve una sola cadena con a y b separadas por un espacio '<a> <b>', excepto que intercambie los dos primeros caracteres de cada cadena. |br|

            ~~~~
            def mix_up(a, b):

            ====    
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(mix_up('mix', 'pod'), 'pox mid', "Esperado: 'pox mid'")
                    self.assertEqual(mix_up('dog', 'dinner'), 'dig donner', "Esperado: 'dig donner'")
                    self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort', "Esperado: 'spash gnort'")
                    self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm', "Esperado: 'fizzy perm'")

            myTests().main()
