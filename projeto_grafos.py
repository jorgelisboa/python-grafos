from os import system

# Aqui definimos nosso "banco de dados"/array de dados inicial, cada item da lista representa uma cidade e -
# suas informações, incluindo nome, distância em km, vel. máx, tempo médio em min. e o consumo estimado de -
# combustível, também há uma lista de conexões para cada cidade.

# Aqui definimos nosso "banco de dados"/array de dados inicial, cada item da lista representa uma cidade e suas informações, incluindo nome, distância em km, vel. máx, tempo médio em min. e o consumo estimado de combustível, também há uma lista de conexões para cada cidade.

BD = [
    {
        "city": {
            "name": "Campinas",
            "distanceKm": 30,
            "maxSpeed": 100,
            "averageTimeMinutes": 25,
            "estimatedFuelConsumption": 27.50
        },
        "connections": [
            {
                "cityInfo": {
                    "name": "Valinhos",
                    "distanceKm": 12,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 10,
                    "estimatedFuelConsumption": 15.50
                }
            },
            {
                "cityInfo": {
                    "name": "Paulínia",
                    "distanceKm": 20,
                    "maxSpeed": 90,
                    "averageTimeMinutes": 15,
                    "estimatedFuelConsumption": 18.75
                }
            },
            {
                "cityInfo": {
                    "name": "Hortolândia",
                    "distanceKm": 18,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 13,
                    "estimatedFuelConsumption": 16.25
                }
            }
        ]
    },
    {
        "city": {
            "name": "Valinhos",
            "distanceKm": 15,
            "maxSpeed": 70,
            "averageTimeMinutes": 12,
            "estimatedFuelConsumption": 16.25
        },
        "connections": [
            {
                "cityInfo": {
                    "name": "Campinas",
                    "distanceKm": 30,
                    "maxSpeed": 100,
                    "averageTimeMinutes": 25,
                    "estimatedFuelConsumption": 27.50
                }
            },
            {
                "cityInfo": {
                    "name": "Sumaré",
                    "distanceKm": 20,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 15,
                    "estimatedFuelConsumption": 18.75
                }
            },
            {
                "cityInfo": {
                    "name": "Vinhedo",
                    "distanceKm": 28,
                    "maxSpeed": 90,
                    "averageTimeMinutes": 20,
                    "estimatedFuelConsumption": 25.75
                }
            }
        ]
    },
    {
        "city": {
            "name": "Vinhedo",
            "distanceKm": 20,
            "maxSpeed": 80,
            "averageTimeMinutes": 15,
            "estimatedFuelConsumption": 18.75
        },
        "connections": [
            {
                "cityInfo": {
                    "name": "Valinhos",
                    "distanceKm": 15,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 12,
                    "estimatedFuelConsumption": 16.25
                }
            },
            {
                "cityInfo": {
                    "name": "Jundiaí",
                    "distanceKm": 42,
                    "maxSpeed": 90,
                    "averageTimeMinutes": 30,
                    "estimatedFuelConsumption": 35.00
                }
            },
            {
                "cityInfo": {
                    "name": "Americana",
                    "distanceKm": 35,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 28,
                    "estimatedFuelConsumption": 32.50
                }
            },
            {
                "cityInfo": {
                    "name": "Indaiatuba",
                    "distanceKm": 25,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 20,
                    "estimatedFuelConsumption": 22.50
                }
            }
        ]
    },
    {
        "city": {
            "name": "Jundiaí",
            "distanceKm": 40,
            "maxSpeed": 90,
            "averageTimeMinutes": 35,
            "estimatedFuelConsumption": 37.50
        },
        "connections": [
            {
                "cityInfo": {
                    "name": "Vinhedo",
                    "distanceKm": 20,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 15,
                    "estimatedFuelConsumption": 18.75
                }
            },
            {
                "cityInfo": {
                    "name": "Limeira",
                    "distanceKm": 58,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 40,
                    "estimatedFuelConsumption": 42.50
                }
            },
            {
                "cityInfo": {
                    "name": "Sorocaba",
                    "distanceKm": 70,
                    "maxSpeed": 100,
                    "averageTimeMinutes": 50,
                    "estimatedFuelConsumption": 55.00
                }
            },
            {
                "cityInfo": {
                    "name": "Mogi-Mirim",
                    "distanceKm": 60,
                    "maxSpeed": 90,
                    "averageTimeMinutes": 45,
                    "estimatedFuelConsumption": 47.50
                }
            }
        ]
    },
    {
        "city": {
            "name": "Limeira",
            "distanceKm": 55,
            "maxSpeed": 80,
            "averageTimeMinutes": 40,
            "estimatedFuelConsumption": 42.50
        },
        "connections": [
            {
                "cityInfo": {
                    "name": "Jundiaí",
                    "distanceKm": 40,
                    "maxSpeed": 90,
                    "averageTimeMinutes": 35,
                    "estimatedFuelConsumption": 37.50
                }
            },
            {
                "cityInfo": {
                    "name": "Americana",
                    "distanceKm": 35,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 28,
                    "estimatedFuelConsumption": 32.50
                }
            },
            {
                "cityInfo": {
                    "name": "Cosmópolis",
                    "distanceKm": 25,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 20,
                    "estimatedFuelConsumption": 22.50
                }
            }
        ]
    },
    {
        "city": {
            "name": "Americana",
            "distanceKm": 60,
            "maxSpeed": 100,
            "averageTimeMinutes": 50,
            "estimatedFuelConsumption": 55.00
        },
        "connections": [
            {
                "cityInfo": {
                    "name": "Vinhedo",
                    "distanceKm": 28,
                    "maxSpeed": 90,
                    "averageTimeMinutes": 20,
                    "estimatedFuelConsumption": 25.75
                }
            },
            {
                "cityInfo": {
                    "name": "Sumaré",
                    "distanceKm": 20,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 15,
                    "estimatedFuelConsumption": 18.75
                }
            },
            {
                "cityInfo": {
                    "name": "Paulínia",
                    "distanceKm": 15,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 12,
                    "estimatedFuelConsumption": 16.25
                }
            },
            {
                "cityInfo": {
                    "name": "Limeira",
                    "distanceKm": 55,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 40,
                    "estimatedFuelConsumption": 42.50
                }
            }
        ]
    },
    {
        "city": {
            "name": "Sumaré",
            "distanceKm": 18,
            "maxSpeed": 70,
            "averageTimeMinutes": 13,
            "estimatedFuelConsumption": 16.25
        },
        "connections": [
            {
                "cityInfo": {
                    "name": "Valinhos",
                    "distanceKm": 15,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 12,
                    "estimatedFuelConsumption": 16.25
                }
            },
            {
                "cityInfo": {
                    "name": "Paulínia",
                    "distanceKm": 15,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 12,
                    "estimatedFuelConsumption": 16.25
                }
            },
            {
                "cityInfo": {
                    "name": "Americana",
                    "distanceKm": 60,
                    "maxSpeed": 100,
                    "averageTimeMinutes": 50,
                    "estimatedFuelConsumption": 55.00
                }
            },
            {
                "cityInfo": {
                    "name": "Hortolândia",
                    "distanceKm": 15,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 12,
                    "estimatedFuelConsumption": 16.25
                }
            }
        ]
    },
    {
        "city": {
            "name": "Paulínia",
            "distanceKm": 15,
            "maxSpeed": 80,
            "averageTimeMinutes": 12,
            "estimatedFuelConsumption": 16.25
        },
        "connections": [
            {
                "cityInfo": {
                    "name": "Sumaré",
                    "distanceKm": 18,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 13,
                    "estimatedFuelConsumption": 16.25
                }
            },
            {
                "cityInfo": {
                    "name": "Campinas",
                    "distanceKm": 30,
                    "maxSpeed": 100,
                    "averageTimeMinutes": 25,
                    "estimatedFuelConsumption": 27.50
                }
            },
            {
                "cityInfo": {
                    "name": "Cosmópolis",
                    "distanceKm": 25,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 20,
                    "estimatedFuelConsumption": 22.50
                }
            }
        ]
    },
    {
        "city": {
            "name": "Indaiatuba",
            "distanceKm": 25,
            "maxSpeed": 70,
            "averageTimeMinutes": 20,
            "estimatedFuelConsumption": 22.50
        },
        "connections": [
            {
                "cityInfo": {
                    "name": "Vinhedo",
                    "distanceKm": 20,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 15,
                    "estimatedFuelConsumption": 18.75
                }
            },
            {
                "cityInfo": {
                    "name": "Cosmópolis",
                    "distanceKm": 12,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 10,
                    "estimatedFuelConsumption": 15.50
                }
            },
            {
                "cityInfo": {
                    "name": "Sorocaba",
                    "distanceKm": 70,
                    "maxSpeed": 100,
                    "averageTimeMinutes": 50,
                    "estimatedFuelConsumption": 55.00
                }
            }
        ]
    },
    {
        "city": {
            "name": "Cosmópolis",
            "distanceKm": 15,
            "maxSpeed": 70,
            "averageTimeMinutes": 12,
            "estimatedFuelConsumption": 16.25
        },
        "connections": [
            {
                "cityInfo": {
                    "name": "Paulínia",
                    "distanceKm": 15,
                    "maxSpeed": 80,
                    "averageTimeMinutes": 12,
                    "estimatedFuelConsumption": 16.25
                }
            },
            {
                "cityInfo": {
                    "name": "Limeira",
                    "distanceKm": 25,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 20,
                    "estimatedFuelConsumption": 22.50
                }
            },
            {
                "cityInfo": {
                    "name": "Indaiatuba",
                    "distanceKm": 12,
                    "maxSpeed": 70,
                    "averageTimeMinutes": 10,
                    "estimatedFuelConsumption": 15.50
                }
            }
        ]
    }
]


# Função que lista todas as opções do banco de dados, ela imprime uma tabela formatada, contendo todas as opções -
# do banco de dados, ela itera sobre cada item do banco e extrai as infos relevantes (nome da cidade, distância, -
# velocidade máxima, tempo médio e conexões) formata adequadamente e imprime na tela.

def clear_screen():
    system("cls")


def listOptions():
    clear_screen()
    print("BD:")
    print("------------------------------------------------------------------------------------------------------------------")
    print("|   Pos  |     City      | Dist (km) | Max Speed | Time (min) | Fuel (L) |    Connections    |")
    print("------------------------------------------------------------------------------------------------------------------")
    for pos, data in enumerate(BD):
        city_name = data["city"]["name"]
        distance = data["city"]["distanceKm"]
        max_speed = data["city"]["maxSpeed"]
        avg_time = data["city"]["averageTimeMinutes"]
        fuel_consumption = data["city"]["estimatedFuelConsumption"]
        print(f"|   {pos+1:2}   | {city_name:12} | {distance:9} | {max_speed:9} | {avg_time:11} | {fuel_consumption:9} |  |")
    print("------------------------------------------------------------------------------------------------------------------")


# Função para cadastrar uma nova cidade no banco de dados
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


# Função para deletar uma nova cidade no banco de dados
def deletar_cidade(nome_cidade):
    if cidade_existe(nome_cidade) == False:
        print(f"A cidade {nome_cidade} não existe no banco de dados.")
        return
    for cidade in BD:
        if cidade["city"]["name"] == nome_cidade:
            BD.remove(cidade)
            print(f"A cidade {nome_cidade} foi removida do banco de dados com sucesso.")
            return
    print(f"A cidade {nome_cidade} não foi encontrada no banco de dados.")


def menu():
    clear_screen()
    print("------- Menu -------")
    print("1. Listar cidades")
    print("2. Cadastrar nova cidade")
    print("3. Encontrar melhor rota")
    print("4. Deletar uma cidade")
    print("5. Sair")

    opcao = input("Selecione uma opção: ")
    if opcao == "1":
        clear_screen()
        listOptions()
        input("\nPressione Enter para voltar ao menu...")
        menu()
    elif opcao == "2":
        clear_screen()
        name = input("Digite o nome da cidade: ")
        distance = float(input("Digite a distância em km: "))
        max_speed = int(input("Digite a velocidade máxima: "))
        avg_time = int(input("Digite o tempo médio em minutos: "))
        fuel_consumption = float(input("Digite o consumo estimado de combustível: "))
        connections = set(input("Digite as conexões separadas por vírgula: ").split(","))
        cadastrar_cidade(name, distance, max_speed, avg_time, fuel_consumption, connections)
        print("Cidade cadastrada com sucesso!")
        input("\nPressione Enter para voltar ao menu...")
        menu()
    elif opcao == "3":
        clear_screen()
        start_city = input("Digite a cidade de partida: ")
        end_city = input("Digite a cidade de destino: ")
        print("\nSelecione os parâmetros a serem priorizados:")
        print("1. Distância em KM")
        print("2. Maior velocidade de via")
        print("3. Tempo médio de viagem")
        print("4. Consumo estimado de combustível")

        param1 = input("Digite o número do primeiro parâmetro: ")
        param2 = input("Digite o número do segundo parâmetro: ")

        param1 = get_param_name(param1)
        param2 = get_param_name(param2)

        encontrar_melhor_rota(start_city, end_city, param1, param2)
        input("\nPressione Enter para voltar ao menu...")
        menu()
    elif opcao == "4":
        clear_screen()
        nome_cidade = input("Digite o nome da cidade a ser deletada: ")
        deletar_cidade(nome_cidade)
        input("\nPressione Enter para voltar ao menu...")
        menu()
    elif opcao == "5":
        clear_screen()
        print("Encerrando o programa...")
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
        input("\nPressione Enter para voltar ao menu...")
        menu()


# Função para obter o nome do parâmetro com base no número fornecido
def get_param_name(number):
    if number == "1":
        return "distanceKm"
    elif number == "2":
        return "maxSpeed"
    elif number == "3":
        return "averageTimeMinutes"
    elif number == "4":
        return "estimatedFuelConsumption"
    else:
        return ""


# Função para encontrar a melhor rota com base nos parâmetros priorizados pelo usuário
def encontrar_melhor_rota(start_city, end_city, param1, param2):
    if start_city == end_city:
        clear_screen()
        print("Início e destino não podem ser iguais!")
        return
    
    if cidade_existe(start_city) == False:
        clear_screen()
        print(f"{start_city} não existe!")
        return

    if cidade_existe(end_city) == False:
        print(f"{end_city} não existe!")
        return

    # Encontrar todas as rotas possíveis
    rotas_possiveis = []
    for cidade in BD:
        if cidade["city"]["name"] == start_city:
            rotas_possiveis = buscar_rotas(start_city, end_city, [], [cidade])
            break

    # Encontrar a melhor rota com base nos parâmetros priorizados
    melhor_rota = None
    melhor_pontuacao = float('inf')

    for rota in rotas_possiveis:
        pontuacao = calcular_pontuacao(rota, param1, param2)
        if pontuacao < melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_rota = rota

    # Exibir a melhor rota encontrada
    if melhor_rota:
        print("Melhor rota:")
        for i, cidade in enumerate(melhor_rota):
            print(f"{i+1}. {cidade['city']['name']}")
    else:
        print("Não foi possível encontrar uma rota que atenda aos requisitos.")


# Função auxiliar para buscar todas as rotas possíveis recursivamente
def buscar_rotas(current_city, end_city, visited_cities, current_route):
    if current_city == end_city:
        return [current_route]

    rotas = []
    for cidade in BD:
        if cidade["city"]["name"] == current_city:
            for connection in cidade["connections"]:
                if connection not in visited_cities:
                    nova_rota = current_route.copy()
                    for city in BD:
                        if city["city"]["name"] == connection:
                            nova_rota.append(city)
                            break
                    visited_cities.append(connection)
                    rotas.extend(buscar_rotas(connection, end_city, visited_cities, nova_rota))
                    visited_cities.remove(connection)

    return rotas

# Função para ver se a cidade existe
def cidade_existe(city_name):
    for city_data in BD:
        if city_data['city']['name'] == city_name:
            return True
    return False


# Função auxiliar para calcular a pontuação de uma rota com base nos parâmetros priorizados
def calcular_pontuacao(rota, param1, param2):
    pontuacao = 0
    for cidade in rota:
        pontuacao += cidade["city"][param1] + cidade["city"][param2]
    return pontuacao


# Executar o menu
menu()