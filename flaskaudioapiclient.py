import requests
import base64
import winsound


response = requests.get('http://f709-2400-1a00-b011-8a7a-c1a-fb9d-6126-da1a.ngrok.io/wav')


jdata = response.json()
audio_enc = jdata['content']

byt = str.encode(audio_enc)


winsound.PlaySound(base64.b64decode(audio_enc), winsound.SND_MEMORY) 





