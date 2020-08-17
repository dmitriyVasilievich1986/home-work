"use strict"

// инициализируем список товаров
const products = [
    {
        id: 3,
        price: 127,
        photos: [
            "1.jpg",
            "2.jpg",
        ]
    },
    {
        id: 5,
        price: 499,
        photos: []
    },
    {
        id: 10,
        price: 26,
        photos: [
            "3.jpg"
        ]
    },
    {
        id: 8,
        price: 78,
    },
];

// фильтруем список
const productsWithPhotos = products.filter(product => product.photos != undefined && product.photos.length > 0);

// сортируем список
const sortedList = products.sort((a, b) => a.price - b.price);

// выводим поличившиеся значения
console.log(productsWithPhotos);
console.log(sortedList);