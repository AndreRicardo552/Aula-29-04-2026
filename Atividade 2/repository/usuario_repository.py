class UsuarioRepository:
    def __init__(self, db):
        self.db = db

    def salvar(self, usuario):
        self.db.insert(usuario)
        return True