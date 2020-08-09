// запрос значений от пользователя
const tempCelcius = parseInt(prompt('Enter temperature in celcius: '))

// перевод значения по формуле
const tempFahrengeit = parseInt((9 / 5) * tempCelcius + 32)

// вывод результата
alert(`Temperature:\nCelcius: ${tempCelcius}\nFahrengeit: ${tempFahrengeit}`)