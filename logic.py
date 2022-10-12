def symbol_add(symbol: str, place):
    pos = place.cursorPosition()
    text = list(place.text())
    text.insert(pos, symbol)
    place.setText("".join(text))
    place.setCursorPosition(pos+1)


def execution(place):
    expression = str(place.text())
    expression=expression.replace("√", "sqrt")
    expression=expression.replace("sqr", "pow")
    try:
        exec(f"from math import *; result = {expression}; place.setText(str(result))")
    except ZeroDivisionError:
        place.setText("You can not divide by zero!")
    except SyntaxError:
        place.setText("Invalid sintax. Check your expression...")

def break_expression(place):
    place.setText("")





