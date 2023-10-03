from math import cos, tan, sin, radians
angulo = float(input('Digite um ângulo: '))
anguloradiando = radians(angulo)

print('- '*12, '\nPara o ângulo {:.1f} \nO Seno é {:.2f} \nO Cosseno é {:.2f} \nE a Tangente é {:.2f} \n'.format( angulo, sin(anguloradiando), cos(anguloradiando), tan(anguloradiando)) ,'- '*12)

