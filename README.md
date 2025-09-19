# 🏨 Sistema de Gerenciamento de Hotel

Este é um **protótipo didático** desenvolvido para a disciplina de **Engenharia e Projeto de Software**.  
O sistema foi implementado em **Python 3.x** utilizando conceitos de **Programação Orientada a Objetos (POO)**, com foco em aplicar **engenharia de requisitos, modelagem UML e testes**.

---

## 📌 Objetivo
O sistema visa facilitar o **gerenciamento de hotéis de pequeno porte**, permitindo:  
- Cadastro de **hóspedes** e **funcionários**;  
- Cadastro e gerenciamento de **quartos**;  
- Criação e cancelamento de **reservas**;  
- Consulta de reservas por hóspede ou pelo hotel.  

---

## ⚙️ Funcionalidades
- **Funcionário**
  - Adicionar/remover quartos no hotel
  - Registrar hóspedes
  - Cancelar reservas
- **Hóspede**
  - Fazer reservas em quartos disponíveis
  - Cancelar reservas existentes
  - Consultar reservas próprias
- **Hotel**
  - Listar quartos (disponíveis/ocupados)
  - Listar funcionários
  - Consultar reservas ativas

---

## 📐 Modelagem (UML)
- **Casos de Uso**: cadastro, reservas, cancelamentos e consultas.  
- **Diagrama de Classes**: entidades `Hotel`, `Quarto`, `Hospede`, `Funcionario`, `Reserva`, `Pessoa`.  
- **Diagrama de Sequência**: fluxo de **fazer reserva** e **cancelar reserva**.  

*(Os diagramas completos estão disponíveis no relatório do projeto.)*

---

## 🖥️ Arquitetura
- **Camadas simples**: cada entidade implementada em um arquivo `.py`;  
- **Dados em memória** (listas Python);  
- **Execução em CLI** (`main.py`) para demonstrar o funcionamento.  

---

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/sistema-hotel.git
   cd sistema-hotel
   ```
2. Execute o programa:
   ```bash
   python main.py
   ```
3. Acompanhe no console a execução de cadastros, listagens, reservas e cancelamentos.

---

## ✅ Testes
Foram criados **testes unitários** em `unittest` para verificar:  
- Fluxo de reserva e cancelamento de quartos;  
- Prevenção de reservas duplicadas;  
- Estado de disponibilidade dos quartos.  

Para rodar os testes:
```bash
python -m unittest discover tests
```

---

## 📊 Requisitos Atendidos
- **RF001–RF008**: funcionalidades principais de cadastro, reservas e consultas.  
- **RNF001–RNF006**: usabilidade, desempenho, portabilidade, manutenibilidade e segurança básica.  

---

## 📚 Referências
- Pressman, R. S. *Engenharia de Software – Uma Abordagem Profissional*.  
- Sommerville, I. *Engenharia de Software*. 10ª ed. Pearson.  
- Documentação oficial Python: [https://docs.python.org/3](https://docs.python.org/3)

---

## ✨ Próximos Passos
- Implementar **datas de check-in/check-out** nas reservas;  
- Persistência em **SQLite/JSON**;  
- Interface gráfica (Tkinter/PyQt) ou versão web (Flask/FastAPI);  
- Relatórios de ocupação e histórico de reservas.  


