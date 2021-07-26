import shutil

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_notas = arquivo.read()
    #print(aluno_notas)
    aluno_notas = aluno_notas.split('\n')
    #print(aluno_notas)

    lista_media = []

    for x in aluno_notas:
        lista_notas = x.split(',')
        # print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo,'C:/Projeto/globallabs/')

def move_aquivo(nome_arquivo):
    shutil.move(nome_arquivo,'C:/Projeto/globallabs/')


if __name__ == '__main__':
    move_aquivo('notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira linha. \n')
    # aluno = '\nCesar, 7, 9, 3, 8'
    # atualizar_arquivo('notas.txt', notas)
    # ler_arquivo('teste.txt')

resultado = 'João programa em Python, Java, PHP e Ruby'.split('!')
print(resultado)

import shutil
texto = 'Primeira linha\nSegunda linha'
file = open('arquivo.txt', 'w')
file.write(texto)
file.close()
shutil.copy('arquivo.txt', 'backup.txt')
texto_split = texto.split('\n')
print(texto_split)