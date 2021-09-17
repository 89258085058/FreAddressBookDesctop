from model.project import Project
import random

def test_add_project(app):
    old_projects = app.project.get_project_list()
    project = Project(name="New Project ({0})".format(random.randrange(1, 10)), description="Description")
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)