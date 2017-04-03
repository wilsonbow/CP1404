
COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "black":"#000000", "blue1": "#0000ff",
                "BlueViolet": "8a2be2", "brown": "#a52a2a", "chocolate": "d2691e",
                "coral": "#ff7f50", "DimGray": "#696969", "firebrick": "#b22222"}

colour = input("Enter a colour name: ")
if colour in COLOUR_NAMES:
    print("{} is {}".format(colour, COLOUR_NAMES[colour]))
else:
    print("{} not in dictionary.".format(colour))

