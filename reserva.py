#reserva.py

class Reserva:
    """
    Representa uma reserva de um quarto para um hóspede.

    Atributos:
        _hospede (Hospede): O hóspede associado à reserva.
        _quarto (Quarto): O quarto associado à reserva.
    """
    def __init__(self,hospede,quarto):
        self._hospede=hospede
        self._quarto=quarto