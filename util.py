# -*- coding: utf-8 -*-

""" 
    Arquivo que armazena funções adicionais, variáveis/constantes globais e dados previos de manutenção do sistema

"""


import string
import random
from pytz.gae import pytz
from pytz import timezone


local_tz = pytz.timezone('Brazil/East')
BASE_URL= "http://livraria-js.appspot.com/"

"""
    Função que retorna a timezone adequada para conexão com o servidor AppEngine
"""
def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)


"""
    Função que gera um identificador aleatório utilizado para o token de login
"""
def id_generator(size=25, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


"""
    Dados e estruturas de dados para exemplos e testes
"""

lista_default = [
{
"urlCapa": "http://i430.photobucket.com/albums/qq29/unifei-itabira-bilbioteca/InteligenciaArtificialStuartRussell.jpg",
"urlDeletaLivro": "http://v4.livraria-js.appspot.com/deletarLivro?id=va8XSjYW0adpSS6dLwaCxqlfD",
"preco": "219,90",
"urlGetCometarios": "http://v4.livraria-js.appspot.com/getComentarios?idlivro=va8XSjYW0adpSS6dLwaCxqlfD",
"titulo": "Livro - Inteligencia Artificial",
"autores": "Russell, Norvig",
"data": "06/04/16 - 23:31",
"id": "va8XSjYW0adpSS6dLwaCxqlfD",
"desc": "A primeira edição de Inteligência artificial: uma abordagem moderna se tornou um clássico na literatura sobre IA. O livro foi adotado por mais de 600 universidades de 60 países e foi elogiado como a síntese definitiva desse campo. Nesta segunda edição, todos os capítulos foram extensivamente reescritos. Foi introduzida uma quantidade significativa de material novo, abrangendo áreas como: satisfação de restrições, inferência proposicional rápida, grafos de planejamento, agentes de inter-redes, inferência probabilística exata, técnicas de Markov Chain Monte Carlo, filtros de Kalman, métodos de aprendizado harmonioso, aprendizado estatístico, modelos probabilísticos de linguagens naturais, robótica probabilística e aspectos éticos da IA."
},
{
"urlCapa": "http://3.bp.blogspot.com/-umADLKwLxNA/VfW-9wmpaKI/AAAAAAAABbU/roqu_6SukSQ/s1600/download.jpg",
"urlDeletaLivro": "http://v4.livraria-js.appspot.com/deletarLivro?id=XOHZCuKDUCZXdAtg1OFFpXv98",
"preco": "34,90",
"urlGetCometarios": "http://v4.livraria-js.appspot.com/getComentarios?idlivro=XOHZCuKDUCZXdAtg1OFFpXv98",
"titulo": "O Silmarillion",
"autores": "J. R. R. Tolkien",
"data": "06/04/16 - 23:31",
"id": "XOHZCuKDUCZXdAtg1OFFpXv98",
"desc": "O Silmarillion, relata acontecimentos de uma época muito anterior ao final da Terceira Era, quando ocorreram os grandes eventos narrados em O Senhor dos Anéis. São lendas derivadas de um passado remoto, ligadas às Silmarils, três gemas perfeitas criadas por Fëanor, o mais talentoso dos elfos. Tolkien trabalhou nesses textos ao longo de toda a sua vida, tornando-os veículo e registro de suas reflexões mais profundas."
},
{
"urlCapa": "http://i430.photobucket.com/albums/qq29/unifei-itabira-bilbioteca/IntroducaoTeoriaComputacao.jpg",
"urlDeletaLivro": "http://v4.livraria-js.appspot.com/deletarLivro?id=xfM9JP1A1uh61TU8TXFMrWXlC",
"preco": "69,70",
"urlGetCometarios": "http://v4.livraria-js.appspot.com/getComentarios?idlivro=xfM9JP1A1uh61TU8TXFMrWXlC",
"titulo": "Introdução À Teoria da Computação",
"autores": "Sipser, Michael",
"data": "06/04/16 - 23:31",
"id": "xfM9JP1A1uh61TU8TXFMrWXlC",
"desc": "Esta obra apresenta a teoria da computação por meio de teoremas e provas, sempre com a preocupação do autor em mostrar a intuição por trás de cada resultado e em amenizar a leitura destas últimas, apresentando, para cada teorema, uma idéia da prova."
},
{
"urlCapa": "http://ecx.images-amazon.com/images/I/61ChgMff%2BzL._SX371_BO1,204,203,200_.jpg",
"urlDeletaLivro": "http://v4.livraria-js.appspot.com/deletarLivro?id=9ZvcOReRwGjDLMap8WFVzxvg0",
"preco": "176,70",
"urlGetCometarios": "http://v4.livraria-js.appspot.com/getComentarios?idlivro=9ZvcOReRwGjDLMap8WFVzxvg0",
"titulo": "Redes de Computadores",
"autores": "Tanenbaum ",
"data": "06/04/16 - 23:31",
"id": "9ZvcOReRwGjDLMap8WFVzxvg0",
"desc": "Este clássico best-seller foi totalmente atualizado e passa a abordar as redes desenvolvidas a partir de 1990. Entretanto, há partir do ano 2000 também há uma grande quantidade de novos desenvolvimentos. O mais importante é o enorme crescimento das redes sem fio, incluindo 802.11, loops locais sem fio, redes celulares 2G e 3G, Bluetooth, WAP, i-mode e outras. Acompanhando essa tendência, incluímos neste volume uma grande quantidade de material sobre redes sem fi"
},
{
"urlCapa": "http://img.travessa.com.br/livro/BA/c9/c97beeef-26e5-458e-85ec-0162bbf0d7b1.jpg",
"urlDeletaLivro": "http://v4.livraria-js.appspot.com/deletarLivro?id=xvgbsV0uxV5HuDNyWe4EwblMc",
"preco": "71,90",
"urlGetCometarios": "http://v4.livraria-js.appspot.com/getComentarios?idlivro=xvgbsV0uxV5HuDNyWe4EwblMc",
"titulo": "A Origem Das Espécies",
"autores": "Darwin, Charles",
"data": "06/04/16 - 23:31",
"id": "xvgbsV0uxV5HuDNyWe4EwblMc",
"desc": "Ainda considerado como um dos mais inovadores e desafiantes tratados biológicos já escritos, A origem das espécies, com sua abordagem sobre os processos evolutivos, chocou grande parte do mundo ocidental, quando foi lançando em 1859. Charles Darwin apresentou aos seus primeiros leitores as teorias da seleção natural, dando inicio a discussões fervorosas sobre o tema. "
},
{
"urlCapa": "http://ecx.images-amazon.com/images/I/51FWXX9KWVL._AC_UL320_SR248,320_.jpg",
"urlDeletaLivro": "http://v4.livraria-js.appspot.com/deletarLivro?id=zBudyTzcil5q4Uy024LOMEKK4",
"preco": "180,00",
"urlGetCometarios": "http://v4.livraria-js.appspot.com/getComentarios?idlivro=zBudyTzcil5q4Uy024LOMEKK4",
"titulo": "Compiladores - Princípios, Técnicas e Ferramenta",
"autores": "Alfred V. Aho, Ravi Sethi, Jeffrey D. Ullman",
"data": "06/04/16 - 23:31",
"id": "zBudyTzcil5q4Uy024LOMEKK4",
"desc": "Compiladores, de Alfred V. Aho e Jeffrey D. Ullman, começa com uma introdução às principais idéias por trás da compilação e, em seguida ilustra-as através da construção de um compilador simples de uma passagem. O restante do livro amplia as idéias apresentadas nos dois primeiros capítulos e discute tópicos mais avançados, tais como a análise sintática, a verificação de tipos e a geração e otimização de código."
},
{
"urlCapa": "http://www.tblivraria.com.br/capas/287/9788588639287.jpg",
"urlDeletaLivro": "http://v4.livraria-js.appspot.com/deletarLivro?id=401s8FgQ1yYaxuNVMrEXdd6hx",
"preco": "183,84",
"urlGetCometarios": "http://v4.livraria-js.appspot.com/getComentarios?idlivro=401s8FgQ1yYaxuNVMrEXdd6hx",
"titulo": "ENGENHARIA DE SOFTWARE",
"autores": "SOMMERVILLE, IAN",
"data": "06/04/16 - 23:31",
"id": "401s8FgQ1yYaxuNVMrEXdd6hx",
"desc": "Desde a primeira edição deste livro, publicada há mais de vinte anos, muitos dos processos relacionados a hardware e software mudaram, e de modo extraordinário. Naquela época, o software era então destinado principalmente a mainframes, e os computadores pessoais ainda não eram tão populares como hoje. Jamais imaginaríamos o quanto eles invadiriam nossa vida nem quanto eles mudariam o mundo.A capacidade de os engenheiros de software criarem sistemas grandes e complexos certamente aumentou na era da computação pessoal. Nos últimos anos, os avanços mais importantes na engenharia de software foram o aparecimento da UML como padrão para a descrição de sistemas orientados a objetos e o desenvolvimento de métodos ágeis, como a extreme programming."
},
{
"urlCapa": "http://2.bp.blogspot.com/-OY0ENUlcFEI/VVR-Gv8ygVI/AAAAAAAAAKQ/pWvceM1Wwm0/s320/1939597_4.jpg",
"urlDeletaLivro": "http://v4.livraria-js.appspot.com/deletarLivro?id=pjVKplWktcFM89juupsRU06Cw",
"preco": "125,00",
"urlGetCometarios": "http://v4.livraria-js.appspot.com/getComentarios?idlivro=pjVKplWktcFM89juupsRU06Cw",
"titulo": "Estrutura de Dados e Algoritmos em Java",
"autores": "Michael T Goodrich, Roberto Tamassia ",
"data": "06/04/16 - 23:31",
"id": "pjVKplWktcFM89juupsRU06Cw",
"desc": "Este livro oferece uma introdução a estruturas de dados e algoritmos, incluindo projeto, análise e implementação. Em um texto simples e claro, os autores utilizam recursos visuais e cenários do mundo real, focando as funções mais populares na análise de algoritmos."
},
{
"urlCapa": "http://mlb-s2-p.mlstatic.com/java-como-programar-6-edico-deitel-360801-MLB20396065099_082015-O.jpg",
"urlDeletaLivro": "http://v4.livraria-js.appspot.com/deletarLivro?id=AVpotLhMg1EaEFO2YwtqVAXs5",
"preco": "100,00",
"urlGetCometarios": "http://v4.livraria-js.appspot.com/getComentarios?idlivro=AVpotLhMg1EaEFO2YwtqVAXs5",
"titulo": "Java - Como Programar",
"autores": "Deitel",
"data": "06/04/16 - 23:31",
"id": "AVpotLhMg1EaEFO2YwtqVAXs5",
"desc": "O best seller escrito pela familia Deitel chega a 6ª edição com tradução e revisão técnica de primeira qualidade, cobrindo pontos fundamentais para o aprendizado da programação Java em sua essência. Totalmente atualizada com Java 2 Platform Standard Edition (J2SE) 1.5, traz uma infinidade de exercícios práticos, orientados para o nível básico e intermediário."
},
{
"urlCapa": "http://ecx.images-amazon.com/images/I/410Yirblc6L._SX387_BO1,204,203,200_.jpg",
"urlDeletaLivro": "http://v4.livraria-js.appspot.com/deletarLivro?id=G24DYC1piDKHJDBigWQzhUQZg",
"preco": "107,74",
"urlGetCometarios": "http://v4.livraria-js.appspot.com/getComentarios?idlivro=G24DYC1piDKHJDBigWQzhUQZg",
"titulo": "ANGULARJS",
"autores": "PANDA, SANDEEP",
"data": "06/04/16 - 23:31",
"id": "G24DYC1piDKHJDBigWQzhUQZg",
"desc": "AngularJS: Novice to Ninja is your fast track route to mastering AngularJS, the superheroic JavaScript framework. AngularJS provides the fastest, most efficient way to build single page web applications."
}
]

lista_comentarios = [
{
"urlGetLivro": "http://v4.livraria-js.appspot.com/getLivro?id=XOHZCuKDUCZXdAtg1OFFpXv98",
"idlivro": "XOHZCuKDUCZXdAtg1OFFpXv98",
"usuario": "Antonio",
"conteudo": "Muito bom!",
"data": "06/04/16 - 20:34",
},
{
"urlGetLivro": "http://v4.livraria-js.appspot.com/getLivro?id=va8XSjYW0adpSS6dLwaCxqlfD",
"idlivro": "va8XSjYW0adpSS6dLwaCxqlfD",
"usuario": "Gloria Pires",
"conteudo": "Não sou capaz de opinar...",
"data": "06/04/16 - 20:34",
},
{
"urlGetLivro": "http://v4.livraria-js.appspot.com/getLivro?id=va8XSjYW0adpSS6dLwaCxqlfD",
"idlivro": "va8XSjYW0adpSS6dLwaCxqlfD",
"usuario": "Antonio",
"conteudo": "Bom livro.",
"data": "06/04/16 - 20:35",
}
]
