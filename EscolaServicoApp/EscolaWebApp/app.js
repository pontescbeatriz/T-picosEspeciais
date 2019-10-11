// Inicializar o módulo.

let nomeApp = 'EscolaWebApp';
let modulos = []
var app = angular.module(nomeApp, modulos);


app.controller('MeuPrimeiroController', nomeDaFuncao);

app.controller('AlunoController', alunoController);

var alunoController = function($scope){
  $scope.nome = "";
  $scope.matricula = "";
  $scope.cpf = "";
  $scope.nascimento = "";
  $scope.id_endereco = "";
  $scope.id_curso = "";
}

app.controller('AlunoController', alunoController);

app.controller('CampusController', campusController);

var campusController = function($scope){
  $scope.sigla = ";
  $scope.cidade = ";
}

app.controller('CampusController', campusController)

app.controller('CursoController', cursoController);

var cursoController = function($scope){
  $scope.nome = "";
  $scope.id_turno = "";
}

app.controller('CursoController', cursoController);

app.controller('DisciplinaController', disciplinaController);

var cursoController = function($scope){
  $scope.nome = "";
  $scope.id_professor= "";
}

app.controller('DisciplinaController', disciplinaController);

app.controller('EnderecoController', enderecoController);

var cursoController = function($scope){
  $scope.nome = "";
  $scope.complemento= "";
  $scope.bairro = "";
  $scope.cep= "";
  $scope.numero= "";
}

app.controller('EnderecoController', enderecoController);


app.controller('ProfessorController', professorController);

var cursoController = function($scope){
  $scope.nome = "";
  $scope.id_endereco= "";
}

app.controller('ProfessorController', professorController);

app.controller('TurmaController', turmaController);

var cursoController = function($scope){
  $scope.nome = "";
}

app.controller('TurmaController', turmaController);

app.controller('TurnoController', turnoController);

var cursoController = function($scope){
  $scope.nome = "";
}

app.controller('TurnoController', turnoController);

app.controller('TurnoController', turnoController);

var cursoController = function($scope){
  $scope.nome = "";
}

app.controller('TurnoController', turnoController);
