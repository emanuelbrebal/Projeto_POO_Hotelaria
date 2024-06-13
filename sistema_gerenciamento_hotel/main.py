from hospedes.guests import *
#from sistema_gerenciamento_hotel.hospedes.guests_functions import *
from quartos.rooms import *
#from sistema_gerenciamento_hotel.hospedes.rooms_functions import *
from reservas.booking import *
#from sistema_gerenciamento_hotel.hospedes.booking_functions import *

#declara arrays que serão utilizados
hospedes_array = []
quartos_array = []
reservas_array = []

#povoamento quartos
quarto1 = quarto_simples('101', 100)
suite1 = suite('201', 200)
quarto_duplo1 = quarto_duplo('301', 150)

#povoando os quartos
quartos_array.append(quarto1)
quartos_array.append(suite1)
quartos_array.append(quarto_duplo1)


while (True):
    print("""
        -----Menu Inicial-----
          Bem-vindo(a) ao sistema de gerenciamento de hotéis
          Por favor, selecione uma opção:
          1- Área dos quartos
          2- Área dos hóspedes
          3- Área das reservas
          0- Encerrar programa
    """)
    opc = int(input("Digite a sua opção: "))

    if opc == 1:
        print("""
            -----Área dos Quartos-----
        
            Por favor, selecione uma opção referente aos quartos:
            1- Listar todos os quartos
            2- Remover quartos
            3- Atualizar quartos
            4- Voltar para Menu Inicial
            0- Encerrar programa
        """)
        opc_rooms = int(input("Digite a sua opção: "))
        if opc_rooms == 1:
            print(quartos_array)
        elif opc_rooms == 2:
            print(quartos_array)
            indice = int(input("Digite o índice do quarto que deseja remover: "))
            if indice > 0:
                quartos_array.pop(indice-1)
            elif indice == 0:
                quartos_array.pop(indice)
            else:   
                print("Índice inválido.")
        elif opc_rooms == 3:
            print(quartos_array)
            indice = int(input("Digite o índice do quarto que deseja atualizar: "))
            novo_quarto = quartos_array[indice-1] 
            novo_preco = str(input("Qual o novo preço do quarto? "))
            novo_quarto.preco_quarto = novo_preco
        elif opc_rooms == 4:
            opc == ''
            opc_rooms == ''
        elif opc_rooms == 0:
            break
        
    elif opc == 2:
        print("""
            -----Área dos Hóspedes-----
        
            Por favor, selecione uma opção referente aos hóspedes:
            1- Registrar novo hóspede
            2- Consultar histórico de reservas
            3- Fazer reserva (check-in/check-out)
            4- Voltar para Menu Inicial
            0- Encerrar programa
        """)
        opc_guests = int(input("Digite a sua opção: "))
        if opc_guests == 1:
            nome = str(input("Digite o nome do novo hóspede: "))
            hospede_ID = str(input("Digite o ID do novo hóspede: "))
            novo_hospede = Hospede(nome, hospede_ID, '')
            hospedes_array.append(novo_hospede)

            for i in hospedes_array:
                print(i)

        elif opc_guests == 2:
            print(hospedes_array)
            indice = int(input("Digite o índice do hóspede que quer visualizar: "))
            view_hospede = hospedes_array[indice-1]
            print(view_hospede.historico_reservas)


        elif opc_guests == 4:
            opc == ''
            opc_guests == ''
        elif opc_guests == 0:
            break

    elif opc == 0:
        break