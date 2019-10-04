// Inicializar o módulo.
let nomeApp = 'EscolaWebApp'
let modulos = [];
var app = angular.module(nomeApp, modulos );

// Estrutura básica para uma função no controlador.
var MeuPrimeiroController = function ($scope){
  $scope.logradouro = "Outro valor";
}

app.controller('MeuPrimeiroController', meuPrimeiroController);

var MeuSegundoController = function ($scope){
  $scope.logradouro = "Outro valor";
}

app.controller('MeuSegundoController', meuSegundoController);

