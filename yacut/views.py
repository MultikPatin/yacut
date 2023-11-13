from flask import flash, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import generate_link_end


@app.route("/", methods=["GET", "POST"])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if short:
            if URLMap.query.filter_by(short=short).first():
                flash("Предложенный вариант короткой ссылки уже существует")
                return render_template("index.html", form=form)
        else:
            short = generate_link_end()
        url_map = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template("index.html", form=form, short=url_map.short)
    return render_template("index.html", form=form, short="")
