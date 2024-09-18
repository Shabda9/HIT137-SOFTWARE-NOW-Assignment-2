# import time
# current_time =int(time.time())

# generated_number = (current_time % 100) + 50

# if generated_number % 2 == 0:
#     generated_number+=10

# print(generated_number)
# here the generated_number n =60

from PIL import Image

# Open the original image
original_image = Image.open('./question2_task1_img.jpg')

# Get the dimensions of the image
width, height = original_image.size

# Define the generated number
generated_number = 60

# Create a new image with the same size and mode as the original
new_image = Image.new('RGB', (width, height))

# Iterate over each pixel and apply the transformation
for x in range(width):
    for y in range(height):
        # Get the original pixel values
        r, g, b = original_image.getpixel((x, y))
        
        # Add the generated number to each channel
        new_r = min(r + generated_number, 255)
        new_g = min(g + generated_number, 255)
        new_b = min(b + generated_number, 255)

        # Set the new pixel value in the new image
        new_image.putpixel((x, y), (new_r, new_g, new_b))

# Save the new image
new_image.save('outputimage_ques2.png')

# Calculate the sum of all red pixel values in the new image
red_pixel_sum = sum(new_image.getpixel((x, y))[0] for x in range(width) for y in range(height))

# Print the sum
print("Sum of red pixel values:", red_pixel_sum)

