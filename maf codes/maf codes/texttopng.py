from PIL import Image, ImageDraw, ImageFont

# ======== CONFIGURE YOUR TEXT & IMAGE ========
text = input("Enter the text to convert to PNG: ")
font_size = 40  # You can change this
text_color = "black"
bg_color = "white"
padding = 20  # Space around the text

# ======== LOAD FONT ========
try:
    font = ImageFont.truetype("arial.ttf", font_size)  # Change font file if you want
except:
    font = ImageFont.load_default()
    print("Custom font not found, using default.")

# ======== CALCULATE IMAGE SIZE BASED ON TEXT ========
dummy_image = Image.new('RGB', (1,1))
draw = ImageDraw.Draw(dummy_image)
text_width, text_height = draw.textsize(text, font=font)

width = text_width + padding * 2
height = text_height + padding * 2

# ======== CREATE IMAGE AND ADD TEXT ========
image = Image.new('RGB', (width, height), color=bg_color)
draw = ImageDraw.Draw(image)
draw.text((padding, padding), text, fill=text_color, font=font)

# ======== SAVE IMAGE ========
output_file = "text_image.png"
image.save(output_file)
print(f"PNG saved as {output_file}")