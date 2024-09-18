The original image ('question2_task1_img.jpg') is opened, and its dimensions are obtained.
A new image with the same dimensions is created.
Each pixel of the original image has the generated number added to its RGB channels in the new image.
The new image is saved as 'outputimage_ques2.png'.
The sum of red pixel values in the new image is calculated.
red_pixel_sum = sum(new_image.getpixel((x, y))[0] for x in range(width) for y in range(height))
The final sum is then printed:
print("Sum of red pixel values:", red_pixel_sum).
![416121808_743866484019812_9027364188248165892_n](https://github.com/Sonish1212/Software-now-assignment-2/assets/153173641/01b9ba23-6c7d-4093-8698-0ee71d3fc6e5)
![question2_task1_img](https://github.com/Sonish1212/Software-now-assignment-2/assets/153173641/a083b499-e2c3-48d2-bd0d-150b6608a867)
