"use strict"


// сначала объявляем переменные и присваиваем им значения
// a=1, b=1, c и d = undefined
let a = 1, b = 1, c, d;
// присваиваем переменной c значение переменной a
// префиксный инкремент ++ имеет больший приоритет чем присвоение =
// вначале происходит уаелечение значения переменной a на 1,
// затем переменной c присваивается значение переменной a = 2
c = ++a;

// присваиваем переменной d значение переменной b
// постфиксный инкремент ++ имеет меньший приоритет чем присвоение =
// вначале происходит присвоение переменной значения переменной b = 1,
// затем переменной b прибавляется 1, переменная b = 2
d = b++;

