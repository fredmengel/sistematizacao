#hotel.py
from quarto import Quarto
from hospede import Hospede
from reserva import Reserva

class Hotel:
    """
    Representa um hotel com listas de quartos, hóspedes e reservas.

    Atributos:
        _quartos[]: Lista de quartos disponíveis no hotel.
        _hospedes[]: Lista de hóspedes registrados no hotel.
        _reservas[]: Lista de todas as reservas feitas no hotel.

        Incluído, além do que foi mencionado no diagrama da sistematização:
        _funcionarios[]: Lista os funcionários do hotel


    Métodos:
        add_quarto(self,quarto): Adiciona um quarto à lista de quartos do hotel.
        remover_quarto(self,quarto): Remove um quarto da lista de quartos do hotel.
        registrar_hospede(self,hospede): Adiciona um hóspede à lista de hóspedes do hotel.
        cancelar_reserva(self,reserva): Cancela uma reserva e libera o quarto associado.

        Incluídos, além do que foi mencionado no diagrama da sistematização:
        fazer_reserva(hospede, quarto): Faz uma reserva para um hóspede em um quarto, se disponível.
        consultar_reservas(): Retorna a lista de reservas do hotel.
    """
    def __init__(self):
        self._quartos=[]
        self._hospedes=[]
        self._reservas=[]
        self._funcionarios=[]
    
    def add_quarto(self,quarto):
        self._quartos.append(quarto)

    def remover_quarto(self,quarto):
        if quarto in self._quartos:
            self._quartos.remove(quarto)
        else:
            print("Quarto não encontrado.")
    
    def registrar_hospede(self,hospede):
        self._hospedes.append(hospede)
    
    def cancelar_reserva(self,reserva):
        if reserva in self._reservas:
            reserva._quarto.liberar()
            self._reservas.remove(reserva) #remove reserva da lista do hotel
            if reserva in reserva._hospede._reservas: #remove a reserva da lista do hóspede
                reserva._hospede._reservas.remove(reserva)
            print(f"Reserva para o quarto {reserva._quarto._numero} foi cancelada.")
        else:
            print("Reserva não encontrada.")

     
    def consultar_reservas(self):
        return self._reservas
    
    def add_funcionario(self, funcionario):
        self._funcionarios.append(funcionario)

    def remover_funcionario(self, funcionario):
        if funcionario in self._funcionarios:
            self._funcionarios.remove(funcionario)
        else:
            print("Funcionário não encontrado.")

    def listar_funcionarios(self):
        for funcionario in self._funcionarios:
            print(f"ID: {funcionario.get_id()}, Nome: {funcionario.get_nome()}, E-mail: {funcionario.get_email()}")

    def listar_quartos(self):
        print("Lista de quartos do Hotel:")
        for quarto in self._quartos:
            if quarto.estaDisponivel(): 
                disponibilidade = "Disponível" 
            else: 
                disponibilidade="Ocupado"
            print(f"Número: {quarto._numero}, Tipo: {quarto._tipo}, Disponibilidade: {disponibilidade}")
    
    def adicionar_reserva(self,reserva):
        self._reservas.append(reserva)