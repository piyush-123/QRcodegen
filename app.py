import segno

qrcode = segno.make_qr("Hello World")
qrcode_rotated = qrcode.to_pil(scale=5,light="lightblue",dark="red",quiet_zone="maroon",data_dark="green").rotate(45,expand=True)
#qrcode_rotated.save('scaled_07_qrcode.png',scale=5,light="lightblue",dark="red",quiet_zone="maroon",data_dark="green")
qrcode_rotated.save('roated_02_qr.png')



