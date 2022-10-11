import datetime

hex_input = input(">").lower()

if " " in hex_input:
    new_hex = hex_input.split(" ")
    joined_hex = "".join(new_hex)
else:
    joined_hex = hex_input

converted_hex = int(joined_hex, 16)

times = datetime.timedelta(seconds=(int(converted_hex) * 0.01))

print(times)