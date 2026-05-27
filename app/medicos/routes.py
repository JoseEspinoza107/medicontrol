from flask import render_template, request, redirect

from app.medicos import bp_medicos

from app.models import Medico

from app import db


@bp_medicos.route('/')
def index():

    medicos = Medico.query.all()

    return render_template(
        'medicos/index.html',
        medicos=medicos
    )


@bp_medicos.route('/nuevo', methods=['GET', 'POST'])
def nuevo():

    if request.method == 'POST':

        nombre = request.form['nombre']

        especialidad = request.form['especialidad']

        medico = Medico(
            nombre=nombre,
            especialidad=especialidad
        )

        db.session.add(medico)

        db.session.commit()

        return redirect('/medicos/')

    return render_template('medicos/nuevo.html')


@bp_medicos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    medico = Medico.query.get(id)

    if request.method == 'POST':

        medico.nombre = request.form['nombre']

        medico.especialidad = request.form['especialidad']

        db.session.commit()

        return redirect('/medicos/')

    return render_template(
        'medicos/editar.html',
        medico=medico
    )


@bp_medicos.route('/eliminar/<int:id>')
def eliminar(id):

    medico = Medico.query.get(id)

    db.session.delete(medico)

    db.session.commit()

    return redirect('/medicos/')