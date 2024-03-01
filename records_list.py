from PIL import Image, ImageDraw, ImageFont


def create_list(achievements):
    image = Image.open("data/records.png")
    font = ImageFont.truetype("arial.ttf", 25)
    drawer = ImageDraw.Draw(image)
    y = 1
    for key in achievements:
        ticks, num = achievements[key]
        millis = ticks % 1000
        seconds = int(ticks / 1000 % 60)
        minutes = int(ticks / 60000 % 24)
        time = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        drawer.text((50, y * 100), f"{key}:   {num};    {time}", font=font, fill='yellow')
        y += 1
    if not achievements:
        drawer.text((50, 100), "Установите свой первый рекорд!", font=font, fill='yellow')
    image.save('data/new_rec.png')
