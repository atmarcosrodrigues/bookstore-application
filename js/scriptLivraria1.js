/* 
 * Script Angular JS - Livraria JS
*/

(function () {
    var app = angular.module('livrariaJS', []);
    //altera o separador de formatacao AngularJS para evitar confiltos com webapp
    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });

    app.controller('livrariaJSController', function($scope) {

    //carrega a lista de livros 
    $scope.listaDeLivros = db;

    //variaveis de controle do modulo
    $scope.showAddArea = false;
    $scope.exibeEdicao = false;
    $scope.indice = 0;
    $scope.livroSelecionado = $scope.listaDeLivros[$scope.indice];

    //função que adiciona um novo livro na lista
    $scope.addLivro = function(livro) {
        livro.comentarios = [];
        if (livro.urlCapa == undefined || livro.urlCapa == "")
            livro.urlCapa = "images/capa_livro.png";

        $scope.listaDeLivros.push(angular.copy(livro));
        window.alert("Livro cadastrado com sucesso!");
        $scope.indice = $scope.listaDeLivros.length - 1;
        $scope.livroSelecionado = $scope.listaDeLivros[$scope.indice];
        $scope.limpaCampos(livro);
        $scope.desativaAddArea();

    };

    //funcoes para avançar/voltar livros da lista
    $scope.previous = function() {
        $scope.incrementa(-1);
        $scope.updatecomentarios();
    };

    $scope.next = function() {
        $scope.incrementa(1);
        $scope.updatecomentarios();
    };

    //funcao que incrementa o livro corrente no painel de listagem
    $scope.incrementa = function(incremento) {
        var len = $scope.listaDeLivros.length;
        $scope.indice = ((($scope.indice + incremento) + len) % len)
        $scope.livroSelecionado = $scope.listaDeLivros[$scope.indice];
    };

    //funcoes de controle dos paineis da interface
    $scope.ativaAddArea = function() {
        $scope.showAddArea = true;

    };
    $scope.desativaAddArea = function() {
        $scope.showAddArea = false;
        $scope.updatecomentarios();
    };

    $scope.updatecomentarios = function() {
        var livro = $scope.listaDeLivros[$scope.indice]
        if ($scope.listaDeLivros[$scope.indice].comentarios == undefined) {
            livro.comentarios = get_comentarios(livro.id);
        }
    };

    $scope.livro_nao_editado = {};
    $scope.ativaEdicao = function() {
        $scope.livro_nao_editado = angular.copy($scope.listaDeLivros[$scope.indice])
        $scope.exibeEdicao = $scope.exibeEdicao ? false : true;

    };

    $scope.limpaCampos = function(lista) {
        for (var chave in lista) {
            lista[chave] = null;
        }
    };

    $scope.sobre = function() {
        window.alert("P3-ufcg - Livraia JS \n Simples aplicação para manipulação do frontend com Angular JS");
    };

    //funcao que adiciona um novo comentario no livro corrente
    $scope.postarComentario = function(comentario) {
        comentario.data = new Date();
        $scope.listaDeLivros[$scope.indice].comentarios.push(angular.copy(comentario));
        var idlivro = $scope.listaDeLivros[$scope.indice].id;
        $scope.limpaCampos(comentario);
    };

    $scope.salvaEdicao = function() {
        var livro = $scope.listaDeLivros[$scope.indice];
        window.alert("Alterações feitas com sucesso!");
        $scope.ativaEdicao();
    };

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

    $scope.updatecomentarios();
});
})();
