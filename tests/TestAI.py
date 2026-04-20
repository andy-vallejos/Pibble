import unittest
from src.AIClient import AIClient


class TestAIClient(unittest.TestCase):

    def setUp(self):
        self.ai = AIClient()

    def test_inicializacion(self):
        cliente, modelo = self.ai.iniciar()

        self.assertIsNotNone(cliente)
        self.assertIsNotNone(modelo)
        self.assertIsInstance(modelo, str)

    def test_singleton_interno(self):
        cliente1, modelo1 = self.ai.iniciar()
        cliente2, modelo2 = self.ai.iniciar()

        self.assertEqual(cliente1, cliente2)
        self.assertEqual(modelo1, modelo2)

    def test_modelo_valido(self):
        _, modelo = self.ai.iniciar()

        self.assertTrue(len(modelo) > 0)

if __name__ == "__main__":
    unittest.main()
