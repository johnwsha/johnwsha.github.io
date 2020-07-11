from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)
# if __name__ == '__main__':
    # app.run(debug=True)

# @app.route('/')
# def welcome():
# 	return render_template(
# 		"welcome.html"
# 	)

# @app.route('/home')
@app.route('/')
def home():
	return render_template(
		"homepage.html"
	)

# @app.route('/portfolio')
# def portfolio():
# 	return render_template(
# 		"portfolio.html"
# 	)

# @app.route('/car')
# def car():
# 	return render_template(
# 		"car.html"
# 	)

# @app.route('/contact')
# def contact():
# 	return render_template(
# 		"contact.html"
# 	)
