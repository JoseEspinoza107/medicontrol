from flask import Blueprint

bp_medicos = Blueprint(
    'medicos',
    __name__,
    template_folder='../templates'
)

from app.medicos import routes