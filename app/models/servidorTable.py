from app import db


class Servidor(db.Model):
    __tablename__ = "servidor"

    cpf = db.Column(db.String(20), nullable=False, primary_key=True)
    siape = db.Column(db.String(20), nullable=True)
    nome = db.Column(db.String(255), nullable=False)
    users_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, cpf, siape, nome, users_id):
        self.cpf = cpf
        self.siape = siape
        self.nome = nome
        self.users_id = users_id

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Servidor %s>" % (self.nome)
