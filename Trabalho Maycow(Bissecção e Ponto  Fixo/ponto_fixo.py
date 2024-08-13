def ponto_fixo():
    def raiz_ponto_fixo(xo, funcx,funcao_g, precisao, nIteracao):
        k = 1
        while k <= nIteracao:
            x1 = funcao_g(xo)

            if abs(x1 - xo) < precisao:
                x_barra = x1
                return x_barra, k

            xo = x1
            k += 1

        raise Exception(f"O método de ponto fixo não convergiu após {nIteracao} iterações.")

    funcx = input("Digite a expressão da F(X): ")
    funcao_str = input("Digite a expressão da função G(X): ")
    funcao = lambda x: eval(funcao_str)

    xo = float(input("X.o inicial: "))
    precisao = float(input("Taxa de Erros: "))
    num_interacao = 1
    contador = 0
    raiz = None
    k = None
    while raiz is None and k is None:
        try:
            raiz, k = raiz_ponto_fixo(xo, funcx, funcao, precisao, num_interacao)
        except:
            num_interacao += 1
    for i in range(len(str(precisao))):
        contador += 1
    print('=' * 20)
    print('Resultado')
    print('=' * 20)
    print(f'\nValor aproximado da raiz: {raiz:.{contador-2}f}\nInterações: {k}')
