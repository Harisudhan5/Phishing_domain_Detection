import pickle
import numpy as np
from feature import FeatureExtraction
with open('C://Projects//Phishing//Url Classification//classifier_2//classifier_2//apps//phish.pkl', 'rb') as file:
    gbc = pickle.load(file)
    url = "https://repairs-iv-magazine-specialty.trycloudflare.com/"
    ul = FeatureExtraction(url)
    x = np.array(ul.getFeaturesList()).reshape(1,30) 
    y_pred =gbc.predict(x)[0]
    y_pro_phishing = gbc.predict_proba(x)[0,0]
    y_pro_non_phishing = gbc.predict_proba(x)[0,1]
    print("op",y_pred)
    print("phishing probabilty :",y_pro_phishing)
    print("non phishing probability :",y_pro_non_phishing)
