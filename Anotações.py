#Arquivo de anotações dos arquivos principal


from flask import Flask, render_template

app = Flask(__name__)
#app == site, ou seja, isso é extremamente importante, pois permitirá o flask
# entender que esse aarquivo é um site, e também, iterigar os arquivos de front e back end
          #Dentro dos parênteses está o caminho da página, ou seja, em qual link a página estará disponível
@app.route('/')  #Essa função diz o que aparecerá dentro da página
def home():
    return render_template('home.html')

#@app.route() é um decorator, ou seja, é uma função que atribui uma nova funcionalidade para a função logo abaixo
# nesse caso, a funcionalidade é fazer a função "contatos aparecer no link específicaddo"
@app.route('/contato')
def contatos():
    return "Quanquer dúvda contactar o email: diogo.giarranti@gmail.com"

@app.route('/usuarios')
def usuarios():
    lista_usuarios = ['Diogo', 'Arthur', 'Marcel']
    #                       parâmetros: nome que eu quiser =nome da lista criada
    #                       (recomendado que o parâmetro receba o mesmo nome da variável, pois é mais lógico)
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

if __name__ =='__main__': #Serve para garantir que esse código só vai rodar se eu estiver rodando esse arquivo especificamente
    app.run(debug=True)#Pra alguma mudança ser feita no site, se faz necessára a reinicialização do código, para evitar isso:
                       # (debug=True)Isso faz com que toda mudança no código será altomaticamente implementada no site
                       # só precisa reiniciar a página do site

#Informações sobre htlm:
# Uma linguagem de, essencialmente, construção de paginas(p que irá aparecer, como vai aparecer, etc).
#Lógica HTML: Trabalha por tags, portando sempre abre e fecha: <x> ........ </x>. Ex:

#<!DOCTYPE html>
#<html lang="pt-br">
#    <head>                          No <head> é onde ficarão os scripts que farão coisas dinâmicas na pag,
#        <meta charset="UTF-8">      códigos de formatação(adicionar cor, etc),
#        <title>Title</title>        ou seja, ele não aparece quando a página é abeta
#    </head>
#    <body>                          No <body> é onde são colocadas as coisas que irâo aparecer na página
#
#    </body>
#</html>

#Informações sobre css e javascript nesse projeto:
#Linguagens de edição dentro de tags html

#Bootstrap:
