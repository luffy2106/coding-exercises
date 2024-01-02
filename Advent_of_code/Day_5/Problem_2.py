"""
--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?


--- Analyze the problem ---
1. Seed to soil
a1 b1 c1
a2 b2 c2
             input       range_a       range_b      range_a_sample    range_b_sample    out_seed not in range_a     out_seed in range_a        out
soil_1       seed 79      [a1,a1+c1]    [b1,b1+c1]       [50,52]          [98,100]                seed               seed + a2 - b2              79      
soil_2       seed 79      [a2,a2+c2]    [b2,b2+c2]       [52,100]         [50,98]                 seed               seed + a2 - b2         79 +  52 - 50


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


def append_list_to_set_list(list_range_mapping, range_mapping_case):
    if range_mapping_case not in list_range_mapping:
        list_range_mapping.append(range_mapping_case)
    



def get_range_mapping(list_input_range, list_dict_source_to_dest):
    """There will be 5 cases

    dict_source_to_dest : [source, source + length, dest]
    input_range :  [x, x_range] => [x_min, x_max]
    Args:
        input_range (_type_): _description_
        dict_source_to_dest (_type_): _description_
    
    """
    total_list_range_mapping_input = []
    for input_range in list_input_range:
        # list_range_mapping_input  = [input_range]
        list_range_mapping_input = []
        for dict_source_to_dest in list_dict_source_to_dest:
            # case 1 : x_max < source
            if input_range[1] < dict_source_to_dest[0]:
                range_mapping_case_1 = [input_range[0], input_range[1]]
                # list_range_mapping_input = []
                if input_range in list_range_mapping_input:
                    list_range_mapping_input.remove(input_range)
                append_list_to_set_list(list_range_mapping_input, range_mapping_case_1) 
            # case 2 : x  < source <= x_max <= source + length
            if input_range[0]  < dict_source_to_dest[0] <= input_range[1] <= dict_source_to_dest[1]:
                range_mapping_case_2_1 = [input_range[0], dict_source_to_dest[0]-1]      #[x, source - 1]
                range_mapping_case_2_2 = [dict_source_to_dest[2], input_range[1] + dict_source_to_dest[2] - dict_source_to_dest[0]]    #[source + dest - source, x + x_range + dest - source]
                # list_range_mapping_input = []
                if input_range in list_range_mapping_input:
                    list_range_mapping_input.remove(input_range)
                append_list_to_set_list(list_range_mapping_input, range_mapping_case_2_1) 
                append_list_to_set_list(list_range_mapping_input, range_mapping_case_2_2) 
            # case 3 : x > source and x + x_range < source + length
            if input_range[0] > dict_source_to_dest[0] and input_range[1] < dict_source_to_dest[1]:
                range_mapping_case_3 = [input_range[0] + dict_source_to_dest[2] - dict_source_to_dest[0], input_range[1] + dict_source_to_dest[2] - dict_source_to_dest[0]]    # [x + dest-source, x + x_range + dest - source]
                # list_range_mapping_input = []
                if input_range in list_range_mapping_input:
                    list_range_mapping_input.remove(input_range)
                append_list_to_set_list(list_range_mapping_input, range_mapping_case_3)
            # case 4 : source < x < source + length < x + x_range
            if dict_source_to_dest[0] < input_range[0] < dict_source_to_dest[1] < input_range[1]:
                range_mapping_case_4_1 = [input_range[0] + dict_source_to_dest[2]-dict_source_to_dest[0], dict_source_to_dest[1]+dict_source_to_dest[2] - dict_source_to_dest[0] ]  # [x+dest-source, source+length+dest-source]
                range_mapping_case_4_2 = [dict_source_to_dest[1]+1, input_range[1]]       # [source + length + 1, x_max]
                # list_range_mapping_input = []
                if input_range in list_range_mapping_input:
                    list_range_mapping_input.remove(input_range)
                append_list_to_set_list(list_range_mapping_input, range_mapping_case_4_1)
                append_list_to_set_list(list_range_mapping_input, range_mapping_case_4_2)
            # case 5 : source + length < x
            if dict_source_to_dest[1] < input_range[0]:
                range_mapping_case_5 = [input_range[0], input_range[1]]
                # list_range_mapping_input = []
                if input_range in list_range_mapping_input:
                    list_range_mapping_input.remove(input_range)
                append_list_to_set_list(list_range_mapping_input, range_mapping_case_5)
        total_list_range_mapping_input.extend(list_range_mapping_input)
    optimize_list = optimize_range_list(total_list_range_mapping_input)
    return optimize_list


def optimize_range_list(range_list):
    """
    Need to convert [[79, 92], [81, 94]] to [[79, 94]]
    """
    sorted_ranges = sorted(range_list, key=lambda x: x[0])

    # Initialize the optimized list with the first range
    optimized_list = [sorted_ranges[0]]

    # Iterate over each range in the sorted list
    for current_range in sorted_ranges[1:]:
        # Get the last range from the optimized list
        last_range = optimized_list[-1]

        # Check if the current range overlaps or can be merged with the last range
        if current_range[0] <= last_range[1]:
            # Update the ending value of the last range
            last_range[1] = max(last_range[1], current_range[1])
        else:
            # Add the current range to the optimized list
            optimized_list.append(current_range)

    return optimized_list

def main():
    sections = load_input("input2.txt")
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
    list_seed_range = [[seeds_number[i], seeds_number[i+1] - 1] for i in range(0, len(seeds_number)-1, 2)]
    list_min_location = []
    for seed_range in list_seed_range:
        seed_range = [seed_range[0], seed_range[0] + seed_range[1]]
        seed_range_list = [seed_range]    #[79,92] 82
        soil_range_list = get_range_mapping(seed_range_list, dict_seed_to_soil)   #[81,94] 84
        fertilizer_range_list = get_range_mapping(soil_range_list, dict_soil_to_fertilizer) #[81,94] 84
        water_range_list = get_range_mapping(fertilizer_range_list, dict_fertilizer_to_water) #[81,94] 84
        light_range_list = get_range_mapping(water_range_list, dict_water_to_light) #[74,87] 77
        temperature_range_list = get_range_mapping(light_range_list, dict_light_to_temperature) #[[78,81],[78,87]] 45
        humidity_range_list = get_range_mapping(temperature_range_list, dict_temperature_to_humidity)
        location_range_list = get_range_mapping(humidity_range_list, dict_humidity_to_location)
        min_location = min([x[0] for x in location_range_list])
        list_min_location.append(min_location)
    result = min(list_min_location)
    print(result)
        
if __name__ == "__main__":
    main()