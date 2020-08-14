"use strict"

// объевляем переменные и присваиваем им значения
const a = 5, b = 10;

// объявляем функцию сравнения двух чисел
function two_numbers(a, b) {
    /**
     * function compares two integer numbers
     * @param {number} a first integer number
     * @param {number} b second integer number
     * @returns {number}
     */
    if (a >= 0 && b >= 0)
        return (a - b);
    else if (a < 0 && b < 0)
        return (a * b);
    else
        return (a + b);
}

// вызываем функцию и выводим результат
console.log(two_numbers(a, b));
