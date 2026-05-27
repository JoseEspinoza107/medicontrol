from flask import render_template, request, redirect

from app.pacientes import bp_pacientes

from app.models import Paciente

from app import db


@bp_pacientes.route('/')
def index():

    pacientes = Paciente.query.all()

    return render_template(
        'pacientes/index.html',
        pacientes=pacientes
    )


@bp_pacientes.route('/nuevo', methods=['GET', 'POST'])
def nuevo():

    if request.method == 'POST':

        nombre = request.form['nombre']

        telefono = request.form['telefono']

        paciente = Paciente(
            nombre=nombre,
            telefono=telefono
        )

        db.session.add(paciente)

        db.session.commit()

        return redirect('/pacientes/')

    return render_template('pacientes/nuevo.html')


@bp_pacientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    paciente = Paciente.query.get(id)

    if request.method == 'POST':

        paciente.nombre = request.form['nombre']

        paciente.telefono = request.form['telefono']

        db.session.commit()

        return redirect('/pacientes/')

    return render_template(
        'pacientes/editar.html',
        paciente=paciente
    )


@bp_pacientes.route('/eliminar/<int:id>')
def eliminar(id):

    paciente = Paciente.query.get(id)

    db.session.delete(paciente)

    db.session.commit()

    return redirect('/pacientes/')