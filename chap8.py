from flask import Flask,render_template
app = Flask(__name__)

@app.route('/table')
def index():
	dict = {'physics':88,'chemistry':88,'maths':95}
	return render_template('chap8.html',result=dict)

if __name__ == '__main__':
	app.run(debug=True)
