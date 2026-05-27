from app import db

class Medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    especialidad = db.Column(db.String(100))

    citas = db.relationship('Cita', backref='medico', lazy=True)


class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    telefono = db.Column(db.String(20))

    citas = db.relationship('Cita', backref='paciente', lazy=True)


class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(20))
    hora = db.Column(db.String(20))

    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))