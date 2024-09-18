from PIL import Image
import time


def generate_random_number():
    """Generates a random number based on the current timestamp.

    This function uses the current unix timestamp to create a "random" number.
    It extracts the last two digits of the timestamp, adds 50, and ensures it's odd
    by adding 10 if it's even. This provides a basic level of randomness but isn't
    cryptographically secure.

    Returns:
        int: The generated random number between 60 and 149.
    """
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50
    if generated_number % 2 == 0:
        generated_number += 10
    return generated_number


def process_image(image_path, output_path):
    """Processes an image by adding a random value to each pixel channel.

    This function opens an image, generates a random number, creates a new image
    with the same dimensions, iterates through each pixel, adds the generated number
    to each color channel (red, green, blue), and ensures the values don't exceed 255.
    Finally, it saves the new image and prints the sum of the red channel values.

    Args:
        image_path: The path to the image file to process.
        output_path: The path to save the processed image.
    """
    # Open the image
    img = Image.open(image_path)

    # Generate the random number using the function
    n = generate_random_number()
    print(f"Generated random number: {n}")

    # Create a new image with the same size as the original
    new_img = Image.new("RGB", img.size)

    # Process each pixel
    sum_of_red = 0
    for x in range(img.width):
        for y in range(img.height):
            # Get the original pixel values
            r, g, b = img.getpixel((x, y))

            # Add n to each channel, ensuring we don't exceed 255
            new_r = min(r + n, 255)
            new_g = min(g + n, 255)
            new_b = min(b + n, 255)

            # Set the new pixel in the new image
            new_img.putpixel((x, y), (new_r, new_g, new_b))

            # Add the new red value to our sum
            sum_of_red += new_r

    # Save the new image
    new_img.save(output_path)

    # Print the sum of red pixel values
    print(f"The sum of red pixel values in the new image is: {sum_of_red}")


# Define paths for input and output images (modify as needed)
image_path = "./chapter1.jpg"
output_path = "chapter1out.png"

# Process the image
process_image(image_path, output_path)
