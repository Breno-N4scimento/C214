import unittest
from unittest.mock import MagicMock
import json
import os
from main import HorarioAtendimentoService, BuscaHorario


class TestBuscaHorario(unittest.TestCase):
    def setUp(self):
        # cria um mock para HorarioAtendimentoService
        self.serviceMock = MagicMock()
        self.busca_horario = BuscaHorario(self.serviceMock)

    # Testes de Sucesso
    def testAcerto1(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Chris",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "integral",
            "sala": "3",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(1)
        self.assertEqual(horario.nome, "Chris")

    def testAcerto2(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Renzo",
            "horarioDeAtendimento": "14:00-16:00",
            "periodo": "noturno",
            "sala": "7",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(2)
        self.assertEqual(horario.horario, "14:00-16:00")

    def testAcerto3(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Marcelo",
            "horarioDeAtendimento": "13:00-14:00",
            "periodo": "integral",
            "sala": "6",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(3)
        self.assertEqual(horario.periodo, "integral")

    def testAcerto4(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Jonas",
            "horarioDeAtendimento": "17:00-19:00",
            "periodo": "integral",
            "sala": "2",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(5)
        self.assertEqual(horario.nome, "Jonas")

    def testAcerto5(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Chris",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "integral",
            "sala": "1",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(1)
        self.assertEqual(horario.sala, "1")

    def testAcerto6(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Renzo",
            "horarioDeAtendimento": "14:00-16:00",
            "periodo": "noturno",
            "sala": "7",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(2)
        self.assertEqual(horario.predio, 2)

    def testAcerto7(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Marcelo",
            "horarioDeAtendimento": "13:00-14:00",
            "periodo": "integral",
            "sala": "5",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(3)
        self.assertEqual(horario.horario, "13:00-14:00")

    def testAcerto8(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Ynoguti",
            "horarioDeAtendimento": "15:00-17:00",
            "periodo": "noturno",
            "sala": "10",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(4)
        self.assertEqual(horario.periodo, "noturno")

    def testAcerto9(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Jonas",
            "horarioDeAtendimento": "17:00-19:00",
            "periodo": "integral",
            "sala": "12",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(5)
        self.assertEqual(horario.predio, 3)

    def testAcerto10(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Chris",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "integral",
            "sala": "3",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(1)
        self.assertEqual(horario.sala, "3")

    '''-----------------------------------------------------------'''

    # Teste erro
    def testErro1(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Renzo",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "integral",
            "sala": "3",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(1)
        self.assertNotEqual(horario.nome, "Renzo")

    def testErro2(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Renzo",
            "horarioDeAtendimento": "14:00-16:00",
            "periodo": "integral",
            "sala": "7",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(2)
        self.assertNotEqual(horario.horario, "14:00-16:00")  # Espera falha, pois o horário é 14:00-16:00"

    def testErro3(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Marcelo",
            "horarioDeAtendimento": "13:00-17:00",
            "periodo": "integral",
            "sala": "6",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(3)
        self.assertNotEqual(horario.periodo, "integral")  # Espera falha, pois o período é "integral"

    def testErro4(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Jonas",
            "horarioDeAtendimento": "17:00-19:00",
            "periodo": "integral",
            "sala": "8",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(5)
        self.assertNotEqual(horario.nome, "Jonas")

    def testErro5(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Jonas",
            "horarioDeAtendimento": "17:00-19:00",
            "periodo": "integral",
            "sala": "2",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(5)
        self.assertNotEqual(horario.nome, "Jonas")  # Espera falha, pois o nome é "Jonas"

    def testErro6(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Chris",
            "horarioDeAtendimento": "09:00-12:00",
            "periodo": "integral",
            "sala": "1",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(1)
        self.assertNotEqual(horario.sala, "1")  # Espera falha, pois a sala é "1"

    def testErro7(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Marcelo",
            "horarioDeAtendimento": "13:00-14:00",
            "periodo": "noturno",
            "sala": "5",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(5)
        self.assertEqual(horario.horario, "13:00-17:00")

    def testErro8(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Marcelo",
            "horarioDeAtendimento": "13:00-14:00",
            "periodo": "noturno",
            "sala": "5",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(3)
        self.assertNotEqual(horario.horario, "13:00-14:00")  # Espera falha, pois o horário é "13:00-14:00"

    def testErro9(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Chris",
            "horarioDeAtendimento": "15:00-17:00",
            "periodo": "noturno",
            "sala": "10",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(4)
        self.assertNotEqual(horario.periodo, "noturno")  # Espera falha, pois o período é "noturno"

    def testErro10(self):
        self.serviceMock.busca.return_value = json.dumps({
            "nomeDoProfessor": "Jonas",
            "horarioDeAtendimento": "17:00-19:00",
            "periodo": "integral",
            "sala": "12",
            "predio": ["1", "2", "3", "4", "6"]
        })
        horario = self.busca_horario.busca_horario(5)
        self.assertNotEqual(horario.nome, "Jonas")

    def geraJson(self):
        horario1 = {
            "nomeDoProfessor": "Chris",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "integral",
            "sala": "3",
            "predio": ["1", "2", "3", "4", "6"]
        }

        if not os.path.isdir("./horario1"):
            os.makedirs("./horario1")

        with open("./horario1/horario.json", 'w') as json_file:
            json.dump(horario1, json_file, indent=4, separators=(',', ': '))


if __name__ == "__main__":
    unittest.main()
