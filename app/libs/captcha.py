import random
import os
import oss2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from tornado.web import RequestHandler
from config.config import ali_url

class CaptchaPIL(RequestHandler):

    def get(self):
        code, path = generate_captcha(ali_url)
        self.clear_cookie("captcha")
        self.set_cookie('captcha', code)
        return 'https://apl-verification-code.oss-cn-shanghai.aliyuncs.com/' + path, 200


def generate_captcha(url=None):
    def rnd_char():
        return chr(random.randint(65, 90))

    # 随机颜色1:
    def rnd_color():
        return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

    # 随机颜色2:
    def rnd_color2():
        return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('Arial.ttf', 45)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rnd_color())

    code = ''

    # 输出文字:
    for t in range(4):
        tmp = rnd_char()
        code += tmp
        draw.text((60 * t + 10, 8), tmp, font=font, fill=rnd_color2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    file_name = str(uuid.uuid4()) + '.png'
    local_path = os.path.join(tempfile.gettempdir(), file_name)

    image.save(local_path, 'png')

    access_key_id = 'LTAIsLk2fj3SuV7y'
    access_key_secret = 'OyAxjkuAFoQqsJ3wTPB0JeRTZiAFkK'
    bucket_name = 'apl-verification-code'
    endpoint = url.get("url")

    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
    bucket.put_object_from_file(file_name, local_path)
    os.remove(local_path)

    return code, file_name

