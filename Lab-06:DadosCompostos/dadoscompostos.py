import csv
import copy

meuVeiculo = {
    "vin" : "",
    "make" : "" ,
    "model" : "" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in meuVeiculo.items():
    print(f"{key} : {value}")

print("-" *100)

inventarioList = []

with open('car_list.csv') as csvfile:
    csvLer = csv.reader(csvfile, delimiter=',')
    contandoLinha = 0
    for linha in csvLer:
        if contandoLinha == 0:
            print(f'Os nomes das colunas são: {",".join(linha)}')
            contandoLinha += 1
        else:
            print(f'vin: {linha[0]} make: {linha[1]}, model: {linha[2]}, year: {linha[3]}, range: {linha[4]}, topSpeed: {linha[5]}, zeroSixty: {linha[6]}, mileage: {linha[7]}')
            veiculoAtual = copy.deepcopy(meuVeiculo)
            veiculoAtual["vin"] = linha[0]  
            veiculoAtual["make"] = linha[1]  
            veiculoAtual["model"] =  linha[2]  
            veiculoAtual["year"] = linha[3]  
            veiculoAtual["range"] = linha[4]  
            veiculoAtual["topSpeed"] = linha[5]  
            veiculoAtual["zeroSixty"] =  linha[6]  
            veiculoAtual["mileage"] = linha[7]  
            inventarioList.append(veiculoAtual)
            contandoLinha += 1
    print(f"{contandoLinha} linhas processadas.")

    print("-" *100)

    for meuCarroPro in inventarioList:
        for key, value in meuCarroPro.items():
            print(f"{key} : {value}")
            print("-" *10) 