# coding: utf8
import os, textwrap
from flask import Flask
from PIL import ImageFont, ImageDraw, Image
from StringIO import StringIO
from datetime import datetime
from pytz import timezone
import tweepy

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def draw_text_centered(draw, center, text, font, spacing=0):
    text_box_size = draw.multiline_textsize(text, font=font, spacing=spacing)
    topleft = (
        center[0] - text_box_size[0]/2,
        center[1] - text_box_size[1]/2
    )
    draw.multiline_text(topleft, text, font=font, align='center', spacing=spacing)

consumer_key = "uoNshE7yi6VMjtkQEGmrmbDtL"
consumer_secret = "JGnfE8M6wQTEuwGzqR80CnLP1h90IQEXSMXDXy3WKZViRMAoi0"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = "4459955302-6AoQQfoBasGg2JmylCYCjBTSVFOyhqfQE5xqF1l"
access_token_secret = "nFTSXhPZCyXjAQcZ4o6xIqHdLCBmRfbJQwfsDWdDyMzYA"
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_latest_tweet():
    public_tweets = api.user_timeline()
    tweet = public_tweets[0]

    return tweet.text

@app.route('/kindleimage')
def kindle_image():
    image = Image.new('L', (800, 600), 255)

    draw = ImageDraw.Draw(image)
    small_font = ImageFont.truetype('Garamond.otf', 10)

    text = str(datetime.now(timezone('Europe/London')).strftime('%x %X'))
    draw.multiline_text((10, 10), text, font=small_font, spacing=20)

    tweet = get_latest_tweet()

    wrapped_tweet = '\n'.join(textwrap.wrap(tweet, width=30))

    font = ImageFont.truetype('ArnoPro-Caption.otf', 60)
    draw_text_centered(draw, text=wrapped_tweet, center=(400, 288), font=font, spacing=20)

    tagline_font = ImageFont.truetype('Futura LT Medium.otf', 24)
    draw_text_centered(draw, text=u'–\n@GrisedalePike', center=(400, 516), font=tagline_font)

    image = image.transpose(Image.ROTATE_90)

    image_data = StringIO()

    image.save(image_data, format='png')
    image_data.seek(0)
    return image_data.read(), 200, {'content-type': 'image/png', 'refresh': 30}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
