
import csv

class Orcamento:
    def __init__(self, imovel):
        self.imovel = imovel
        self.valor_contrato = 2000

    def mostrar_orcamento(self):
        print("\n===== ORÇAMENTO =====")
        print(f"Valor mensal do aluguel: R$ {self.imovel.calcular_valor():.2f}")
        print(f"Valor do contrato: R$ {self.valor_contrato:.2f}")
        print(f"Contrato parcelado em até 5x de R$ {self.valor_contrato / 5:.2f}")

    def gerar_csv(self):
        with open("parcelas.csv", "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Parcela", "Valor"])
            for i in range(1, 13):
                writer.writerow([i, self.imovel.calcular_valor()])
        print("Arquivo parcelas.csv gerado com sucesso!")
