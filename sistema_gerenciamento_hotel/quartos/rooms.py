class quarto_simples:
    def __init__(self, numero_quarto, preco_quarto, tipo_cama='Cama de solteiro'):
        self.numero_quarto = numero_quarto
        self.tipo_quarto = 'Quarto Simples'
        self.status_quarto = 'DISPONÍVEL'
        self.preco_quarto = preco_quarto
        self.tipo_cama = tipo_cama
        self.qtd_camas = 1

    def __str__(self):
        return (f'Número do quarto: {self.numero_quarto}, Tipo do quarto: {self.tipo_quarto}, '
                f'Status do quarto: {self.status_quarto}, Preço do quarto: {self.preco_quarto}, '
                f'Tipo de cama: {self.tipo_cama}, Quantidade de Camas: {self.qtd_camas}')


class suite(quarto_simples):
    def __init__(self, numero_quarto, preco_quarto):
        super().__init__(numero_quarto, preco_quarto, tipo_cama='Cama de casal')
        self.tipo_quarto = "Suíte"
        self.banheiro = True

    def __str__(self):
        return (f'Número do quarto: {self.numero_quarto}, Tipo do quarto: {self.tipo_quarto}, '
                f'Status do quarto: {self.status_quarto}, Preço do quarto: {self.preco_quarto}, '
                f'Tipo de cama: {self.tipo_cama}, Quantidade de camas: {self.qtd_camas}, '
                f'Banheiro: {self.banheiro}')


class quarto_duplo(quarto_simples):
    def __init__(self, numero_quarto, preco_quarto, tipo_cama='Cama de solteiro'):
        super().__init__(numero_quarto, preco_quarto, tipo_cama)
        self.tipo_quarto = "Quarto Duplo"
        self.qtd_camas = 2

    def __str__(self):
        return (f'Número do quarto: {self.numero_quarto}, Tipo do quarto: {self.tipo_quarto}, '
                f'Status do quarto: {self.status_quarto}, Preço do quarto: {self.preco_quarto}, '
                f'Tipo de cama: {self.tipo_cama}, Quantidade de camas: {self.qtd_camas}')



