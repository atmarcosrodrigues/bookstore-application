/* Pogramação 3 - Ex1
   Script Angular JS - Livraria JS
*/

var app = angular.module('livrariaJS');


app.controller('uiRouterController', function($scope, $http) {

    //variaveis de controle do modulo
    $scope.exibeEdicao = false;
    $scope.indice = 0;

    $scope.listaDeLivros = []; 
    $scope.livroSelecionado = {}; 

    console.log("Ok...");

});