const prod1 = {};
prod1.nome = 'Celular iPhone Ultra';
prod1.preco = 4567.90;
prod1['Desconto'] = 0.40; // evitar atributos com espaço

console.log(prod1);

const prod2 = {
    nome:'Henrique',
    produto:'Relógio Cassio',
    preco: 79.90,
    interassados: {
        cliente1: {
            nome: 'José',
            idade: 18,
            cidade: 'NH'
        },

        cliente2: {
            nome: 'Cleberson',
            idade: 27,
            cidade: 'São Leopoldo'
        },
        
        cliente3: {
            nome: 'Rodrigo',
            idade: 42,
            cidade: 'Estância Velha'
        }
    }
}

prod2.interassados.cliente4 = {};
prod2.interassados.cliente4.nome = 'Camaro';
prod2.interassados.cliente4.idade = 65;
prod2.interassados.cliente4.cidade = 'Los Angeles';
console.log(prod2.interassados);
