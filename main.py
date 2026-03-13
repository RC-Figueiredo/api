from flask import Flask, jsonify
import os

app = Flask(__name__)

jogo= [
    {"id":1,"nome":"fnaf"},
    {"id":2,"nome":"amoungs us"},
]

@app.route("/alunos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de jogo"})

@app.route("/", methods=["GET"])
def listar_jogo():
    return jsonify(jogo)

if __name__ == "__main__": 
    port=int(os.envicorn.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)