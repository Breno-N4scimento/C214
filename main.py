import json


class HorarioAtendimentoService:
    def busca(self, id):

        horarios = {
            1: {"nomeDoProfessor": "Chris", "horarioDeAtendimento": "10:00-12:00", "periodo": "integral", "sala": "3",
                "predio": ["1", "2", "3", "4", "6"]},
            2: {"nomeDoProfessor": "Renzo", "horarioDeAtendimento": "14:00-16:00", "periodo": "noturno", "sala": "7",
                "predio": ["1", "2", "3", "4", "6"]},
            3: {"nomeDoProfessor": "Marcelo", "horarioDeAtendimento": "13:00-14:00", "periodo": "integral", "sala": "6",
                "predio": ["1", "2", "3", "4", "6"]},
            4: {"nomeDoProfessor": "Ynoguti", "horarioDeAtendimento": "15:00-17:00", "periodo": "noturno", "sala": "8",
                "predio": ["1", "2", "3", "4", "6"]},
            5: {"nomeDoProfessor": "Jonas", "horarioDeAtendimento": "17:00-19:00", "periodo": "integral", "sala": "2",
                "predio": ["1", "2", "3", "4", "6"]},
        }
        horario = horarios.get(id)
        if horario is None:
            return None

        # Garantindo que a estrutura do JSON esteja correta
        horario_formatado = {
            "nomeDoProfessor": horario.get("nomeDoProfessor", ""),
            "horarioDeAtendimento": horario.get("horarioDeAtendimento", ""),
            "periodo": horario.get("periodo", ""),
            "sala": horario.get("sala", ""),
            "predio": horario.get("predio", ["1", "2", "3", "4", "6"])
        }

        return json.dumps(horario_formatado)

    def horario_existente(self, id):
        # Verifica se o horário existe com base no ID
        return id in {
            1, 2, 3, 4, 5  # IDs válidos
        }
class HorarioAtendimento:
    def __init__(self, nome, horario, periodo, sala, predio):
        self.nome = nome
        self.horario = horario
        self.periodo = periodo
        self.sala = sala
        self.predio = predio

class BuscaHorario:
    def __init__(self, service):
        self.horarioService = service

    def busca_horario(self, id):

        # Busca o JSON de atendimento do professor com base no ID
        horarioJson = self.horarioService.busca(id)
        if horarioJson is None:
            return None

        jsonObject = json.loads(horarioJson)

        # Verifica o prédio com base no número da sala
        sala = int(jsonObject["sala"])
        predio = 1 if 1 <= sala <= 5 else (2 if 6 <= sala <= 10 else 3)

        return HorarioAtendimento\
        (
            nome=jsonObject["nomeDoProfessor"],
            horario=jsonObject["horarioDeAtendimento"],
            periodo=jsonObject["periodo"],
            sala=jsonObject["sala"],
            predio=predio
        )

    def verifica_horario_existente(self, id):
        return self.horarioService.horario_existente(id)
