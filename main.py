import PIL.Image


dec = input("1 for contrast and 2 for a gradiant: ")
if dec == "1":
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
elif dec == "2":
    ASCII_CHARS = ["Ñ","@","#","W","$","9","8","7","6","5","4","3","2","1","0","?","!","a","b","c",";",";","+",",",".","_"]    
else:
    print("Invalid input... random value will be used")
    ASCII_CHARS = ["Ñ","@","#","W","$","9","8","7","6","5","4","3","2","1","0","?","!","a","b","c",";",";","+",",",".","_"]


def resize(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=100):
    path = input("Enter the path to the image: ")

    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid path to an image.")

    new_image_data = pixels_to_ascii(grayify(resize(image)))    
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

    print(ascii_image)
    

main()