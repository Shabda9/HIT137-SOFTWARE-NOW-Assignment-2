from PIL import Image
import time


# Create a function to generate and return the random number.
def generate_number():
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50
    if generated_number % 2 == 0:
        generated_number += 10
    return generated_number

# Open the image
img = Image.open("./chapter1.jpg")

# Generate the number using the provided algorithm
n = generate_number()
print(f"Generated number: {n}")

# Create a new image with the same size as the original
new_img = Image.new('RGB', img.size)

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
new_img.save("chapter1out.png")

# Print the sum of red pixel values
print(f"The sum of red pixel values in the new image is: {sum_of_red}")