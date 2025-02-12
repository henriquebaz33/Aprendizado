const nome = 'Henrique';

const concatenacao = 'Olá ' + nome + "!";
console.log(concatenacao);
const template = `Olá ${nome}!`;
console.log(template);

console.log(`1 + 1 = ${1 + 1}`);

// expressões
const up = texto => texto.toUpperCase(); // recebe texto como parametro (isso é uma function)

console.log(`Ei... ${up('Cuidado')}!`);
