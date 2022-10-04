from ast import Break
import math 

angulo = int(input("Digite um angulo : "))
    
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo de {}° tem o SENO de {:.3f}'.format(angulo, seno))
print('O ângulo de {}° tem o COSSESENO de {:.3f}'.format(angulo, cosseno))
print('O ângulo de {}° tem o TANGENTE de {:.3f}'.format(angulo, tangente))


a = (input("fim, aperte enter para fechar."))
Break