"use strict"

// инициализируем список товаров
const products = [
    {
        id: 3,
        price: 200,
    },
    {
        id: 4,
        price: 900,
    },
    {
        id: 1,
        price: 1000,
    },
];

// инициализируем переменную
const discount = 0.15

// проводим скидку
products.forEach(product => product.price -= product.price * discount);