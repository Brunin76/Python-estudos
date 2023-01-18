while True:
    try:
        tabuada = int(input('Entre com um número inteiro e positivo: '))
        if tabuada == -1:
            break
        for i in range(11):
            print(f'{tabuada}x{i}={tabuada*i}')
    except:
        pass