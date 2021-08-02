/* 
 * Script Angular JS - Livraria JS
*/

(function () {
var app = angular.module('livrariaJS');

app.controller('loginController', function($scope, $http, loginUsuario) {

    //variaveis de controle do modulo
    $scope.login = loginUsuario.getProperty(); // 
    $scope.login.email = "";
    $scope.login.senha = "";
    $scope.cadastro = {nome: "", sobrenome: "", email: "", senha: "", confsenha: ""};

    /* Variável que carrega os templates Html da UI*/
    $scope.template = {login: "templates/login.html", 
                        boasvindas: "templates/boasvindas.html", 
                        cadastrolivro: "templates/cadastrolivro.html", 
                        comentarios: "templates/comentarios.html",
                        livros: "templates/livros-disponiveis.html",
                        busca: "templates/busca.html",
                        resultadosbusca: "templates/resultados-busca.html",
                        footer: "templates/footer.html"
                    };

    /* Função que efetua login do usuário*/
    $scope.logar = function(){
         var url = "getUsuario?email=" + $scope.login.email + 
                 "&hashsenha=" + $scope.login.senha.hashCode();
         
        console.log(url)
         // HTTP GET
        $http.get(url).
        success(function(data) {
            console.log(data);
            if (data.length == 0)
                alert("Email ou senha inválidos!");
            else{
                $scope.login.status = true;
                $scope.login.nome = data[0].nome;
                $scope.login.sobrenome = data[0].sobrenome;
                loginUsuario.setProperty($scope.login)
                console.log($scope.login.nome)   
                console.log($scope.login.sobrenome)
                window.open("#inicio", "_self");             
            } 

        });
    }

    /* Função de cadastro de usuários*/
    $scope.cadastrar = function(){
        if (!validateEmail($scope.cadastro.email))
            alert("Email inválido!");
        else if ($scope.cadastro.senha != $scope.cadastro.confsenha)
            alert("As senhas não conrrespondem!");
        else if ($scope.cadastro.senha.length < 6)
            alert("A senha é muito curta!");
        else{
            var url = "postUsuario?nome=" + $scope.cadastro.nome +
                     "&sobrenome=" + $scope.cadastro.sobrenome + 
                     "&email=" + $scope.cadastro.email + 
                     "&hashsenha=" + $scope.cadastro.senha.hashCode();
             // HTTP POST
            $http.post(url).
            success(function(data) {
                console.log(data);
                alert("Cadastro realizado com sucesso!");
                 $scope.login.email = $scope.cadastro.email;
                $scope.login.senha = $scope.cadastro.senha;
                $scope.logar();
            });
        }
    }
    
    /* funçãode logout */
    $scope.sair = function(){
            $scope.login.status = false;
            $scope.login.nome = "";
            $scope.login.sobrenome = "";
            $scope.login.senha = "";
    }

    /* Função que checa a validade da formatação de um email*/
    function validateEmail(email) {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    }

    /* função que gera um hashCode para strings */
    String.prototype.hashCode = function() {
        var hash = 0, i, chr, len;
        if (this.length === 0) return hash;
        for (i = 0, len = this.length; i < len; i++) {
        chr   = this.charCodeAt(i);
        hash  = ((hash << 5) - hash) + chr;
        hash |= 0; // Convert to 32bit integer
        }
        return hash;
    };

    $scope.sobre = function(livro) {
        console.log("sobre");
        window.open("#sobre", "_self")
    }

});
})();
