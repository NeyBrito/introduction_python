from aula6Televisao import Televisao
from aula8ContadorLetras import contador_letras



if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    lista = ['cachorro','gato','elefante']
    print(contador_letras(lista))
valida_numero = {
    'par': lambda a: True if a % 2 == 0 else False,
    'impar': lambda b: True if b % 2 == 0 else False
}
resultado = valida_numero['par'](10)
print(resultado)