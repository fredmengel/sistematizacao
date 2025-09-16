#funcionario.py
from pessoa import Pessoa


class Funcionario(Pessoa): 
    """
    Representa um funcionário, que a pessoa que pode gerenciar os quartos e hóspedes em um hotel.
    A classe Funcionario herda da classe Pessoa os atributos e métodos

    Métodos:
        add_quarto(self,hotel, quarto): Adiciona um quarto ao hotel.
        remover_quarto(self,hotel, quarto): Remove um quarto do hotel.
        registrar_hospede(self,hotel, hospede): Registra um hóspede no hotel.
        cancelar_reserva(self,hotel, reserva): Cancela uma reserva no hotel.
    """
    def add_quarto(self, hotel, quarto):
        hotel.add_quarto(quarto)

    def remover_quarto(self,hotel,quarto):
        hotel.remover_quarto(quarto)
    
    def registrar_hospede(self,hotel,hospede):
        hotel.registrar_hospede(hospede)
    
    def cancelar_reserva(self,hotel,reserva):
        hotel.cancelar_reserva(reserva)