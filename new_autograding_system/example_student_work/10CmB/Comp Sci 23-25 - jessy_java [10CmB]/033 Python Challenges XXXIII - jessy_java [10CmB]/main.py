import random

def get_min_colour_depth(num_colors):
    num_colors -= 1
    binary = bin(num_colors)[2:]  # remove '0b' prefix
    length = len(binary)
    return length

def calculate_bitmap_filesize(width, height, num_colors, mode=True):
    bits_per_pixel = get_min_colour_depth(num_colors)
    total_pixels = width * height
    filesize_bits = total_pixels * bits_per_pixel

    if mode:
        return filesize_bits
    else:
        filesize_bytes = filesize_bits / 8
        return filesize_bytes

def calculate_audio_filesize(length, sample_rate, sampling_resolution, is_stereo):
    bits_per_sample = sample_rate * sampling_resolution
    if is_stereo:
        bits_per_sample *= 2
    bytes_per_second = bits_per_sample / 8
    filesize_kilobytes = (bytes_per_second * length) / 1000 


    return filesize_kilobytes


def rle_compress(string):
    compressed = " "
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressed += str(count) + string[i-1]
            count = 1
    compressed += str(count) + string[-1]
    return compressed

def random_bitmap(width, height, colour_depth):
    
    bitmap = [random.randint(0, 1) 

        for i in range(width)
            
        for i in range(height)]
    print(bitmap)
   
    return bitmap 


        


    

if __name__ == "__main__":
    assert calculate_bitmap_filesize(100, 100, 1, True) == 10000
    assert calculate_audio_filesize(30, 44100, 32, True) == 10584
    assert rle_compress("aaaaabbbbbbcddddeeeefffgg") == "5a6b1c4d4e3f2g"
