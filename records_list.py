from PIL import Image, ImageDraw, ImageFont


def create_list(achievements):
    image = Image.open("data/records.png")
    font = ImageFont.truetype("arial.ttf", 25)
    drawer = ImageDraw.Draw(image)
    y = 1
    for key in achievements:
        drawer.text((50, y * 100), f"{key}:   {achievements[key]}", font=font, fill='yellow')
        y += 1
    if not achievements:
        drawer.text((50, 100), "Установите свой первый рекорд!", font=font, fill='yellow')
    image.save('data/new_rec.png')
