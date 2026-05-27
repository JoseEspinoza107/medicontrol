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


from flask import render_template, request, redirect

from app.citas import bp_citas

from app.models import Cita

from app import db


@bp_citas.route('/')
def index():

    citas = Cita.query.all()

    return render_template(
        'citas/index.html',
        citas=citas
    )


@bp_citas.route('/nuevo', methods=['GET', 'POST'])
def nuevo():

    if request.method == 'POST':

        fecha = request.form['fecha']

        hora = request.form['hora']

        medico_id = request.form['medico_id']

        paciente_id = request.form['paciente_id']

        cita = Cita(
            fecha=fecha,
            hora=hora,
            medico_id=medico_id,
            paciente_id=paciente_id
        )

        db.session.add(cita)

        db.session.commit()

        return redirect('/citas/')

    return render_template('citas/nuevo.html')


@bp_citas.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    cita = Cita.query.get(id)

    if request.method == 'POST':

        cita.fecha = request.form['fecha']

        cita.hora = request.form['hora']

        cita.medico_id = request.form['medico_id']

        cita.paciente_id = request.form['paciente_id']

        db.session.commit()

        return redirect('/citas/')

    return render_template(
        'citas/editar.html',
        cita=cita
    )


@bp_citas.route('/eliminar/<int:id>')
def eliminar(id):

    cita = Cita.query.get(id)

    db.session.delete(cita)

    db.session.commit()

    return redirect('/citas/')