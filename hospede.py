#hospede.py
from pessoa import Pessoa
from reserva import Reserva



class Hospede(Pessoa):
    """
    Representa um hóspede. Pode fazer, cancelar e consultar suas próprias reservas
    A classe Hospede herda da classe Pessoa os atributos e métodos

    Atributos:
        _reservas[]: Lista de reservas feitas pelo hóspede.

    Métodos:
        fazer_reserva(self,reserva): Adiciona uma reserva à lista de reservas do hóspede.
        cancelar_reserva(self,reserva): Remove uma reserva da lista de reservas do hóspede.
        consultar_reservas(self): Retorna a lista de reservas do hóspede específico.
    """
    def __init__(self,id,nome,email):
        #A função super() chama o __init__ da classe-pai que foi importada (Pessoa). Assim, a classe Hospede herda os atributos definidos na classe Pessoa (_id, _nome e _email).
        super().__init__(id,nome,email)
        self._reservas=[] #trocar por list()?

    def fazer_reserva(self,quarto,hotel):
        if quarto.estaDisponivel():
            quarto.reservar()
            reserva = Reserva(self, quarto)
            self._reservas.append(reserva) #adiciona na lista de reservas do hospede
            hotel.adicionar_reserva(reserva) #adiciona na lista geral de reservas do hotel
            return reserva
        else:
            return None
    
    def cancelar_reserva(self,reserva,hotel):
        if reserva in self._reservas:
            reserva._quarto.liberar()
            self._reservas.remove(reserva) #remove a reserva do hóspede
            if reserva in hotel._reservas: #remove a reserva da lista do hotel
                hotel._reservas.remove(reserva)
            print(f"Reserva para o quarto {reserva._quarto._numero} foi cancelada.")
        else:
            print("Reserva não encontrada.")

    
    def consultar_reservas(self):
        return self._reservas
    
