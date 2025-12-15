while True:
    print("\n=== Calculadora ===")
    
    # 1. Receber números do usuário
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    # 2. Converter para float (aceita inteiros também)
    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        print("Valor inválido! Digite apenas números.")
        continue

    # 3. Mostrar opções ao usuário
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Opção: ")

    # 4. Fazer a operação com condicional
    if opcao == "1":
        resultado = num1 + num2
        print(f"\nResultado: {resultado}")
    elif opcao == "2":
        resultado = num1 - num2
        print(f"\nResultado: {resultado}")
    elif opcao == "3":
        resultado = num1 * num2
        print(f"\nResultado: {resultado}")
    elif opcao == "4":
        if num2 == 0:
            print("\nNão é possível dividir por zero!")
            continue
        resultado = num1 / num2
        print(f"\nResultado: {resultado}")
    else:
        print("\nOpção inválida!")
        continue

    # 5. Perguntar se deseja continuar
    repetir = input("\nDeseja fazer outra operação? (s/n): ").lower()
    if repetir != "s":
        print("\nEncerrando a calculadora... Até mais!")
        break