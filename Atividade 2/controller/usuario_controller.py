class UsuarioController:
    def __init__(self, service):
        self.service = service

    def cadastrar_usuario(self, dados):
        try:
            usuario = self.service.validar_e_criar_usuario(dados)
            return {"mensagem": "Sucesso", "usuario": usuario}, 201
        except ValueError as erro:
            return {"erro": str(erro)}, 400