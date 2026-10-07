# 사용법: python make_qr.py https://본인계정.github.io/저장소이름/
# 준비:   pip install qrcode pillow
import sys, qrcode
url = sys.argv[1]
q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=14, border=2)
q.add_data(url); q.make(fit=True)
q.make_image(fill_color="black", back_color="white").save("qr.png")
print("qr.png 저장 완료:", url)
