let isAtivo = false;
console.log(isAtivo);

isAtivo = true;
console.log(true);

isAtivo = 1;
console.log(!!isAtivo); // negação duas vezes mostra o valor original

console.log('os verdadeiros...');

console.log(!!3);
console.log(!!-1);
console.log(!!' ');
console.log(!!'teste');
console.log(!![]);
console.log(!!{});
console.log(!!Infinity);
console.log(!!(isAtivo = 33));

console.log('os falsos...');
console.log(!!0);
console.log(!!""); //da pra usar se o nome estiver preenchido ou não, só passar a string
console.log(!!null);
console.log(!!NaN);
console.log(!!undefined);
console.log(!!(isAtivo = 0));

console.log("Pra finalizar...");
console.log(('' || null || 0 || "heureca")); // retorna o  primeiro valor verdadeiro encontrado

let nome = '';
// let nome = 'Lucas'
console.log(nome || 'Desconhecido');
