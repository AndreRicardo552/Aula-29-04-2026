class UsuarioService:
    def __init__(self, repository):
        self.repository = repository

    def validar_e_criar_usuario(self, dados):
        if "nome" not in dados or "email" not in dados:
            raise ValueError("Nome e e-mail são obrigatórios")
        
        usuario = {"nome": dados["nome"], "email": dados["email"]}
        self.repository.salvar(usuario)
        return usuario