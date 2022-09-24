from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def bem_vindo():
    return render_template("home.html")


'''def escolha():
    print('O que deseja fazer?')
    esc = input('Digite (i) incluir, (d) deletar, (b) buscar uma pessoa ou (s) para sair\n')

    if(esc == 'i' or esc == 'I'):
        incluir()

    if(esc == 'd' or esc == 'D'):
        deletar()

    if(esc == 'b' or esc == 'B'):
        buscar()

    if(esc == 's' or esc == 'S'):
        print('Agradeco pela preferencia, ate outro dia!')
    
    else:
        print('Comando invalido!')
        return escolha()


def incluir():
    print('Quem voce deseja incluir?')
    nome = input('Digite seu nome: ')
    email = input('Digite seu emal: ')
    cel = input('Digite seu celular: ')
    contato = [email, cel]
    agenda[nome] = contato
    #agenda.update(aloc)

    print(nome, ':', email, ',', cel, '\nContato salvo com sucesso!')

    return escolha()


def buscar():
    nome = input('Digite o nome do contato que voce procura: ')
    comp = nome in agenda
    if(comp == False):
        print('Esse contato nao existe!')

    else:
        print(agenda[nome])

    return escolha()


def deletar():
    nome = input('Digite o nome do contado que deseja deletar: ')
    comp = nome in agenda
    if(comp == False):
        print('Esse contato nao existe!')

    else:
        del agenda[nome]
        print('Contato deletado com sucesso!')

    return escolha()

escolha()'''


app.run()