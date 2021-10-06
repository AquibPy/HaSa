from flask import Flask,render_template,request
import pickle

classifier = pickle.load(open('model.pkl','rb'))
cv = pickle.load(open('cv.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_predict = classifier.predict(vect)
        return render_template('result.html',prediction=my_predict)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)