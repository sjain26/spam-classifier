import uvicorn
from fastapi import FastAPI

import pickle 
import nltk
import string
from spamimmg import Email
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
ps = PorterStemmer()

app = FastAPI()
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.post('/predict')
def text_transform(email:str):
    
    
    
    text = email.lower()
    print(text)
    text = nltk.word_tokenize(text)
    print(text)
    y= []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    print("text------before stopward-----------",text)
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    print("text------before stem-----------",text)
    mail = ""
    for i in text:
        y.append(ps.stem(i))
    
            
        mail = " ".join(y)
    tfidf = pickle.load(open('vectorizer.pkl','rb'))
    model = pickle.load(open('model.pkl','rb'))
    

    vector_input =  tfidf.transform([mail])
    
    result = model.predict(vector_input)[0]
    
    
    if result==1:
         result ="Spam"
    else:
         result ="not Spam"
  
    return result

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)