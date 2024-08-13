def bissecao():

    def f(x):
        # Substitua a função pela expressão fornecida pelo usuário
        return eval(funcao.replace('x', str(x)))

    def bissecao(a, b, epsilon):
        k = 1
        while True:
            x = (a + b) / 2
            M = f(a)

            if abs(b - a) < epsilon or M == 0:
                return x, k

            if M * f(x) > 0:
                a = x
            else:
                b = x

            k += 1

    # Dados iniciais
    funcao = input("Digite a f(X): ")
    a = float(input("Qual o primeiro intervalo:? "))
    b = float(input("Qual o segundo intervalo:? "))
    epsilon = float(input("Qual a taxa de erro:? "))
    contador = 0
    resultado, k = bissecao(a, b, epsilon)
    for i in range(len(str(epsilon))):
        contador += 1
    print(f"Valor aproximado da Raiz: {resultado:.{contador-2}f}\nInterações: {k}")