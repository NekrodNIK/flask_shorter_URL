from flask import Flask, render_template, request
import bitly_api 

BITLY_ACCESS_TOKEN ="b904a9c8c944408e7abf4b333910da4733f43bfb"
b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN) 
app = Flask(__name__, static_folder='static')

@app.route('/', methods=['post', 'get'])
def login():
	message = ""
	got = ""
	if request.method == 'POST':
		url = request.form.get('url')
		try:

			response = str(b.shorten(url)) 
			urlshort = response.split()[1]
			for i in urlshort:
				if not i == "'" and not i == ",":
					got=got+i
			message = got   
		except bitly_api.bitly_api.BitlyError:
			message = 'Некоректная ссылка'

	return render_template('index.html', message=message) 