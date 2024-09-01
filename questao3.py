import json

faturamento_json = '''
[
    {"dia": 1, "valor": 1000.0},
    {"dia": 2, "valor": 2000.0},
    {"dia": 3, "valor": 0.0},
    {"dia": 4, "valor": 3000.0},
    {"dia": 5, "valor": 4000.0}
    // Adicione os dados restantes do mês
]
'''

faturamento_diario = json.loads(faturamento_json)

valores = [dia["valor"] for dia in faturamento_diario if dia["valor"] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
