import nltk
from nltk.tokenize import word_tokenize
from flask import Flask,request,jsonify,render_template
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt',quiet=True)
nltk.download('stopwords',quiet=True)

ps = PorterStemmer()

class spamclassifier:
    def __init__(self,tfidf_path, model_path):
        self.tf_idf = pickle.load(open(tfidf_path,'rb'))
        self.model = pickle.load(open(model_path,'rb'))

    def transform_text(seld, text):
        text = text.lower()
        text = word_tokenize(text)
        text = [i for i in text if i.isalnum()]
        text = [i for i in text if i not in stopwords.words('english') and i not in string.punctuation]
        text = [ps.stem(i) for i in text]
        return " ".join(text)
    
    def predict(self,input_sms):
        transformed_sms = self.transform_text(input_sms)
        vector_input = self.tf_idf.transform([transformed_sms])
        result = self.model.predict(vector_input)[0]
        return result
    

app = Flask(__name__)

tfidf_path = r'C:\SMS-Classifier\vectorizer.pkl'
model_path = r'C:\SMS-Classifier\model.pkl'


classifier = spamclassifier(tfidf_path, model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data= request.get_json(force=True)
    input_sms = data.get('message', '')

    if not input_sms:
        return jsonify({'error': 'No message provided'}),400
    
    result = classifier.predict(input_sms)
    predection = "spam" if result==1 else "Not Spam"

    return jsonify({'Message': input_sms,'prediction':predection})

if __name__=='__main__':
    app.run(debug=True)

