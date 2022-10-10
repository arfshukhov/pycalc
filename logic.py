def symbol_add(symbol: str, place):
    text = place.text() + symbol
    text.setText(text)


def execution(expression: str, place)-> str:
    expression.replace("√", "sqrt")
    result = exec(f"from math import *;{expression}")
    place.setText(result)




