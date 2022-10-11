import datetime

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
    converted_hex = int(joined_hex[::-1], 16)
else:
    converted_hex = int(joined_hex, 16)

times = datetime.timedelta(seconds=(int(converted_hex) * multiplier))

print(times)