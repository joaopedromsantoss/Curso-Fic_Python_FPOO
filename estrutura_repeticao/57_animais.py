import json
animais = [
    {
     "animal": "Cachorro Pastor",
     "idade": 3,
     "fator_idade_humano": 12,
     "idade_de_humano": 0
    },
    {
     "animal": "Cachorro Fila",
     "idade": 4,
     "fator_idade_humano": 10,
     "idade_de_humano": 0
    },
    {
      "animal": "Cachorro Golden",
      "idade": 2,
      "fator_idade_humano": 8,
      "idade_de_humano": 0
    },
    {
      "animal": "Papagaio",
      "idade": 8,
      "fator_idade_humano": 5,
      "idade_de_humano": 0
    },
    {
      "animal": "Gato Siamês",
      "idade": 3,
      "fator_idade_humano": 9,
      "idade_de_humano": 0
    },
    {
      "animal": "Cachorro Husky",
      "idade": 3,
      "fator_idade_humano": 9,
      "idade_de_humano": 0
    }
]

for animal in animais:
   idade_animal_humano = animal.get("idade") * animal.get("fator_idade_humano")
   animal["idade_de_humano"] = idade_animal_humano
   eh_cachoro = animal.get("animal").startswith("Cachorro")

   if eh_cachoro and animal.get("idade_de_humano") >= 30:
       print(f"-----Informações do Animal-----")
       print(json.dumps(animal, sort_keys=True, indent=4))