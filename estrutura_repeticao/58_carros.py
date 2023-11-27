import json

carros = [
    {
        "veiculo": "Hb20",
        "valor_km": 0.89,
        "valor_dia": 67.90,
        "valor_seguro": 129.90,
        "media_gasolina": 12,
        "media_etanol": 10,
        "valor_total_gasolina": 0,
        "valor_total_etanol": 0
    },
    {
        "veiculo": "Mobi",
        "valor_km": 0.79,
        "valor_dia": 62.90,
        "valor_seguro": 119.90,
        "media_gasolina": 15,
        "media_etanol": 10,
        "valor_total_gasolina": 0,
        "valor_total_etanol": 0
    },
    {
        "veiculo": "Voyage",
        "valor_km": 1.09,
        "valor_dia": 89.90,
        "valor_seguro": 79.90,
        "media_gasolina": 9,
        "media_etanol": 7,
        "valor_total_gasolina": 0,
        "valor_total_etanol": 0
    },
    {
        "veiculo": "Spin",
        "valor_km": 0.99,
        "valor_dia": 99.90,
        "valor_seguro":109.90,
        "media_gasolina": 8,
        "media_etanol": 6,
        "valor_total_gasolina": 0,
        "valor_total_etanol": 0
    },
    {
        "veiculo": "Cronos",
        "valor_km": 1.19,
        "valor_dia": 99.90,
        "valor_seguro": 59.90,
        "media_gasolina": 11,
        "media_etanol": 9,
        "valor_total_gasolina": 0,
        "valor_total_etanol": 0
    },
    {
        "veiculo": "Argo",
        "valor_km": 0.89,
        "valor_dia": 49.90,
        "valor_seguro": 159.90,
        "media_gasolina": 13,
        "media_etanol": 11,
        "valor_total_gasolina": 0,
        "valor_total_etanol": 0
    },
    {
      "veiculo": "Logan",
      "valor_km": 0.67,
      "valor_dia": 69.90,
      "valor_seguro": 109.90,
      "media_gasolina": 10,
      "media_etanol": 8,
      "valor_total_gasolina": 0,
      "valor_total_etanol": 0
    }
]

for carro in carros:
    valor_gasolina = (890 / carro.get("media_gasolina")) * 5.29
    valor_etanol = (890 / carro.get("media_etanol")) * 3.39
    valor_total_gasolina = valor_gasolina + (carro.get("valor_km") * 890) + (carro.get("valor_dia") * 3) + (carro.get("valor_seguro"))
    valor_total_etanol = valor_etanol + (carro.get("valor_km") * 890) + (carro.get("valor_dia") * 3) + (carro.get("valor_seguro"))
    carro["valor_total_gasolina"] = valor_total_gasolina
    carro["valor_total_etanol"] = valor_total_etanol



    if carro.get("valor_total_gasolina") and carro.get("valor_total_etanol") <= 1400:
        print(f"-----Informações dos Carros-----")
        print(json.dumps(carro, sort_keys=True, indent=4))