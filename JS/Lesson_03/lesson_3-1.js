"use strict"

// инициализируем цикл
for (let cycle = 0; cycle < 11; cycle++) {
    if (cycle === 0) {
        console.log("0-это ноль");  // выводим входной 0
    } else {
        const postScript = cycle % 2 === 0 ? '-четное число' : '-нечетное число'; // вычисляем остаток
        console.log(`${cycle}${postScript}`);   // выводим получившееся выражение
    }
};