
from imovel import Apartamento, Casa, Estudio
from orcamento import Orcamento

def menu():
    print("===== R.M IMOBILIÁRIA =====")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estudio")

    opcao = int(input("Escolha o tipo de imóvel: "))

    if opcao == 1:
        quartos = int(input("Quantidade de quartos (1 ou 2): "))
        garagem = input("Deseja garagem? (s/n): ").lower() == "s"
        possui_criancas = input("Possui crianças? (s/n): ").lower() == "s"
        imovel = Apartamento(quartos, garagem, possui_criancas)

    elif opcao == 2:
        quartos = int(input("Quantidade de quartos (1 ou 2): "))
        garagem = input("Deseja garagem? (s/n): ").lower() == "s"
        imovel = Casa(quartos, garagem)

    elif opcao == 3:
        vagas = int(input("Quantidade de vagas: "))
        imovel = Estudio(vagas)

    else:
        print("Opção inválida!")
        return

    orcamento = Orcamento(imovel)
    orcamento.mostrar_orcamento()
    orcamento.gerar_csv()


if __name__ == "__main__":
    menu()
