from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def hello():
	return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
	return render_template(page_name)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
	if request.method == "POST":
		data = request.form.to_dict()
		email = data["email"]
		name = data["name"]
		message = data["message"]
		with open('database.csv', 'a', newline='') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([email, name, message])
		return render_template("thankyou.html")
	else:
		return render_template("tryagain.html")