========
String-1
========


.. tabbed:: quiz1

    .. tab:: Ejercicio 1

        .. activecode:: q1_1_ees
            :nocodelens:

            Dado un entero count que representa el número de donuts, devuelve una cadena en la forma 'Número de donuts: <count>', donde <count> es el número pasado. Sin embargo, si count es 10 o más, entonces usa la palabra 'muchos' en lugar del número real. 

            ~~~~
            def donuts(count):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(donuts(4), 'Número de donuts: 4', "Esperado: 'Número de donuts: 4'")
                    self.assertEqual(donuts(9), 'Número de donuts: 9', "Esperado: 'Número de donuts: 9'")
                    self.assertEqual(donuts(10), 'Número de donuts: muchos', "Esperado: 'Número de donuts: muchos'")
                    self.assertEqual(donuts(99), 'Número de donuts: muchos', "Esperado: 'Número de donuts: muchos'")

            myTests().main()

    .. tab:: Ejercicio 2

        .. activecode:: q1_2_ees
            :nocodelens:

            Dada una cadena s, devuelve una cadena hecha de los dos primeros y los dos últimos caracteres de la cadena original, por lo que 'spring' produce 'spng'. Sin embargo, si la longitud de la cadena es menor que 2, devuelve en su lugar una cadena vacía. 

            ~~~~
            def both_ends(s):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(both_ends('spring'), 'spng', "Esperado: 'spng'")
                    self.assertEqual(both_ends('Hello'), 'Helo', "Esperado: 'Helo'")
                    self.assertEqual(both_ends('a'), '', "Esperado: ''")
                    self.assertEqual(both_ends('xyz'), 'xyyz', "Esperado: 'xyyz'")

            myTests().main()

    .. tab:: Ejercicio 3

        .. activecode:: q1_3_ees
            :nocodelens:

            Dada una cadena s, devuelve una cadena donde todas las ocurrencias de su primer carácter han sido cambiadas por '*', excepto el primer carácter en sí. 

            ~~~~
            def fix_start(s):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(fix_start('babble'), 'ba**le', "Esperado: 'ba**le'")
                    self.assertEqual(fix_start('aardvark'), 'a*rdv*rk', "Esperado: 'a*rdv*rk'")
                    self.assertEqual(fix_start('google'), 'goo*le', "Esperado: 'goo*le'")
                    self.assertEqual(fix_start('donut'), 'donut', "Esperado: 'donut'")

            myTests().main()

    .. tab:: Ejercicio 4

        .. activecode:: q1_4_ees
            :nocodelens:

            Dadas las cadenas a y b, devuelve una sola cadena con a y b separadas por un espacio '<a> <b>', excepto que intercambia los primeros 2 caracteres de cada cadena. 

            ~~~~
            def mix_up(a, b):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(mix_up('mix', 'pod'), 'pox mid', "Esperado: 'pox mid'")
                    self.assertEqual(mix_up('dog', 'dinner'), 'dig donner', "Esperado: 'dig donner'")
                    self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort', "Esperado: 'spash gnort'")
                    self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm', "Esperado: 'fizzy perm'")

            myTests().main()
