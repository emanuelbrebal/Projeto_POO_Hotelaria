class Hospede:
    def __init__(self, nome, hospede_ID, historico_reservas=None):
        self.nome = nome
        self.hospede_ID = hospede_ID
        self.historico_reservas = historico_reservas 
    
    # Get e set para nome
    def get_nome(self):
        return self.nome  

    def set_nome(self, nome):
        self.nome = nome

    # Get e set para ID
    def get_hospede_ID(self):
        return self.hospede_ID  

    def set_hospede_ID(self, new_ID):
        self.hospede_ID = new_ID

    # Get para histórico de reservas
    def get_historico(self):
        return self.historico_reservas

    # Método para adicionar uma reserva ao histórico
    def adicionar_reserva(self, reserva):
        self.historico_reservas.append(reserva)

    # __str__ para formatar as saídas
    def __str__(self):
        return f'Nome: {self.nome}, ID: {self.hospede_ID}, Histórico de reservas: {self.historico_reservas}'
