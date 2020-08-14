console.log(10 + 10 + "10")
// результат = 2010.
// оператор сложения выролняется слева направо:
// 1. сложение целых чисел 10+10
// 2. сложение int + string 20 приводится к "20"
// 3. результат "2010"

console.log(10 + "10" + 10)
// результат = 101010.
// оператор сложения выролняется слева направо:
// 1. сложение int + string 10 + "10" результат "1010"
// 2. сложение string + int "1010" + 10
// 3. результат "2010"

console.log(10 + 10 + + "10")
// результат = 30.
// оператор сложения выролняется слева направо:
// 1. сложение int + int 10 + 10 результат 20
// 2. + "10" неявно приводится к значению int 10
// 3. сложение int + int 20 + 10 результат 30

console.log(10 / - "")
// результат = -infinity.
// оператор деления выролняется слева направо:
// 1. выражение - "" неявно приводится к значению int -0
// 2. выполняется деление int / int 10 / -0
// 3. результат = -infinity.

console.log(10 / + "2.5")
// результат = 4.
// оператор деления выролняется слева направо:
// 1. выражение + "2.5" неявно приводится к значению int 2.5
// 2. выполняется деление int / int 10 / 2.5
// 3. результат = 4
