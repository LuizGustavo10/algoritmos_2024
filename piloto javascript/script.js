
//váriaveis
        //tipo inteiro
let nome = "Arlindo";       //tipo String(Texto)
let peso = 69.5;            //tipo decimal
let sistemaAtivo = false;   //tipo booleano (True ou False)(Verdadeiro ou Falso)
let numero = 75;     

//impressões
console.log("o nome é: " + nome);
alert("o nome é: " + nome);

//estrutura condicional
//tipos de comparação: 
// > maior
// < menor
// >= maior igual
// <= menor igual
// === igualdade
// !== diferente
//se número for maior que 10
if (numero > 10) {
    alert("Número maior que 10! ");
}else {                                 //se não for maior que 10
    alert("Número menor que 10! ");
}

if (nome === "Arlindo") {
    console.log("O cliente Arlindo está com conta atrasada! ");
}

let contador = 0;
//estrutura de repetição
//enquanto
while(contador < 5){
    console.log("O número é " + contador);
    contador = contador + 1;
}

//trabalhando com lista
let nomes = ['Julius','Marcos','Lucas','José', 'Joao'];

console.log("nome: "+ nomes[3]);

//nomes.lenght = tamanho da lista = 5

//inicio     condição de continuação    incrementador +1
for(contador =0; contador<nomes.length; contador++){
    console.log("Imprimindo nomes: "+ nomes[contador]);
}

//objeto
var pessoa = { idade:10, nome: 'Nivaldo', altura: 1.72 };
alert(pessoa.nome);



