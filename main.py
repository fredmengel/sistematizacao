#Link vídeo: https://youtu.be/pK-O9k59HUA
#Link Replit: https://replit.com/@fredengel/sistematizacao-projeto-3
#Link GitHub: https://github.com/fredmengel/sistematizacao

#main.py
from funcionario import Funcionario
from hospede import Hospede
from hotel import Hotel
from quarto import Quarto

def main():
    hotel=Hotel()

    funcionario1 = Funcionario(1, "Leonardo Rebouças", "leonardo@hotel.com")
    hotel.add_funcionario(funcionario1)

    funcionario2 = Funcionario(2, "Ana Pereira", "ana@hotel.com")
    hotel.add_funcionario(funcionario2)
    hotel.listar_funcionarios()
    #hotel.remover_funcionario(funcionario1)
    print("-="*30)
    
    quarto1 = Quarto(101, "Standard")
    funcionario1.add_quarto(hotel, quarto1)

    quarto2 = Quarto(102, "Duplo")
    funcionario2.add_quarto(hotel, quarto2)

    quarto3 = Quarto(103, "Família")
    funcionario1.add_quarto(hotel, quarto3)
    hotel.listar_quartos()
    print("-="*30)
    hospede1 = Hospede(1, "Caroline Silva", "caroline@hospede.br")
    funcionario1.registrar_hospede(hotel, hospede1)

    hospede2 = Hospede(2, "Maria do Bairro", "mariadobairro@sbt.tv")
    funcionario2.registrar_hospede(hotel, hospede2)

    reserva1 = hospede1.fazer_reserva(quarto1, hotel)
    if reserva1: #verifica se foi bem sucedida a reserva
        print(f"Reserva realizada para o quarto {quarto1._numero} por {hospede1.get_nome()}")
    else:
        print(f"Quarto não disponível para reserva. Escolher outro quarto para {hospede1.get_nome()}")
    
    reserva2 = hospede2.fazer_reserva(quarto1, hotel)
    if reserva2:
        print(f"Reserva realizada para o quarto {quarto1._numero} por {hospede2.get_nome()}")
    else:
        print(f"Quarto não disponível para reserva. Escolher outro quarto para {hospede2.get_nome()}")
    
    print("-="*30)
    hospede1.cancelar_reserva(reserva1, hotel)

    print("-="*30)
    reserva2 = hospede2.fazer_reserva(quarto1, hotel)
    if reserva2:
        print(f"Reserva realizada para o quarto {quarto1._numero} por {hospede2.get_nome()}")
    else:
        print(f"Quarto não disponível para reserva. Escolher outro quarto para {hospede2.get_nome()}")




if __name__=="__main__":
    main()



