from flask import Flask,render_template,request, redirect,url_for
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:name_page>')
def html_page(name_page):
    return render_template(name_page)

def write_to_text_file(data):
	with open('database.txt', mode='a') as database:
		name=data["name"]
		mail=data["email"]
		text=data["text"]
		length=database.write(f'{name},{mail},{text}\n')
		return length


def write_to_csv_file(data):
	with open('database.csv', mode='a',newline='') as database2:
		name=data["name"]
		mail=data["email"]
		text=data["text"]
		csv_file=csv.writer(database2,delimiter=',',quotechar='~', quoting=csv.QUOTE_MINIMAL)
		csv_file.writerow([name,mail,text])
		return 

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data=request.form.to_dict()
			write_to_csv_file(data)
			return redirect('/thankyou.html')
		except:
			return 'did not saved in the database'
	else:
		return 'Something was wrong!. Try again.'