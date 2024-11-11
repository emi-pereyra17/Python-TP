from flask import Blueprint, render_template, redirect, url_for, request, flash

from models import Photo
from forms import PhotoForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    from app import db
    photos = Photo.query.all()
    return render_template('index.html', photos=photos)

@main.route('/add', methods=['GET', 'POST'])
def add_photo():
    from app import db
    form = PhotoForm()
    if form.validate_on_submit():
       
        if form.image_url.data:  
            image_path = form.image_url.data  
        else:
            flash('Por favor, proporciona una URL de la imagen.', 'danger')
            return redirect(url_for('main.add_photo'))

       
        new_photo = Photo(
            title=form.title.data,
            description=form.description.data,
            image=image_path  
        )
        db.session.add(new_photo)
        db.session.commit()
        flash('Foto añadida exitosamente!', 'success')  
        return redirect(url_for('main.index'))  
    
    return render_template('photo_form.html', form=form)  

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_photo(id):
    from app import db
    photo = Photo.query.get_or_404(id)
    form = PhotoForm(obj=photo)
    if form.validate_on_submit():
        
        photo.title = form.title.data
        photo.description = form.description.data
        
        
        if form.image_url.data:
            photo.image = form.image_url.data

        db.session.commit()
        flash('Foto actualizada exitosamente!', 'success')
        return redirect(url_for('main.index'))
    return render_template('photo_form.html', form=form, photo=photo)

@main.route('/delete/<int:id>', methods=['POST'])
def delete_photo(id):
    from app import db
    photo = Photo.query.get_or_404(id)
    db.session.delete(photo)
    db.session.commit()
    return redirect(url_for('main.index'))
