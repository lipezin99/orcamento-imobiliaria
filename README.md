
# 🏠 Sistema de Orçamento de Aluguel – R.M Imobiliária

## 📖 Sobre o Projeto

Este projeto foi desenvolvido para automatizar a geração de orçamentos de aluguel para a empresa R.M Imobiliária.

A aplicação calcula automaticamente o valor mensal do aluguel com base nas regras de negócio definidas, aplica descontos quando necessário e gera um arquivo `.csv` contendo as 12 parcelas do orçamento.

---

## 🎯 Objetivo

Automatizar o processo de geração de orçamento de imóveis para aluguel, aplicando:

- Regras de cálculo por tipo de imóvel
- Acréscimos por quartos e garagem
- Descontos específicos
- Cálculo do contrato imobiliário
- Geração de relatório em CSV

---

## 🧠 Conceitos Aplicados

- Pensamento Algorítmico
- Programação Orientada a Objetos (POO)
- Herança
- Encapsulamento
- Modularização
- Manipulação de Arquivos (CSV)

---

## 🏗 Estrutura do Projeto

orcamento_imobiliaria/
│
├── main.py
├── imovel.py
├── orcamento.py
├── README.md

---

## 🏢 Regras de Negócio

### Valores Base:

- Apartamento: R$ 700,00 (1 quarto)
- Casa: R$ 900,00 (1 quarto)
- Estúdio: R$ 1.200,00

### Regras adicionais:

- Apartamento com 2 quartos: + R$ 200,00
- Casa com 2 quartos: + R$ 250,00
- Garagem (casa/apartamento): + R$ 300,00
- Estúdio:
  - 2 vagas: + R$ 250,00
  - Vagas adicionais: + R$ 60,00 cada
- Desconto de 5% para apartamentos (sem crianças)
- Contrato imobiliário: R$ 2.000,00 parcelado em até 5x

---

## ▶️ Como Executar

1. Instale o Python 3.
2. Abra o terminal na pasta do projeto.
3. Execute:

python main.py

4. Siga as instruções exibidas no terminal.
5. O arquivo `parcelas.csv` será gerado automaticamente.

---

## 🎓 Trabalho Acadêmico

Disciplina: Algorithmic Thinking & Introduction to Object-Oriented Programming

---

## 👨‍💻 Autor

Coloque seu nome aqui
