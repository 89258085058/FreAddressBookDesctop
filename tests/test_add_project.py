from model.project import Project
import random
import string

username = "administrator"
password = "root"

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits + string.punctuation + " "*10
    return prefix + "".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


def test_create_project(app):
    old_project = app.soap.get_project_list(username, password)
    project = Project(name=random_string("NewName: ", 10))
    app.project.create(project)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_project) + 1 == len(new_projects)
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)