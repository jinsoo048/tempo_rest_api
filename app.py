import json
import os
import datetime
import hashlib
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from database import list_users, verify, delete_user_from_db, add_user
from database import read_note_from_db, write_note_into_db, delete_note_from_db, match_user_id_with_note_id
from database import image_upload_record, list_images_for_user, match_user_id_with_image_uid, delete_image_from_db
from werkzeug.utils import secure_filename
# JJS ADD
from tempo.tempoapiclient import client
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')


@app.errorhandler(401)
def FUN_401(error):
    return render_template("page_401.html"), 401


@app.errorhandler(403)
def FUN_403(error):
    return render_template("page_403.html"), 403


@app.errorhandler(404)
def FUN_404(error):
    return render_template("page_404.html"), 404


@app.errorhandler(405)
def FUN_405(error):
    return render_template("page_405.html"), 405


@app.errorhandler(413)
def FUN_413(error):
    return render_template("page_413.html"), 413


# JJS ADD BEGIN
@app.route("/tempo/get_data")
def TEMPO_get():
    return render_template("tempo/get_data.html")


@app.route("/get_worklogs", methods=['POST'])
def FUN_get_worklogs():
    if request.method == 'POST':
        tempo = client.Tempo(
            auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
            base_url="https://api.tempo.io/core/3")

        if request.form.get("dateFrom"):
            dateFrom = request.form.get("dateFrom")
        else:
            print("no input")
            return render_template("tempo/get_data.html")

        if request.form.get("dateTo"):
            dateTo = request.form.get("dateTo")
        else:
            print("no input")
            return render_template("tempo/get_data.html")

        results = tempo.get_worklogs(
            dateFrom=dateFrom,
            dateTo=dateTo
        )

        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "worklogs_" + dateFrom + "_" + dateTo + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

    return render_template("tempo/get_data.html", results=results)


@app.route("/get_all", methods=['POST'])
def FUN_get_all():
    if request.method == 'POST':
        tempo = client.Tempo(
            auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
            base_url="https://api.tempo.io/core/3")

        results = tempo.get_accounts()
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "accounts_" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        results = tempo.get_account_categories()
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "categories_" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        results = tempo.get_account_category_types()
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "account_category_types_" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        results = tempo.get_customers()
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "customers_" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        results = tempo.get_holiday_schemes()
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "holiday_schemes_" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        results = tempo.get_teams()
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "teams_" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        results = tempo.get_work_attributes()
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "work_attributes_" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        return render_template("tempo/get_data.html", results=results)


@app.route("/get_accounts", methods=['POST'])


def FUN_get_accounts():
    if request.method == 'POST':
        tempo = client.Tempo(
            auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
            base_url="https://api.tempo.io/core/3")

        results = tempo.get_accounts(
        )

        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "accounts_" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        return render_template("tempo/get_data.html", results=results)


@app.route("/get_account_categories", methods=['POST'])
def FUN_get_account_categories():
    if request.method == 'POST':
        tempo = client.Tempo(
            auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
            base_url="https://api.tempo.io/core/3")

        results = tempo.get_account_categories(
        )

        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "categories_" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        return render_template("tempo/get_data.html", results=results)


@app.route("/get_account_category_types", methods=['POST'])
def FUN_get_account_category_types():
    if request.method == 'POST':
        tempo = client.Tempo(
            auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
            base_url="https://api.tempo.io/core/3")

        results = tempo.get_account_category_types(
        )

        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "account_category_types" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        return render_template("tempo/get_data.html", results=results)


@app.route("/get_customers", methods=['POST'])
def FUN_get_customers():
    if request.method == 'POST':
        tempo = client.Tempo(
            auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
            base_url="https://api.tempo.io/core/3")

        results = tempo.get_customers(
        )

        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "customers" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        return render_template("tempo/get_data.html", results=results)


@app.route("/get_holiday_schemes", methods=['POST'])
def FUN_get_holiday_schemes():
    if request.method == 'POST':
        tempo = client.Tempo(
            auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
            base_url="https://api.tempo.io/core/3")

        results = tempo.get_holiday_schemes(
        )

        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "holiday_schemes" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        return render_template("tempo/get_data.html", results=results)


@app.route("/get_permission_roles", methods=['POST'])
def FUN_get_permission_roles():
    if request.method == 'POST':
        tempo = client.Tempo(
            auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
            base_url="https://api.tempo.io/core/3")

        results = tempo.get_permission_roles(
        )

        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "permission_roles" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        return render_template("tempo/get_data.html", results=results)


@app.route("/get_teams", methods=['POST'])
def FUN_get_teams():
    if request.method == 'POST':
        tempo = client.Tempo(
            auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
            base_url="https://api.tempo.io/core/3")

        results = tempo.get_teams(
        )

        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "teams" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        return render_template("tempo/get_data.html", results=results)


@app.route("/get_work_attributes", methods=['POST'])
def FUN_get_work_attributes():
    if request.method == 'POST':
        tempo = client.Tempo(
            auth_token="7t34jjGvG35YTRJeXk9pVFhFTFgeAA",
            base_url="https://api.tempo.io/core/3")

        results = tempo.get_work_attributes(
        )

        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        dir = "C:\\Users\\42Maru\\Desktop\\TimeReporting\\Tempo Backup\\"
        filename = dir + "work_attributes" + dt_string + ".txt"
        f = open(filename, "x")
        for i in results:
            f.write(json.dumps(i))
        f.close()

        return render_template("tempo/get_data.html", results=results)


# JJS ADD END

@app.route("/")
def FUN_root():
    return render_template("index.html")


@app.route("/public/")
def FUN_public():
    return render_template("public_page.html")


@app.route("/private/")
def FUN_private():
    if "current_user" in session.keys():
        notes_list = read_note_from_db(session['current_user'])
        notes_table = zip([x[0] for x in notes_list], \
                          [x[1] for x in notes_list], \
                          [x[2] for x in notes_list], \
                          ["/delete_note/" + x[0] for x in notes_list])

        images_list = list_images_for_user(session['current_user'])
        images_table = zip([x[0] for x in images_list], \
                           [x[1] for x in images_list], \
                           [x[2] for x in images_list], \
                           ["/delete_image/" + x[0] for x in images_list])

        return render_template("private_page.html", notes=notes_table, images=images_table)
    else:
        return abort(401)


@app.route("/admin/")
def FUN_admin():
    if session.get("current_user", None) == "ADMIN":
        user_list = list_users()
        user_table = zip(range(1, len(user_list) + 1), \
                         user_list, \
                         [x + y for x, y in zip(["/delete_user/"] * len(user_list), user_list)])
        return render_template("admin.html", users=user_table)
    else:
        return abort(401)


@app.route("/write_note", methods=["POST"])
def FUN_write_note():
    text_to_write = request.form.get("text_note_to_take")
    write_note_into_db(session['current_user'], text_to_write)

    return (redirect(url_for("FUN_private")))


@app.route("/delete_note/<note_id>", methods=["GET"])
def FUN_delete_note(note_id):
    if session.get("current_user", None) == match_user_id_with_note_id(
            note_id):  # Ensure the current user is NOT operating on other users' note.
        delete_note_from_db(note_id)
    else:
        return abort(401)
    return (redirect(url_for("FUN_private")))


# Reference: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload_image", methods=['POST'])
def FUN_upload_image():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', category='danger')
            return (redirect(url_for("FUN_private")))
        file = request.files['file']
        # if user does not select file, browser also submit a empty part without filename
        if file.filename == '':
            flash('No selected file', category='danger')
            return (redirect(url_for("FUN_private")))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_time = str(datetime.datetime.now())
            image_uid = hashlib.sha1((upload_time + filename).encode()).hexdigest()
            # Save the image into UPLOAD_FOLDER
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_uid + "-" + filename))
            # Record this uploading in database
            image_upload_record(image_uid, session['current_user'], filename, upload_time)
            return (redirect(url_for("FUN_private")))

    return (redirect(url_for("FUN_private")))


@app.route("/delete_image/<image_uid>", methods=["GET"])
def FUN_delete_image(image_uid):
    if session.get("current_user", None) == match_user_id_with_image_uid(
            image_uid):  # Ensure the current user is NOT operating on other users' note.
        # delete the corresponding record in database
        delete_image_from_db(image_uid)
        # delete the corresponding image file from image pool
        image_to_delete_from_pool = \
            [y for y in [x for x in os.listdir(app.config['UPLOAD_FOLDER'])] if y.split("-", 1)[0] == image_uid][0]
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], image_to_delete_from_pool))
    else:
        return abort(401)
    return (redirect(url_for("FUN_private")))


@app.route("/login", methods=["POST"])
def FUN_login():
    id_submitted = request.form.get("id").upper()
    if (id_submitted in list_users()) and verify(id_submitted, request.form.get("pw")):
        session['current_user'] = id_submitted

    return (redirect(url_for("FUN_root")))


@app.route("/logout/")
def FUN_logout():
    session.pop("current_user", None)
    return (redirect(url_for("FUN_root")))


@app.route("/delete_user/<id>/", methods=['GET'])
def FUN_delete_user(id):
    if session.get("current_user", None) == "ADMIN":
        if id == "ADMIN":  # ADMIN account can't be deleted.
            return abort(403)

        # [1] Delete this user's images in image pool
        images_to_remove = [x[0] for x in list_images_for_user(id)]
        for f in images_to_remove:
            image_to_delete_from_pool = \
                [y for y in [x for x in os.listdir(app.config['UPLOAD_FOLDER'])] if y.split("-", 1)[0] == f][0]
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], image_to_delete_from_pool))
        # [2] Delele the records in database files
        delete_user_from_db(id)
        return (redirect(url_for("FUN_admin")))
    else:
        return abort(401)


@app.route("/add_user", methods=["POST"])
def FUN_add_user():
    if session.get("current_user", None) == "ADMIN":  # only Admin should be able to add user.
        # before we add the user, we need to ensure this is doesn't exsit in database. We also need to ensure the id is valid.
        if request.form.get('id').upper() in list_users():
            user_list = list_users()
            user_table = zip(range(1, len(user_list) + 1), \
                             user_list, \
                             [x + y for x, y in zip(["/delete_user/"] * len(user_list), user_list)])
            return (render_template("admin.html", id_to_add_is_duplicated=True, users=user_table))
        if " " in request.form.get('id') or "'" in request.form.get('id'):
            user_list = list_users()
            user_table = zip(range(1, len(user_list) + 1), \
                             user_list, \
                             [x + y for x, y in zip(["/delete_user/"] * len(user_list), user_list)])
            return (render_template("admin.html", id_to_add_is_invalid=True, users=user_table))
        else:
            add_user(request.form.get('id'), request.form.get('pw'))
            return (redirect(url_for("FUN_admin")))
    else:
        return abort(401)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
