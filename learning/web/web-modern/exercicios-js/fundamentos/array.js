const valores = [7.7, 6.3, 3.3, 8.9];
console.log(valores[0], valores[2]);
console.log(valores[4]);

valores[4] = 10;
console.log(valores);
console.log(valores.length);

valores.push({id: 3}, false, null, 'teste');
console.log(valores);
console.log(valores.length);

console.log(valores.pop());
console.log(valores);
console.log(valores.length);

delete valores[valores.length - 1];
console.log(valores);
console.log(valores.length);

console.log(typeof valores);
