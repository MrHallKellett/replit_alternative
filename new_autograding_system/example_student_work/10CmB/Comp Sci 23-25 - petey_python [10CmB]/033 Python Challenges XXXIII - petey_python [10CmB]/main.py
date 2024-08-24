from random import randint

def get_min_colour_depth(colour_num):
    min_colour_depth = len(str(bin(colour_num - 1))) - 2
    print(min_colour_depth)
    return min_colour_depth

#assert get_min_colour_depth(17) == 5

def calculate_bitmap_filesize(width, height, colour_num, mode):
    colour_depth = get_min_colour_depth(colour_num)
    minimum_file_size = width * height * colour_depth
    if mode == True:
        final_file_size = minimum_file_size
    else:
        final_file_size = minimum_file_size // 8
    return final_file_size

def calculate_audio_filesize(length, sample_rate, sampling_resolution, is_stereo):
    minimum_file_size = (length * sample_rate * sampling_resolution)/8000
    if is_stereo == True:
        final_file_size = minimum_file_size * 2
    else:
        final_file_size = minimum_file_size
    return final_file_size

def rle_compress(character_string):
    letter_count = 0
    final_string = ""
    this_character_string = character_string + " "
    for letter in this_character_string:
        current_letter = letter
        if current_letter == previous_letter:
            letter_count += 1
        else:
            letter_count = 0
        previous_letter = current_letter
        final_string = final_string + letter_count + letter
    return final_string
    
def random_bitmap(width, height, colour_depth):
    for i in range(0,height):
        new_list = []
        for j in range (0, width):
            new_list.append(bin(randint(0, 2**colour_depth))[:: 2].zfill(colour_depth), end= ", ")
            #print(bin(randint(0, 2**colour_depth))[:: 2].zfill(colour_depth), end= ", ")
        print("\n")
random_bitmap(10, 12, 3)
    