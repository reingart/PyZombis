======
List-2
======

.. tabbed:: quiz2

    .. tab:: Ejercicio 1

        .. activecode:: q2_1_rrn
            :nocodelens:

            Dada una lista de números, devuelve una lista donde todos los elementos adyacentes iguales se han reducido a un solo elemento, por lo que [1, 2, 2, 3] devuelve [1, 2, 3]. Puedes crear una nueva lista o modificar la lista pasada como argumento. 

            ~~~~
            def remove_adjacent(nums):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3], "Esperado: [1, 2, 3]")
                    self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3], "Esperado: [2, 3]")
                    self.assertEqual(remove_adjacent([]), [], "Esperado: []")

            myTests().main()

    .. tab:: Ejercicio 2

        .. activecode:: q2_2_rrn
            :nocodelens:

            Dadas dos listas ordenadas en orden creciente, crea y devuelve una lista fusionada de todos los elementos en orden ordenado. Puedes modificar las listas pasadas como argumento. Idealmente, la solución debería funcionar en tiempo "lineal", haciendo un solo recorrido de ambas listas.

            ~~~~
            def linear_merge(list1, list2):
                # +++tu código aquí+++
                return
            

            ====
            from unittest.gui import TestCaseGui

            class myTests(TestCaseGui):
                def testOne(self):
                    self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'], "Esperado: ['aa', 'bb', 'cc', 'xx', 'zz']")
                    self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'], "Esperado: ['aa', 'bb', 'cc', 'xx', 'zz']")
                    self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'], "Esperado: ['aa', 'aa', 'aa', 'bb', 'bb']")

            myTests().main()
