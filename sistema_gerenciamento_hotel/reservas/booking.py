class Reserva:
    # Método construtor com atributos da classe reserva
    def __init__(self, data_checkin, data_checkout, estado='Disponível'):
        self.__data_checkin = data_checkin
        self.__data_checkout = data_checkout
        self.estado = estado

    # Get/set de data de check-in
    def get_data_checkin(self):
        return self.__data_checkin
    
    def set_data_checkin(self, nova_data_checkin):
        self.__data_checkin = nova_data_checkin

    # Get/set de data de check-out
    def get_data_checkout(self):
        return self.__data_checkout
    
    def set_data_checkout(self, nova_data_checkout):
        self.__data_checkout = nova_data_checkout

    # Set e get do estado
    def set_estado(self, estado):
        self.estado = estado
    
    def get_estado(self):
        return self.estado

    # Método para atualizar o estado baseado nas datas
    def atualizar_estado(self):
        if self.__data_checkin and not self.__data_checkout:
            self.estado = 'Ocupado'
        else:
            self.estado = 'Disponível'

    # Método __str__ para formatação de saídas
    def __str__(self):
        return (f'Data de Check-in: {self.__data_checkin}, Data de Check-out: {self.__data_checkout}, '
                f'Disponibilidade para reserva: {self.estado}')


