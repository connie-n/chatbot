#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, redirect, request, url_for
import CoffeeChatbot

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/', methods=['GET','POST']) # 접속하는 url
def main():
    if request.method =='POST':
        return redirect(url_for('coffeebot'))
    return render_template('main.html')

@app.route('/coffeebot') # 접속하는 url
def coffeebot():
    return render_template('coffeebot.html')

#def index():
#    return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', port='8000')
# host 등을 직접 지정하고 싶다면
# app.run(host="127.0.0.1", port="5000", debug=True)
# Jupyter Notebook에서는 debug시 에러가 뜸


# In[ ]:




