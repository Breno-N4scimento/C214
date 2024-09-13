import json
import os


def writeAJson(data, name: str):
    try:
        # Verifica se os dados são válidos para JSON
        parsed_json = json.dumps(data, default=str)  # Converte os dados para uma string JSON

        # Cria o diretório se não existir
        if not os.path.isdir("json"):
            os.makedirs("json")

        # Abre e escreve os dados no arquivo JSON
        with open(f"./json/{name}.json", 'w') as json_file:
            json.dump(json.loads(parsed_json), json_file, indent=4, separators=(',', ': '))

        print(f"Arquivo JSON '{name}.json' criado com sucesso.")

    except Exception as e:
        print(f"Erro ao criar o arquivo JSON: {e}")

data = {
    "nome": "Chris",
    "horarioDeAtendimento": "10:00-12:00",
    "periodo": "integral",
    "sala": "3",
    "predio": ["4"]
}
writeAJson(data, "exemplo_horario")
