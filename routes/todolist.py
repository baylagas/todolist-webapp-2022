from flask import Blueprint, render_template, url_for, redirect
from forms.taskCreateForm import TaskCreateForm
from models.task import Task
from utils.db import db

todolist = Blueprint("todolist", __name__)


@todolist.route("/")
def home():
    return render_template("home.html")


@todolist.route("/main")
def main():
    taskList = Task.query.all()
    return render_template("todolist/home.html", tasks=taskList)


@todolist.route("/create", methods=["GET", "POST"])
def create():
    form = TaskCreateForm()
    if form.validate_on_submit():
        description = form.description.data
        newTask = Task(description)
        db.session.add(newTask)
        db.session.commit()
        return redirect(url_for("todolist.main"))
    return render_template("todolist/create.html", form=form)


@todolist.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    currentTask = Task.query.get(id)
    form = TaskCreateForm(
        description=currentTask.description,
        isFinished=currentTask.isFinished,
    )
    if form.validate_on_submit():
        currentTask.description = form.description.data
        currentTask.isFinished = form.isFinished.data
        db.session.add(currentTask)
        db.session.commit()
        return redirect(url_for("todolist.main"))
    return render_template("todolist/update.html", form=form, id=id)


@todolist.route("/delete/<int:id>")
def delete(id):
    currentTask = Task.query.get(id)
    db.session.delete(currentTask)
    db.session.commit()
    return redirect(url_for("todolist.main"))
