def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp <= 0:
        s = "Freezing"
    elif temp < 11:
        s = "Very Cold"
    elif temp < 21:
        s = "Cold"
    elif temp < 31:
        s = "Normal"
    elif temp < 41:
        s = "Hot"
    else:
        s = "Very Hot"
    return s
    return