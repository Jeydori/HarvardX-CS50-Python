import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 1:
        sys.exit("Too mfew command-line arguments")
    else:
        if (sys.argv[1][-4:]num in [".png",".jpg","jpeg"]) and (sys.argv[2][-4:] in [".png",".jpg","jpeg"]):
            if sys.argv[1][-4:] == sys.argv[2][-4:]:
                overlay(sys.argv[1], sys.argv[2])
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input")

def overlay(image_input, image_output):
    try:
        with Image.open(image_input) as img_input, Image.open("shirt.png") as shirt:
            shirt_size = shirt.size
            img_input = ImageOps.fit(img_input, shirt_size)
            img_input.paste(shirt, (0, 0), shirt)
            img_input.save(image_output)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
