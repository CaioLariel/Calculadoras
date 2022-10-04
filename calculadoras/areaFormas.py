from ast import Break


print('vamos calcular a área')
an = int(input('''qual forma vc gostaria de descobrir o valor da área?:
                     [1] triângulo.
                     [2] quadrado(equilátero).
                     [3] losango.
                     [4] trapézio.
                     Sua opção:
                     '''))
if an == 1:
    b = float(input('qual valor da base do triângulo? ='))
    h = float(input('qual valor da altura do triângulo? ='))
    op = (b * h) / 2
    print('área do triângulo = ', op)
if an == 2:
    l = float(input('qual valor do lado do quadrado? ='))
    ap = (l * l)
    print('área do quadrado = ', ap)
if an == 3:
    dm = float(input('qual valor da diagonal maior do losango? ='))
    dp = float(input('qual valor da diagonal menor do losango? ='))
    al = (dm * dp) / 2
    print('área do losango = ', al)
if an == 4:
    bm = float(input('qual valor da base maior do trapézio? ='))
    bp = float(input('qual valor da base menor do trapézio? ='))
    h = float(input('qual valor da altura do trapézio? ='))
    at = h * (bm + bp) / 2
    print('área do trapézio = ', at)

a = (input("fim, aperte enter para fechar."))
Break