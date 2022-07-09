from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)

@app.route('/')
def index():
	return render_template('sample.html')

@app.route('/udidit/<name>')
def udidit(name):
	return 'u did it %s!!!' % name
	
@app.route('/sample',methods = ['POST','GET'])
def sample():
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('udidit',name=user))
		
	else:
		user=request.args.get('nm')
		return redirect(url_for('udidit',name=user))
		
if __name__=='__main__':
	app.run(debug = True)	

