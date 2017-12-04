import unittest
from libs.consulta import BooleanSearch

class BooleanSearchTest(unittest.TestCase):
    entradas = (
        ('sociedad', ["1"]),
        ('mexicano', False),
        ('sociedad boliviana niño', True),
        ('sociedad boliviana niño jose', False),
        ('sociedad boliviana niño jose franciscano', False),
        ('sociedad boliviana niño jose franciscano otros', False),
    )

    def test_prueba(self):
        # for entrada, homonimo in self.entradas:
        #     self.assertEqual(homonimo, ["1"], entrada)
        print("holas")
        # for entrada, homonimo in self.entradas:
        #     d = Diccionario(self.empresas)
        #     d.iniciar()
        #     b = Busqueda(entrada,d.palabras)
        #     b.iniciar()
        #     print("------------------------------------------------------")
        #     print(entrada)
        #     print(b.buscar_exacto(d)[["nombre","len_a","len_b","h__","h_a","h_b"]])
        #     self.assertEqual(any(b.buscar_exacto(d)["h__"]), homonimo, entrada)

if __name__ == '__main__':
    unittest.main()
