

"""
https://adventofcode.com/2023/day/5
"""


def load_input(file):
    with open(file, 'r') as file:
        # Read all lines and store them in a list
        content  = file.read()
    sections = content.split('\n\n')
    return sections

def build_source_dest_map(section):
    source_dest_list = []
    line_section = section.split('\n')
    lines_number = line_section[1:]
    for line in lines_number:
        line_number = line.split(" ")
        number = [int(x) for x in line_number]
        dest = number[0]
        source = number[1]
        length = number[2]
        source_dest_list.append([source, source + length, dest])
    return source_dest_list

def get_mapping(source_dest_list, key):
    found = False
    result = 0
    for line in source_dest_list:
        if line[0]  <= key <= line[1]:
            result = key - line[0] + line[2]
            found = True
    if found:
        return result
    else:
        return key
        


def main():
    sections = load_input("input.txt")
    section_seeds = sections[0]
    seeds = section_seeds.split(":")[1].strip()
    seeds_number = seeds.split(" ")
    seeds_number = [int(x) for x in seeds_number]
    section_seed_to_soil = sections[1]
    section_soil_to_fertilizer = sections[2]
    section_fertilizer_to_water = sections[3]
    section_water_to_light = sections[4]
    section_light_to_temperature = sections[5]
    section_temperature_to_humidity = sections[6]
    section_humidity_to_location = sections[7]
    dict_seed_to_soil = build_source_dest_map(section_seed_to_soil)
    dict_soil_to_fertilizer = build_source_dest_map(section_soil_to_fertilizer)
    dict_fertilizer_to_water = build_source_dest_map(section_fertilizer_to_water)
    dict_water_to_light = build_source_dest_map(section_water_to_light)
    dict_light_to_temperature = build_source_dest_map(section_light_to_temperature)
    dict_temperature_to_humidity = build_source_dest_map(section_temperature_to_humidity)
    dict_humidity_to_location = build_source_dest_map(section_humidity_to_location)
    locations = []
    for seed in seeds_number:
        key_soil =  get_mapping(dict_seed_to_soil, seed)
        key_fertilizer = get_mapping(dict_soil_to_fertilizer, key_soil)
        key_water = get_mapping(dict_fertilizer_to_water, key_fertilizer)
        key_light = get_mapping(dict_water_to_light, key_water)
        key_temperature = get_mapping(dict_light_to_temperature, key_light)
        key_humidity = get_mapping(dict_temperature_to_humidity, key_temperature)
        key_location = get_mapping(dict_humidity_to_location, key_humidity)
        locations.append(key_location)
    lowest_number = min(locations)
    print(f'lowest number is {lowest_number}')
    
if __name__ == "__main__":
    main()



