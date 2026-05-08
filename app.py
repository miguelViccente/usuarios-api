from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "TV Girl"},
    {"id": 2, "nome": "Tame Impala"},
    {"id": 3, "nome": "Melanie Martinez"},
    {"id": 4, "nome": "Malcom Todd"},
    {"id": 5, "nome": "PinkPantheress"},
    {"id": 6, "nome": "Steve Lacy"},
    {"id": 7, "nome": "EsDeeKid"},
    {"id": 8, "nome": "Tyler, The Creator"},
    {"id": 9, "nome": "Playboi Carti"},
    {"id": 10, "nome": "A$AP Rocky"},
    {"id": 11, "nome": "Don Toliver"},
    {"id": 12, "nome": "Kendrick Lamar"},
    {"id": 13, "nome": "Frank Ocean"},
    {"id": 14, "nome": "Rita Lee"},
    {"id": 15, "nome": "Mac DeMarco"},
    {"id": 16, "nome": "Urias"},
    {"id": 17, "nome": "Charli XCX"},
    {"id": 18, "nome": "Ariana Grande"},
    {"id": 19, "nome": "Mother Mother"},
    {"id": 20, "nome": "Marina"},
    {"id": 21, "nome": "JAY-Z"},
    {"id": 22, "nome": "ABBA"},
    {"id": 23, "nome": "Lana Del Rey"},
    {"id": 24, "nome": "Link do Zap"},
    {"id": 25, "nome": "Current Joys"},
    {"id": 26, "nome": "Yeat"},
    {"id": 27, "nome": "Alex G"},
    {"id": 28, "nome": "SZA"},
    {"id": 29, "nome": "Doja Cat"},
    {"id": 30, "nome": "The Strokes"},
    {"id": 31, "nome": "pumapjl"}
]

@app.route('/')
def home():
    return jsonify({
        "mensagem": "API de usuários funcionando!",
        "rota": "/usuarios"
    })

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    novo = request.json

    if not novo or 'nome' not in novo:
        return jsonify({
            "erro": "O campo 'nome' é obrigatório"
        }), 400

    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": novo['nome']
    }

    usuarios.append(novo_usuario)

    return jsonify(novo_usuario), 201


if __name__ == '__main__':
    app.run(debug=True)