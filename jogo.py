import os
import random
import sys

lista_palavras = [
"abelha",
"abutre",
"acaro",
"aguia",
"alce",
"alpaca",
"andorinha",
"anta",
"aranha",
"arara",
"asno",
"atum",
"avestruz",
"babuino",
"bacalhau",
"baiacu",
"baleia",
"barata",
"besouro",
"bezerro",
"bode",
"boi",
"borboleta",
"boto",
"bufalo",
"cabra",
"cachorro",
"camaleao",
"camarao",
"camelo",
"camundongo",
"canario",
"canguru",
"capivara",
"caracol",
"caranguejo",
"carneiro",
"carrapato",
"cascavel",
"castor",
"chita",
"coala",
"cobra",
"coelho",
"coruja",
"corvo",
"crocodilo",
"doninha",
"elefante",
"ema",
"enguia",
"esquilo",
"flamingo",
"flautim",
"foca",
"formiga",
"furao",
"gafanhoto",
"gaivota",
"galinha",
"galo",
"gamba",
"ganso",
"garça",
"gato",
"gaviao",
"gazela",
"girafa",
"girino",
"golfinho",
"gorila",
"gralha",
"grifo",
"grilo",
"hamster",
"hiena",
"hipopotamo",
"iguana",
"jabuti",
"jacare",
"jaguar",
"jamanta",
"jararaca",
"javali",
"jegue",
"jiboia",
"joaninha",
"lacraia",
"lagarta",
"lagartixa",
"lagarto",
"lagosta",
"leao",
"lebre",
"leopardo",
"lesma",
"lhama",
"lince",
"lobo",
"lontra",
"macaco",
"mamute",
"mariposa",
"marisco",
"marmota",
"marreco",
"mico",
"minhoca",
"morcego",
"morsa",
"mosca",
"mosquito",
"mula",
"narval",
"orangotango",
"orca",
"ornitorrinco",
"ostra",
"ovelha",
"panda",
"pantera",
"papagaio",
"pardal",
"pato",
"peixe",
"pelicano",
"peru",
"pinguim",
"piolho",
"piranha",
"polvo",
"pombo",
"porco",
"raia",
"raposa",
"ratazana",
"rato",
"rena",
"rinoceronte",
"sagui",
"salamandra",
"salmao",
"sapo",
"sardinha",
"serpente",
"siri",
"sucuri",
"suricate",
"tamandua",
"tartaruga",
"tatu",
"texugo",
"tigre",
"tordo",
"toupeira",
"touro",
"truta",
"tucano"
]

lista_letras_jogadas = []
string_letras_jogadas = ""
frase = ["___"]
frase_string = ""
vida = 7
vida_string = " "

palavra_do_dia = random.choice(lista_palavras).upper()
lista_letras_palavra_dia = list(palavra_do_dia)

i = 0
posicao_que_existe = []


def concatenarVida(vd):
    cont = 0
    vd = ""
    while cont < vida:
        vd += " ♥︎"
        cont += 1

    while cont < 7:
        vd += " ♡"
        cont+=1
    print("\nVidas:"+vd)


def concaternarFrase(fr):
    cont = 0
    while cont < len(frase): 
        fr+=frase[cont]
        cont+=1
    print(fr)


def concaternarLetrasJogadas(lts_jogadas):
    cont = 0
    while cont < len(lista_letras_jogadas):
        #Add espaços
        if(cont == 4 or (cont+4) % 8 == 0):
            lts_jogadas+="\n"

        #Add letra    
        lts_jogadas += lista_letras_jogadas[cont].upper() + " - "
        cont+=1
    print("Letras Jogadas: "+lts_jogadas+"\n")


def exibirMsg(let):
    print("========== ADIVINHE O ANIMAL ==========")
    i = 0

    if(len(posicao_que_existe) > 0):
        while i < len(posicao_que_existe):
            if(posicao_que_existe[i] == 0):
                frase[posicao_que_existe[i]] = " "+let.upper()+" "
                i+=1
            else:    
                frase[posicao_que_existe[i]] = ", "+let.upper()+" "
                i+=1


    concatenarVida(vida_string)
    if(vida == 0):
        print("\nINFELIZMENTE VOCÊ MORREU E PERDEU O JOGO\n\nO ANIMAL SECRETO ERA: "+palavra_do_dia)
        print("\n========================================\n")
        sys.exit()
    elif(len(lista_letras_palavra_dia) == len(juntaTudo)):
        print("\nPARABENS! VOCÊ GANHOU O JOGO!\n\nO ANIMAL SECRETO ERA: "+palavra_do_dia)
        print("\n========================================\n")
        sys.exit()
    else:
        concaternarLetrasJogadas(string_letras_jogadas)
        concaternarFrase(frase_string)
        

while i < (len(palavra_do_dia)-1):
    frase.append(",___")
    i+=1

juntaTudo = []

print("========== ADIVINHE O ANIMAL ==========")
print('Vidas: ♥︎ ♥︎ ♥︎ ♥︎ ♥︎ ♥︎ ♥︎\n')
concaternarFrase(frase_string)



while True:
    n = 0
    letra = input("Digite sua letra: \n")
    lista_letras_jogadas.append(letra)
    posicao_que_existe = []

    existe = True
    # Verifica se a letra jogada eciste na palavra
    j = 0
    while j < len(lista_letras_palavra_dia):
        if(lista_letras_palavra_dia[j] == letra.upper()):
            posicao_que_existe.append(j)
            existe = False
            juntaTudo.append(j)
        j+=1

    if(existe):
        vida -= 1
    
    #limpa terminal e exibe as msg
    os.system('cls')
    exibirMsg(letra)