from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
# from myapp import accomplishments
from myapp.models import Accomplishment
from myapp.accomplishments.forms import AccomplishmentForm

accomplishments = Blueprint('accomplishments', __name__)

@accomplishments.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = AccomplishmentForm()
    if form.validate_on_submit():
        accomplishment = Accomplishment(title=form.title.data, discipline=form.discipline.data, text=form.text.data, user_id=current_user.id)
        db.session.add(accomplishment)
        db.session.commit()
        flash('Accomplishment Created')
        print('Accomplishment was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)

@accomplishments.route('/<int:accomplishment_id>')
def accomplishment(accomplishment_id):
    accomplishment = Accomplishment.query.get_or_404(accomplishment_id) 
    return render_template('accomplishment.html', title = accomplishment.title, date = accomplishment.date, post = accomplishment)

@accomplishments.route('/<int:accomplishment_id>/update',methods=['GET','POST'])
@login_required
def update(accomplishment_id):
    accomplishment = Accomplishment.query.get_or_404(accomplishment_id)   
    if accomplishment.author != current_user:
        abort(403)
    form = AccomplishmentForm()
    if form.validate_on_submit():
        accomplishment.title = form.title.data
        accomplishment.discipline = form.discipline.data
        accomplishment.text = form.text.data
        db.session.commit()
        flash('Accomplishment Updated')
        return redirect(url_for('accomplishments.accomplishment',accomplishment_id=accomplishment.id))
    elif request.method == 'GET':
        form.title.data = accomplishment.title
        form.discipline.data= accomplishment.discipline
        form.text.data = accomplishment.text
    return render_template('create_post.html',title='Updating',form=form)

@accomplishments.route('/<int:accomplishment_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(accomplishment_id):
    accomplishment = Accomplishment.query.get_or_404(accomplishment_id)
    if accomplishment.author != current_user:
        abort(403)
    db.session.delete(accomplishment)
    db.session.commit()
    flash('Accomplishment Deleted')
    return redirect(url_for('core.index'))