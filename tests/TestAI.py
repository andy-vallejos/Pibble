import unittest

from src.AIClient import AIClient


class TestAIClient(unittest.TestCase):

    def setUp(self):
        self.ai = AIClient()
        self.ai.iniciar()

    def test_inicializacion(self):
        self.assertIsNotNone(self.ai.get_cliente())
        self.assertIsNotNone(self.ai.get_modelo())
        self.assertIsInstance(self.ai.get_modelo(), str)

    def test_modelo_valido(self):
        self.assertTrue(len(self.ai.get_modelo()) > 0)

    def test_generar_respuesta(self):
        self.assertTrue(isinstance(self.ai.generar_respuesta("Dime algo"), dict))


if __name__ == "__main__":
    unittest.main()
