from flask import Flask, jsonify, request #import objects
app = Flask(__name__)  #define app using Flask

#list of dictionaries (items)
languages =[{'name' : 'JavScript'}, {'name' : 'Python'}, {'name' : 'Java'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works'})

@app.route('/lang', methods=['GET'])
def returnAll():
    #key and values
    return jsonify({'languages': languages})

#search by name (key) 
@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    #search lnaguages list for any dictionary that matches the name, put it in a new list
    #search /lang/Python returns just the python information
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})

@app.route('/lang', methods=['POST'])
#add to the list of dictionaries or in real life update DB
def addOne():
    #extract what lnaguage wil be added and adds what name is specified
    language = {'name' : request.json['name']}
    #append to language list dictionaries
    languages.append(language)
    return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    #returns all the languages that match the name
    langs = [language for language in languages if language['name'] == name]
    #update the one record returned
    #looking for name key assign to json object passed in
    #update name to whatever is in the json
    langs[0]['name'] = request.json['name']
    return jsonify({'language': langs[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    #search language list and returns what matches
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages})



if __name__ == '__main__':
    app.run(debug=True,port=8080)  #run app on port 8080 in debug
