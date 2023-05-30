# Aqui definimos nosso "banco de dados"/array de dados inicial, cada item da lista representa uma cidade e -
# suas informações, incluindo nome, distância em km, vel. máx, tempo médio em min. e o consumo estimado de -
# combustível, também há uma lista de conexões para cada cidade.

BD = [
    {
        "city": {
            "name": "campinas",
            "distanceKm": 0,
            "maxSpeed": 120,
            "averageTimeMinutes": 0,
            "estimatedFuelConsumption": 0
        },
        "connections": {"valinhos", "paulínia"}
    },
    {
        "city": {
            "name": "valinhos",
            "distanceKm": 12,
            "maxSpeed": 80,
            "averageTimeMinutes": 10,
            "estimatedFuelConsumption": 15.50
        },
        "connections": {"campinas", "sumaré", "vinhedo"}
    },
    {
        "city": {
            "name": "vinhedo",
            "distanceKm": 28,
            "maxSpeed": 100,
            "averageTimeMinutes": 20,
            "estimatedFuelConsumption": 25.75
        },
        "connections": {"valinhos", "jundiaí", "americana"}
    },
    {
        "city": {
            "name": "jundiaí",
            "distanceKm": 42,
            "maxSpeed": 90,
            "averageTimeMinutes": 30,
            "estimatedFuelConsumption": 35.00
        },
        "connections": {"vinhedo", "limeira"}
    },
    {
        "city": {
            "name": "limeira",
            "distanceKm": 58,
            "maxSpeed": 80,
            "averageTimeMinutes": 40,
            "estimatedFuelConsumption": 42.50
        },
        "connections": {"jundiaí", "americana"}
    },
    {
        "city": {
            "name": "americana",
            "distanceKm": 78,
            "maxSpeed": 100,
            "averageTimeMinutes": 50,
            "estimatedFuelConsumption": 55.00
        },
        "connections": {"vinhedo", "sumaré", "paulínia"}
    },
    {
        "city": {
            "name": "sumaré",
            "distanceKm": 20,
            "maxSpeed": 70,
            "averageTimeMinutes": 15,
            "estimatedFuelConsumption": 18.75
        },
        "connections": {"valinhos", "paulínia", "americana"}
    },
    {
        "city": {
            "name": "paulínia",
            "distanceKm": 15,
            "maxSpeed": 80,
            "averageTimeMinutes": 12,
            "estimatedFuelConsumption": 16.25
        },
        "connections": {"sumaré", "campinas"}
    }
]

# Função que lista todas as opções do banco de dados, ela imprime uma tabela formatada, contendo todas as opções -
# do banco de ddados, ela itera sobre cada item do banco e extrai as infos relevantes (nome da cidade, distância, - 
# velocidade máxima, tempo médio e conexões) formata adequadamente e imprime na tela.

def listOptions():
    print("\nBD:")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("|   Pos  |     City      | Dist (km) | Max Speed | Time (min) | Fuel (L) |    Connections    |")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    for pos, lin in enumerate(BD):
        city_name = lin["city"]["name"]
        distance = lin["city"]["distanceKm"]
        max_speed = lin["city"]["maxSpeed"]
        avg_time = lin["city"]["averageTimeMinutes"]
        fuel_consumption = lin["city"]["estimatedFuelConsumption"]
        connections = ", ".join(lin["connections"])
        print(f"|   {pos+1:2}   | {city_name:12} | {distance:9} | {max_speed:9} | {avg_time:11} | {fuel_consumption:9} | {connections:16} |")
    print("-----------------------------------------------------------------------------------------------------------------------------------")

# Função para cadastrar uma nova cidade no banco de dados, nela, recebemos os parâmetros necessários para cadastrar -
# uma nova cidade no banco, ela cria um novo dicionário contendo as infos da cidade e as conexões, em sequencia -
# adiciona esse dicionário à lista "BD".

def cadastrar_cidade(name, distance, max_speed, avg_time, fuel_consumption, connections):
    new_city = {
        "city": {
            "name": name,
            "distanceKm": distance,
            "maxSpeed": max_speed,
            "averageTimeMinutes": avg_time,
            "estimatedFuelConsumption": fuel_consumption
        },
        "connections": connections
    }
    BD.append(new_city)

cadastrar_cidade("sao paulo", 100, 120, 90, 50.0, {"campinas", "guarulhos", "santo andre"})
cadastrar_cidade("rio de janeiro", 150, 110, 120, 55.5, {"niteroi", "duque de caxias"})
cadastrar_cidade("belo horizonte", 200, 100, 150, 60.0, {"contagem", "nova lima"})
cadastrar_cidade("porto alegre", 250, 90, 180, 65.5, {"canoas", "gravatai"})
cadastrar_cidade("curitiba", 300, 80, 210, 70.0, {"sao jose dos pinhais", "colombo"})
cadastrar_cidade("salvador", 350, 70, 240, 75.5, {"lauro de freitas", "camacari"})
cadastrar_cidade("recife", 400, 60, 270, 80.0, {"olinda", "jaboatao dos guararapes"})
cadastrar_cidade("fortaleza", 450, 50, 300, 85.5, {"caucaia", "maracanau"})
cadastrar_cidade("manaus", 500, 40, 330, 90.0, {"itacoatiara", "parintins"})
cadastrar_cidade("brasilia", 550, 30, 360, 95.5, {"gama", "taguatinga"})

listOptions()