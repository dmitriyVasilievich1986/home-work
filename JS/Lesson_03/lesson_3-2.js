"use strict"

// инициализируем объект
const post = {
    author: "John", //вывести этот текст
    postId: 23,
    comments: [
        {
            userId: 10,
            userName: "Alex",
            text: "lorem ipsum",
            rating: {
                likes: 10,
                dislikes: 2 //вывести это число
            }
        },
        {
            userId: 5, //вывести это число
            userName: "Jane",
            text: "lorem ipsum 2", //вывести этот текст
            rating: {
                likes: 3,
                dislikes: 1
            }
        },
    ]
};

// получаем данные из объекта
const author = post.author;
const dislikes = post.comments[0].rating.dislikes;
const userId = post.comments[1].userId;
const text = post.comments[1].text;

// выводим полученные данные
console.log(author);
console.log(dislikes);
console.log(userId);
console.log(text);