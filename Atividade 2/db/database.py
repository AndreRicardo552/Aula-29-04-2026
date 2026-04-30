class Database:
    def __init__(self):
        self.usuarios_db = []

    def insert(self, usuario):
        self.usuarios_db.append(usuario)
        return True