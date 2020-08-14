// обяъвляем константы типов математических операций
const SUBSTRACT = "SUBSTRACT"
const MULTIPLY = "MULTIPLY"
const SUMMARY = "SUMMARY"
const DIVIDE = "DIVIDE"

// объявляем функцию
function math_function(arg1, arg2, operation) {
    /**
     * function takes 2 numbers and math operator,
     * return value based on operator
     * @param {number} arg1 first integer number
     * @param {number} arg2 second integer number
     * @param {string} operation math operator
     * @returns {number}
     */
    switch (operation) {
        case SUMMARY:
            return two_numbers_summarize(arg1, arg2)
        case SUBSTRACT:
            return two_numbers_substracts(arg1, arg2)
        case MULTIPLY:
            return two_numbers_multiply(arg1, arg2)
        case DIVIDE:
            return two_numbers_divides(arg1, arg2)
        default:
            return 0
    }
}