from wx import *

a = App()
f = Frame(None, title="MyCalculator", size=(400,600))
p = Panel(f)
p.SetBackgroundColour("#a29bfe")
main = BoxSizer(VERTICAL)

display = TextCtrl(p)
display.SetBackgroundColour("#2d3436")
display.SetForegroundColour("white")

display_num = "0"
back_num = ""

display.SetValue(display_num)
display.SetFont(Font(55, FONTFAMILY_SWISS, FONTSTYLE_NORMAL, FONTWEIGHT_BOLD))
main.Add(display, 1, EXPAND|ALL, border=10)

def zero_fun(event):
    global display_num
    global back_num
    if display_num == "0":
        display_num = "0"
    else:
        display_num += "0"
    back_num += '0'
    display.SetValue(display_num)

def one_fun(event):
    global display_num
    global back_num
    if display_num == "0":
        display_num = "1"
    else:
        display_num += "1"
    back_num += "1"
    display.SetValue(display_num)

def two_fun(event):
    global display_num
    global back_num
    if display_num == "0":
        display_num = "2"
    else:
        display_num += "2"
    back_num += "2"
    display.SetValue(display_num)

def three_fun(event):
    global display_num
    global back_num
    if display_num == "0":
        display_num = "3"
    else:
        display_num += "3"
    back_num += "3"
    display.SetValue(display_num)

def four_fun(event):
    global display_num
    global back_num
    if display_num == "0":
        display_num = "4"
    else:
        display_num += "4"
    back_num += "4"
    display.SetValue(display_num)

def five_fun(event):
    global display_num
    global back_num
    if display_num == "0":
        display_num = "5"
    else:
        display_num += "5"
    back_num += "5"
    display.SetValue(display_num)

def six_fun(event):
    global display_num
    global back_num
    if display_num == "0":
        display_num = "6"
    else:
        display_num += "6"
    back_num += "6"
    display.SetValue(display_num)

def seven_fun(event):
    global display_num
    global back_num
    back_num += "7"
    if display_num == "0":
        display_num = "7"
    else:
        display_num += "7"
    display.SetValue(display_num)

def eight_fun(event):
    global display_num
    global back_num
    back_num += "8"
    if display_num == "0":
        display_num = "8"
    else:
        display_num += "8"
    display.SetValue(display_num)

def nine_fun(event):
    global display_num
    global back_num
    back_num += "9"
    if display_num == "0":
        display_num = "9"
    else:
        display_num += "9"
    display.SetValue(display_num)

def cancle_fun(event):
    global display_num
    display_num = "0"
    global back_num
    back_num = "0"
    display.SetValue(display_num)

def backspace_fun(event):
    global display_num
    global back_num
    back_num = back_num[:-1]
    if len(display_num) > 1:
        display_num = display_num[:-1]
    else:
        display_num = "0"
    display.SetValue(display_num)

def dot_fun(event):
    global display_num
    global back_num

    if "." not in display_num:
        display_num += "."
        back_num += "."
    display.SetValue(display_num)

def plus_minus_fun(event):
    global display_num
    global back_num

    print(display_num)
    print(back_num)
    back_num = back_num[:-len(display_num)]
    if display_num[0] == "-":
        back_num += display_num[1:]
    else:
        back_num += "-" + display_num

    if display_num[0] == "-":
        display_num = display_num[1:]
    else:
        display_num = "-"+display_num
    display.SetValue(display_num)

def add_fun(event):
    global back_num
    global display_num
    back_num += "+"
    display_num = "0"

def sub_fun(event):
    global back_num
    global display_num
    back_num += "-"
    display_num = "0"

def mul_fun(event):
    global back_num
    global display_num
    back_num += "*"
    display_num = "0"

def div_fun(event):
    global back_num
    global display_num
    back_num += "/"
    display_num = "0"

def per_fun(event):
    global back_num
    global display_num
    back_num += "/100*"
    display_num = "0"

def equal_fun(event):
    global display_num
    global back_num
    print(display_num)
    print(back_num)
    back_num = display_num = str(eval(back_num))
    display.SetValue(display_num)

btngroup = GridSizer(5,4,5,5)

zero = Button(p, label="0")
one = Button(p, label="1")
two = Button(p, label="2")
three = Button(p, label="3")
four = Button(p, label="4")
five = Button(p, label="5")
six = Button(p, label="6")
seven = Button(p, label="7")
eight = Button(p, label="8")
nine = Button(p, label="9")
cancle = Button(p, label="C")
plus_minus = Button(p, label="+/-")
dot = Button(p, label=".")
equal = Button(p, label="=")
plus = Button(p, label="+")
minus = Button(p, label="-")
multiply = Button(p, label="X")
divide = Button(p, label="÷")
percent = Button(p, label="%")
backspace = Button(p, label="⌫")

zero.Bind(EVT_BUTTON, zero_fun, zero)
one.Bind(EVT_BUTTON, one_fun, one)
two.Bind(EVT_BUTTON, two_fun, two)
three.Bind(EVT_BUTTON, three_fun, three)
four.Bind(EVT_BUTTON, four_fun, four)
five.Bind(EVT_BUTTON, five_fun, five)
six.Bind(EVT_BUTTON, six_fun, six)
seven.Bind(EVT_BUTTON, seven_fun, seven)
eight.Bind(EVT_BUTTON, eight_fun, eight)
nine.Bind(EVT_BUTTON, nine_fun, nine)
cancle.Bind(EVT_BUTTON, cancle_fun, cancle)
backspace.Bind(EVT_BUTTON, backspace_fun, backspace)
dot.Bind(EVT_BUTTON, dot_fun, dot)
plus_minus.Bind(EVT_BUTTON, plus_minus_fun, plus_minus)
equal.Bind(EVT_BUTTON, equal_fun, equal)
plus.Bind(EVT_BUTTON, add_fun, plus)
minus.Bind(EVT_BUTTON, sub_fun, minus)
multiply.Bind(EVT_BUTTON, mul_fun, multiply)
divide.Bind(EVT_BUTTON, div_fun, divide)
percent.Bind(EVT_BUTTON, per_fun, percent)

btnFont = Font(26, FONTFAMILY_MODERN, FONTSTYLE_NORMAL, FONTWEIGHT_BOLD)

zero.SetFont(btnFont)
one.SetFont(btnFont)
two.SetFont(btnFont)
three.SetFont(btnFont)
four.SetFont(btnFont)
five.SetFont(btnFont)
six.SetFont(btnFont)
seven.SetFont(btnFont)
eight.SetFont(btnFont)
nine.SetFont(btnFont)
plus_minus.SetFont(btnFont)
dot.SetFont(btnFont)
equal.SetFont(btnFont)
plus.SetFont(btnFont)
minus.SetFont(btnFont)
multiply.SetFont(btnFont)
divide.SetFont(btnFont)
percent.SetFont(btnFont)
backspace.SetFont(btnFont)
cancle.SetFont(btnFont)

zero.SetBackgroundColour("#d63031")
one.SetBackgroundColour("#d63031")
two.SetBackgroundColour("#d63031")
three.SetBackgroundColour("#d63031")
four.SetBackgroundColour("#d63031")
five.SetBackgroundColour("#d63031")
six.SetBackgroundColour("#d63031")
seven.SetBackgroundColour("#d63031")
eight.SetBackgroundColour("#d63031")
nine.SetBackgroundColour("#d63031")
cancle.SetBackgroundColour("#e17055")
backspace.SetBackgroundColour("#e17055")
percent.SetBackgroundColour("#e17055")
divide.SetBackgroundColour("#e17055")
plus.SetBackgroundColour("#e17055")
minus.SetBackgroundColour("#e17055")
multiply.SetBackgroundColour("#e17055")
divide.SetBackgroundColour("#e17055")
equal.SetBackgroundColour("#e17055")
dot.SetBackgroundColour("#e17055")
plus_minus.SetBackgroundColour("#e17055")
zero.SetForegroundColour("white")
one.SetForegroundColour("white")
two.SetForegroundColour("white")
three.SetForegroundColour("white")
four.SetForegroundColour("white")
five.SetForegroundColour("white")
six.SetForegroundColour("white")
seven.SetForegroundColour("white")
eight.SetForegroundColour("white")
nine.SetForegroundColour("white")
plus_minus.SetForegroundColour("white")
dot.SetForegroundColour("white")
equal.SetForegroundColour("white")
plus.SetForegroundColour("white")
minus.SetForegroundColour("white")
multiply.SetForegroundColour("white")
divide.SetForegroundColour("white")
percent.SetForegroundColour("white")
backspace.SetForegroundColour("white")
cancle.SetForegroundColour("white")

btngroup.AddMany([
    (cancle, 1, EXPAND|ALL),
    (backspace, 1, EXPAND|ALL),
    (percent, 1, EXPAND|ALL),
    (divide, 1, EXPAND|ALL),
    (seven, 1, EXPAND|ALL),
    (eight, 1, EXPAND|ALL),
    (nine, 1, EXPAND|ALL),
    (multiply, 1, EXPAND|ALL),
    (four, 1, EXPAND|ALL),
    (five, 1, EXPAND|ALL),
    (six, 1, EXPAND|ALL),
    (minus, 1, EXPAND|ALL),
    (one, 1, EXPAND|ALL),
    (two, 1, EXPAND|ALL),
    (three, 1, EXPAND|ALL),
    (plus, 1, EXPAND|ALL),
    (plus_minus, 1, EXPAND|ALL),
    (zero, 1, EXPAND|ALL),
    (dot, 1, EXPAND|ALL),
    (equal, 1, EXPAND|ALL),
])

main.Add(btngroup, 4, EXPAND|ALL, border=10)

p.SetSizer(main)
f.Show()
a.MainLoop()