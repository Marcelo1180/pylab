import unittest
from test.numeros.numero_texto_test import TestNumeroTexto
# from test.numeros.romanos_test import TestRomanos
# from test.numeros.texto_numeros_test import TestTextoNumero
# from test.consulta  import BooleanSearchTest
from test.buscar  import TestBuscarPalabras
from libs.buscar import BooleanSearch


if __name__ == '__main__':
    test_classes_to_run = [TestNumeroTexto, TestBuscarPalabras,]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)
    runner = unittest.TextTestRunner(verbosity=3)
    results = runner.run(big_suite)
