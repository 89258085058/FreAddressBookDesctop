from model.project import Project
import random

def test_add_project(app):
    old_projects = app.project.get_project_list()
    project = Project(name="New Project ({0})".format(random.randrange(1, 10)), description="Description")
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_add_project_soap(app):
    app.session.ensure_login(username=app.config['webadmin']['username'], password=app.config['webadmin']['password'])
    old_projects = app.soap.get_project_list(app.config['webadmin']['username'], app.config['webadmin']['password'])
    project = Project(name="New Project ({0})".format(random.randrange(1, 10)), description="Description")
    app.project.create(project)
    new_projects = app.soap.get_project_list(app.config['webadmin']['username'], app.config['webadmin']['password'])
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)