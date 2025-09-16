#Quarto.py

class Quarto:
    """
    Representa um quarto de hotel com número, tipo e disponibilidade.

    Atributos:
        _numero (int): Número do quarto, que será um número inteiro.
        _tipo (str): Tipo de quarto (ex: Standard, Luxo, Duplo). Definico como string
        _disponivel (bool): Indica se o quarto está disponível para reserva, retorna True ou False (booleano)

    Métodos:
        reservar(self): Marca o quarto como reservado se estiver disponível.
        liberar(self): Marca o quarto como disponível.
        estaDisponivel(self): Retorna a disponibilidade do quarto.
    """

    def __init__(self,numero,tipo):
        self._numero=numero
        self._tipo=tipo
        self._disponivel=True
    
    def reservar(self):
        if self._disponivel: #Se estiver disponível, a condição é executada e transforma o self._disponivel em False (ocupado)
            self._disponivel=False
            return True #retorna True pois a reserva foi realizada com sucesso.
        return False #indica que a tentativa de reserva falhou porque o quarto já estava ocupado.

    def liberar(self):
        self._disponivel=True # transforma o self._disponivel em True (liberado)

    def estaDisponivel(self):
        return self._disponivel #retorna a informação sobre a disponibilidade do quarto (True ou False)