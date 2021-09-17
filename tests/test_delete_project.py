from model.project import Project
import random

def test_delete_some_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="New Project ({0})".format(random.randrange(1, 10)), description="Description"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects


def test_delete_some_project_soup(app):
    app.session.ensure_login(username=app.config['webadmin']['username'], password=app.config['webadmin']['password'])
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="New Project ({0})".format(random.randrange(1, 10)), description="Description"))
    old_projects = app.soap.get_project_list(app.config['webadmin']['username'], app.config['webadmin']['password'])
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list(app.config['webadmin']['username'], app.config['webadmin']['password'])
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects