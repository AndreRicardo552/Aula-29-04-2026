from flask import Flask, jsonify, request

class UsuarioViewWeb:
    def __init__(self, controller):
        self.app = Flask(__name__)
        self.controller = controller
        self._configurar_rotas()

    def _configurar_rotas(self):
        @self.app.route("/usuarios", methods=["POST"])
        def preencher_dados():
            dados = request.get_json()
            resposta, status_code = self.controller.cadastrar_usuario(dados)
            return jsonify(resposta), status_code

    def run(self):
        self.app.run(debug=True, port=5001)