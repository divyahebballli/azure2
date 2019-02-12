from flask import Flask,jsonify
from flask import request
app = Flask(__name__)

languages =[{'name':'java'},{'name':'python'}]
print(type(languages))
new={'name':'k'}
languages.append(new)
print(languages)

@app.route('/',methods=['GET'])
def test():
    return jsonify({'message':'it works'})


@app.route('/lang',methods=['GET'])
def returnall():
    return jsonify({'languages':languages})

@app.route('/lang/<string:name>',methods=['GET'])
def returnone(name):
    langs=[language for language in languages if language['name']== name]
    return jsonify({'language':langs[0]})

@app.route('/langs',methods=['POST'])
def addOne():
    try:
     language={'name': request.json['name']}
     languages.append(language)
     return jsonify({'languages':languages})
    except TypeError:
      return jsonify({'languages':languages})

if __name__=='__main__':
    app.run(debug=True,port=8080)