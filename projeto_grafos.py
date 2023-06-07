from collections import deque

grafo = {
    'Campinas': [('Indaiatuba', 20), ('Valinhos', 15), ('Jundiaí', 50)],
    'Indaiatuba': [('Campinas', 20), ('Valinhos', 12)],
    'Valinhos': [('Campinas', 15), ('Indaiatuba', 12), ('Jundiaí', 40), ('Hortolândia', 30)],
    'Jundiaí': [('Campinas', 50), ('Valinhos', 40), ('Hortolândia', 25)],
    'Hortolândia': [('Valinhos', 30), ('Jundiaí', 25), ('Sumaré', 10)],
    'Sumaré': [('Hortolândia', 10), ('Paulínia', 20)],
    'Paulínia': [('Sumaré', 20)]
}

# Dicionário com os parâmetros de cada conexão
parametros = {
    ('Campinas', 'Indaiatuba'): {'distancia': 20, 'velocidade_maxima': 80, 'velocidade_media': 60, 'custo_pedagio': 5, 'num_pedagios': 1, 'peso_max': 100, 'seguranca': 9, 'num_postos': 2, 'conforto': 4.5, 'eficiencia': 7.2},
    ('Campinas', 'Valinhos'): {'distancia': 15, 'velocidade_maxima': 60, 'velocidade_media': 50, 'custo_pedagio': 3, 'num_pedagios': 0, 'peso_max': 80, 'seguranca': 8, 'num_postos': 1, 'conforto': 3.2, 'eficiencia': 6.7},
    ('Campinas', 'Jundiaí'): {'distancia': 50, 'velocidade_maxima': 70, 'velocidade_media': 55, 'custo_pedagio': 8, 'num_pedagios': 2, 'peso_max': 120, 'seguranca': 9.5, 'num_postos': 3, 'conforto': 4.8, 'eficiencia': 8.5},
    ('Indaiatuba', 'Valinhos'): {'distancia': 12, 'velocidade_maxima': 60, 'velocidade_media': 50, 'custo_pedagio': 2, 'num_pedagios': 0, 'peso_max': 80, 'seguranca': 7.5, 'num_postos': 1, 'conforto': 3.1, 'eficiencia': 6.4},
    ('Valinhos', 'Jundiaí'): {'distancia': 40, 'velocidade_maxima': 70, 'velocidade_media': 55, 'custo_pedagio': 7, 'num_pedagios': 1, 'peso_max': 110, 'seguranca': 8.7, 'num_postos': 2, 'conforto': 4.2, 'eficiencia': 7.9},
    ('Valinhos', 'Hortolândia'): {'distancia': 30, 'velocidade_maxima': 60, 'velocidade_media': 45, 'custo_pedagio': 4, 'num_pedagios': 0, 'peso_max': 90, 'seguranca': 7.8, 'num_postos': 1, 'conforto': 3.8, 'eficiencia': 6.1},
    ('Jundiaí', 'Hortolândia'): {'distancia': 25, 'velocidade_maxima': 70, 'velocidade_media': 50, 'custo_pedagio': 3, 'num_pedagios': 0, 'peso_max': 100, 'seguranca': 8.5, 'num_postos': 2, 'conforto': 4.6, 'eficiencia': 7.5},
    ('Hortolândia', 'Sumaré'): {'distancia': 10, 'velocidade_maxima': 60, 'velocidade_media': 45, 'custo_pedagio': 1, 'num_pedagios': 0, 'peso_max': 70, 'seguranca': 7, 'num_postos': 1, 'conforto': 3.8, 'eficiencia': 6.1},
    ('Sumaré', 'Paulínia'): {'distancia': 20, 'velocidade_maxima': 60, 'velocidade_media': 45, 'custo_pedagio': 2, 'num_pedagios': 0, 'peso_max': 80, 'seguranca': 7.2, 'num_postos': 1, 'conforto': 3.5, 'eficiencia': 6.8},
}

def clear_screen():
    print("\033c", end="")

def cadastrar_cidade():
    cidade = input("Digite o nome da cidade: ")
    if cidade in grafo:
        print("Cidade já cadastrada!")
    else:
        grafo[cidade] = []
        print(f"Cidade '{cidade}' cadastrada com sucesso!")

def cadastrar_conexao():
    cidade_origem = input("Digite o nome da cidade de origem: ")
    cidade_destino = input("Digite o nome da cidade de destino: ")
    distancia = int(input("Digite a distância entre as cidades: "))

    if cidade_origem in grafo and cidade_destino in grafo:
        grafo[cidade_origem].append((cidade_destino, distancia))
        parametros[(cidade_origem, cidade_destino)] = {}
        print("Conexão entre as cidades cadastrada com sucesso!")
    else:
        print("Uma ou ambas as cidades não estão cadastradas!")

def buscar_rota():
    cidade_origem = input("Digite o nome da cidade de origem: ")
    cidade_destino = input("Digite o nome da cidade de destino: ")

    if cidade_origem not in grafo or cidade_destino not in grafo:
        print("Uma ou ambas as cidades não estão cadastradas!")
        return

    print("\nParâmetros disponíveis:")
    if (cidade_origem, cidade_destino) in parametros:
        for i, parametro in enumerate(parametros[(cidade_origem, cidade_destino)].keys()):
            print(f"{i+1} - {parametro}")

        parametro1_index = int(input("\nDigite o número do primeiro parâmetro desejado: "))
        parametro2_index = int(input("Digite o número do segundo parâmetro desejado: "))

        if parametro1_index < 1 or parametro1_index > len(parametros[(cidade_origem, cidade_destino)]) or \
                parametro2_index < 1 or parametro2_index > len(parametros[(cidade_origem, cidade_destino)]):
            print("Opção inválida.")
            return

        parametro1 = list(parametros[(cidade_origem, cidade_destino)].keys())[parametro1_index - 1]
        parametro2 = list(parametros[(cidade_origem, cidade_destino)].keys())[parametro2_index - 1]

        fila = deque()
        fila.append([(cidade_origem, None)])
        melhor_rota = None
        menor_custo = float('inf')

        while fila:
            rota_atual = fila.popleft()
            cidade_atual, _ = rota_atual[-1]

            if cidade_atual == cidade_destino:
                custo_total = 0
                for i in range(len(rota_atual) - 1):
                    cidade_atual, cidade_proxima = rota_atual[i]
                    custo_total += parametros[(cidade_atual, cidade_proxima)][parametro1] + \
                                  parametros[(cidade_atual, cidade_proxima)][parametro2]

                if custo_total < menor_custo:
                    melhor_rota = rota_atual
                    menor_custo = custo_total

            for cidade_proxima, _ in grafo[cidade_atual]:
                if cidade_proxima not in [cidade for cidade, _ in rota_atual]:
                    nova_rota = list(rota_atual)
                    nova_rota.append((cidade_proxima, distancia))
                    fila.append(nova_rota)

        if melhor_rota:
            print(f"\nMelhor rota encontrada: {', '.join([cidade for cidade, _ in melhor_rota])}")
            print(f"Custo total: {menor_custo}")
        else:
            print("Não foi possível encontrar uma rota entre as cidades.")
    else:
        print("Não foram encontrados parâmetros para essa rota.")




def listar_cidades():
    print("\nCidades cadastradas:")
    for cidade in grafo:
        print(f"- {cidade}")
        for conexao, distancia in grafo[cidade]:
            print(f"  - {cidade} -> {conexao}")
            print("    Parâmetros:")
            if (cidade, conexao) in parametros:
                for parametro, valor in parametros[(cidade, conexao)].items():
                    print(f"    - {parametro}: {valor}")



while True:
    clear_screen()
    print("===== MENU =====")
    print("1 - Cadastrar cidade")
    print("2 - Cadastrar conexão entre cidades")
    print("3 - Buscar rota")
    print("4 - Listar cidades")
    print("0 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 0:
        break
    elif opcao == 1:
        cadastrar_cidade()
    elif opcao == 2:
        cadastrar_conexao()
    elif opcao == 3:
        buscar_rota()
    elif opcao == 4:
        listar_cidades()
    else:
        print("Opção inválida.")

    input("\nPressione Enter para continuar...")
