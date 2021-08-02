/*   
 * Script Angular JS - Livraria JS
*/

(function () {
var app = angular.module('livrariaJS', [])
 .service('loginUsuario', function () {
        var login = {status:false};

        return {
            getProperty: function () {
                return login;
            },
            setProperty: function(updateLogin) {
                login = updateLogin;
            }
        };
});

//altera o separador de formatacao AngularJS para evitar confiltos com webapp
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});


app.controller('livrariaJSController', function($scope, $http, loginUsuario) {

    //variaveis de controle do modulo

    $scope.login = loginUsuario.getProperty();
    $scope.exibeEdicao = false;
    $scope.indice = 0;
    $scope.searchKeyword = "";

    $scope.listaDeLivros = []; 
    $scope.livroSelecionado = {}; 

    //Funcao que carrega comentarios de um usuario do servidor
    $scope.updatecomentarios = function() {
        try {
            var livro = $scope.listaDeLivros[$scope.indice]
            //HTTP GET            
            $http.get('getComentarios?idlivro=' + livro.id).
            success(function(comentarios) {
                $scope.livroSelecionado.comentarios = comentarios;
            });
        } catch(err) {
            console.log('Sem livros cadastrados!');
        }
    };


    //carrega lista de livros do servidor
    $scope.carregaLivros = function() {
        //HTTP GET
        $http.get('getLivros').
        success(function(data) {
            $scope.listaDeLivros = data;
            console.log($scope.listaDeLivros);
            $scope.livroSelecionado = $scope.listaDeLivros[$scope.indice];
            $scope.updatecomentarios();  
        });

    }

    $scope.carregaLivros();

    //funcao para adicionar um novo livro
    $scope.addLivro = function(livro) {
        livro.comentarios = [];
        if (livro.urlCapa == undefined || livro.urlCapa == "")
            livro.urlCapa = "images/capa_livro.png";

        $scope.listaDeLivros.push(angular.copy(livro));
        $scope.indice = $scope.listaDeLivros.length - 1;
        $scope.livroSelecionado = $scope.listaDeLivros[$scope.indice];
        var url = "inserirLivro?titulo=" + livro.titulo + "&desc=" + livro.desc +
            "&autores=" + livro.autores + "&preco=" + livro.preco + "&urlCapa=" + livro.urlCapa;
        $scope.limpaCampos(livro);
        window.open("#books-view", "_self")
        console.log(url)

        // HTTP POST
        $http.post(url).
        success(function(data) {
            console.log(data);
            $scope.carregaLivros();
        });
    };

    //funcoes de controle dos paineis da interface

    $scope.desativaAddArea = function() {
        window.open("#inicio", "_self")
    };

    // Funcoes de controle ativa/desativa modo de edicao delivro
    $scope.livro_nao_editado = {};
    $scope.ativaEdicao = function() {
        $scope.livro_nao_editado = angular.copy($scope.listaDeLivros[$scope.indice])
        console.log($scope.livro_nao_editado);
        $scope.exibeEdicao = $scope.exibeEdicao ? false : true;
    };

    $scope.limpaCampos = function(lista) {
        for (var chave in lista) {
            lista[chave] = null;
        }
    };

    // Funcao que volta a lista geral para o livro anterior
    $scope.previous = function() {
        $scope.incrementa(-1);
        $scope.updatecomentarios();
    };

    // Funcao que avança a lista geral para o próximo livro
    $scope.next = function() {
        $scope.incrementa(1);
        $scope.updatecomentarios();
    };

    //funcao que incrementa o livro corrente no painel de listagem
    $scope.incrementa = function(incremento) {

        console.log($scope.login);
        var len = $scope.listaDeLivros.length;
        $scope.indice = ((($scope.indice + incremento) + len) % len)
        $scope.livroSelecionado = $scope.listaDeLivros[$scope.indice];
    };

    //funcao que adiciona um novo comentario no livro corrente
    $scope.postarComentario = function(comentario) {
        comentario.data = new Date();
        console.log(comentario.data);
        comentario.usuario = $scope.login.nome + " " + $scope.login.sobrenome
        $scope.listaDeLivros[$scope.indice].comentarios.push(angular.copy(comentario));
        var idlivro = $scope.listaDeLivros[$scope.indice].id;
        var url = "postarComentario?idlivro=" + idlivro + "&usuario=" + comentario.usuario +
            "&conteudo=" + comentario.conteudo + "&data=" + comentario.data.toString().substring(4, 24);
        $scope.limpaCampos(comentario);
        console.log(url)
        $http.post(url).
        success(function(data) {
            console.log(data)
            // $scope.updatecomentarios();
        });
    };

    //funcao que envia para o servidor as mudanças feitas na edição do livro
    $scope.salvaEdicao = function() {
        var livro = $scope.listaDeLivros[$scope.indice];
        var url = "updateLivro?id=" + livro.id + "&titulo=" + livro.titulo + "&desc=" + livro.desc +
            "&autores=" + livro.autores + "&preco=" + livro.preco + "&urlCapa=" + livro.urlCapa;
        console.log(url)
        //HTTP PUT
        $http.put(url).
        success(function(data) {
            console.log(data)
        });
        window.alert("Alterações feitas com sucesso!");
        $scope.ativaEdicao();
    };

    //funcao que cancela as modificaçãos feitas na edição
    $scope.cancelaEdicao = function() {
        console.log($scope.livro_nao_editado);
        livro = $scope.listaDeLivros[$scope.indice];
        livro.titulo = $scope.livro_nao_editado.titulo;
        livro.autores = $scope.livro_nao_editado.autores;
        livro.desc = $scope.livro_nao_editado.desc;
        livro.preco = $scope.livro_nao_editado.preco;
        livro.urlCapa = $scope.livro_nao_editado.urlCapa;
        $scope.ativaEdicao();
    };

    //Função que mostra as informações de um livro selcionado na sessão de busca
    $scope.selecionaLivro = function(livro) {
        $scope.indice = $scope.listaDeLivros.indexOf(livro);
        $scope.livroSelecionado = $scope.listaDeLivros[$scope.indice];
        console.log(livro);
        window.open("#books-view", "_self")
    }

    //Função que remove o livro selecionado do sistema
    $scope.removerLivro = function() {
        var livro = $scope.listaDeLivros[$scope.indice];
        $scope.previous();
        if ($scope.indice == ($scope.listaDeLivros.length-1))
            $scope.previous();
        var url = "deletarLivro?id=" + livro.id;
        console.log(url)
        $http.delete(url).
        success(function(data) {
            console.log(data)
            $scope.carregaLivros();
        });
    }
});
})();
