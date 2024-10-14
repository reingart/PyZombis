========
String-2
========

.. tabbed:: quiz2

    .. tab:: Ejercicio 1

        .. activecode:: q2_1_hes
            :nocodelens:

            Dada una cadena, si su longitud es al menos 3, agrega 'ing' al final. A menos que ya termine en 'ing', en cuyo caso agrega 'ly' en su lugar. Si la longitud de la cadena es menor que 3, déjala sin cambios. Devuelve la cadena resultante.

            ~~~~
            def verbing(s):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(verbing('saludo'), 'saludando', "Esperado: 'saludando'")
                    self.assertEqual(verbing('nadando'), 'nadando', "Esperado: 'nadando'")
                    self.assertEqual(verbing('ir'), 'ir', "Esperado: 'ir'")

            myTests().main()

    .. tab:: Ejercicio 2

        .. activecode:: q2_2_hes
            :nocodelens:

            Dada una cadena, encuentra la primera aparición de la subcadena 'not' y 'bad'. Si 'bad' sigue a 'not', reemplaza toda la subcadena 'not'...'bad' con 'bueno'. Devuelve la cadena resultante. Entonces '¡Esta cena no es tan mala!' produce: '¡Esta cena es buena!'

            ~~~~
            def not_bad(s):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(not_bad('Esta película no está tan mal'), 'Esta película es buena', "Esperado: 'Esta película es buena'")
                    self.assertEqual(not_bad('Esta cena no es tan mala!'), 'Esta cena es buena!', "Esperado: 'Esta cena es buena!'")
                    self.assertEqual(not_bad('Este té no está caliente'), 'Este té no está caliente', "Esperado: 'Este té no está caliente'")
                    self.assertEqual(not_bad("Es malo pero no"), "Es malo pero no", "Esperado: 'Es malo pero no'")

            myTests().main()

    .. tab:: Ejercicio 3

        .. activecode:: q2_3_hes
            :nocodelens:

            Considera dividir una cadena en dos mitades. Si la longitud es par, las mitades delanteras y traseras tienen la misma longitud. Si la longitud es impar, diremos que el carácter extra va en la mitad delantera. Por ejemplo, 'abcde', la mitad delantera es 'abc', la mitad trasera 'de'. Dadas 2 cadenas, a y b, devuelve una cadena de la forma a-mitad-delantera + b-mitad-delantera + a-mitad-trasera + b-mitad-trasera.

            ~~~~
            def front_back(a, b):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy', "Esperado: 'abxcdy'")
                    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez', "Esperado: 'abcxydez'")
                    self.assertEqual(front_back('Gatito', 'Rosquilla'), 'GatRosquitinilloa', "Esperado: 'GatRosquitinilloa'")

            myTests().main()
