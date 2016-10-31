from app import db


class Cadastro(db.Model):
    class Meta:
        abstract = True

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(130))
    endereco = db.Column(db.String(130))
    cidade = db.Column(db.String(100))
    cep = db.Column(db.String(8))
    bairro = db.Column(db.String(100))
    estado = db.Column(db.String(2))

    def __init__(self, nome, endereco, cidade, cep, bairro, estado):
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.cep = cep
        self.bairro = bairro
        self.estado = estado
        
class Fisica(Cadastro):
    id = db.Column(db.Integer, primary_key=True)
    rg = db.Column(db.String(20))
    cpf = db.Column(db.String(18))    

class Juridica(Cadastro):
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(20))
    ie = db.Column(db.String(18))    

class Estado(db.Model):
    id = db.Column(db.String(2), primary_key=True)
    descricao = db.Column(db.String(50))

    def __init__(self, descricao):
        self.descricao = descricao
