import datetime

while True:
    endian = ''

    print("Please input the hex bits")
    hex_input = input(">").lower()
    print("Is the bit order little or big endian (Intel or Motorola)")
    endian = input(">").lower()
    print("Please input any multiplier")
    multiplier = float(input(">"))

    if " " in hex_input:
        new_hex = hex_input.split(" ")
        joined_hex = "".join(new_hex)
    else:
        joined_hex = hex_input

    if "little" in endian or "intel" in endian:
        try:
            converted_hex = int(joined_hex[::-1], 16)
            times = datetime.timedelta(seconds=(int(converted_hex) * multiplier))
            print(times)
        except:
            print("Invalid hex value, please retry")
    else:
        try:
            converted_hex = int(joined_hex, 16)
            times = datetime.timedelta(seconds=(int(converted_hex) * multiplier))
            print(times)
        except:
            print("Invalid hex value, please retry")

    yesno = input("Do you want to check another value? (Yes/No)\n>").casefold()
    if yesno == "yes":
        continue
    else:
        break