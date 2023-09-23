import segno
from urllib.request import urlopen

qrcode_1 = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
url_1 = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")

qrcode_1.to_artistic(background=url_1,target="animated_qr.gif",scale=5)

