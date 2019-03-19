#Unit Converter. Using meter converstion as the pivot.

# dictionay with m to other units 1 to _________

meter_dict = {'m': 1,
              'ft': 3.28,
              'yd': 1.0936,
              'mi': 0.00062137,
              'cm': 100,
              'km': .001,
               'mm': 1000}


input_number = input('What is the distance? Please enter a number:\n')
while True:
    try:
        input_number = float(input_number)
        break
    except ValueError:
        input_number = input('Please enter a number only.')

input_unit = input('What unit of measurement is this? ' + ', '.join(meter_dict.keys()) + ':\n')
while input_unit not in meter_dict.keys():
    input_unit = input(', '.join(meter_dict.keys()) + '\n')

meter_equivalent = input_number / meter_dict[input_unit]
meter_equivalent = round(meter_equivalent, 4)
# print(meter_equivalent)

output_unit = input('What unit of measurement do you want to convert this to? m, ft, yd, mi, cm, km, or mm:\n')
while output_unit not in meter_dict.keys():
    output_unit = input('m, ft, yd, mi, cm, km, or mm:\n')

out_number = round(meter_equivalent * meter_dict[output_unit], 2)

print(out_number)

exit()