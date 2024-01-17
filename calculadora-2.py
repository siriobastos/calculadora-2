def calculadora():
    while True:
        print("\nOperações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = input("Digite o número para a operação desejada: ")

        if escolha == '0':
            print("Encerrando a calculadora. Adeus!")
            break
        elif escolha in {'1', '2', '3', '4'}:
            try:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))
            except ValueError:
                print("Erro: Insira valores numéricos válidos.")
                continue

            if escolha == '1':
                resultado = num1 + num2
                print(f"Resultado: {resultado}")
            elif escolha == '2':
                resultado = num1 - num2
                print(f"Resultado: {resultado}")
            elif escolha == '3':
                resultado = num1 * num2
                print(f"Resultado: {resultado}")
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {resultado}")
                else:
                    print("Erro: Divisão por zero.")
        else:
            print("Essa opção não existe. Tente novamente.")

if __name__ == "__main__":
    calculadora()
