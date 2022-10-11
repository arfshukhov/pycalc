def symbol_add(symbol: str, place):
    text = place.text() + symbol
    place.setText(text)


def execution(place):
    expression = str(place.text())
    expression=expression.replace("√", "sqrt")
    expression=expression.replace("sqr", "pow")
    print(expression)
    exec(f"from math import *; result = {expression}; place.setText(str(result))")


def break_expression(place):
    place.setText("")





