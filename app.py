from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def welcome():
	return render_template(
		"welcome.html"
	)

@app.route('/home')
def home():
	return render_template(
		"homepage.html"
	)

@app.route('/portfolio')
def portfolio():
	return render_template(
		"portfolio.html"
	)
