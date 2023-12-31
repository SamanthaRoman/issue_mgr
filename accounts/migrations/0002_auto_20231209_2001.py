# Generated by Django 5.0 on 2023-12-09 20:01

from django.db import migrations

# name of function can be anything for examle elephant. 
# we just choose to name it what it does. ie populate team


# function 1
def populate_team(apps, schemaeditor):
    entries = {
        "alpha": "The A team",
        "bravo": "The B team",
        "charlie": "The C team",
        "delta": "The D team",
    }
    Team = apps.get_model("accounts", "Team")
    for key, value in entries.items():
        team_obj = Team(name=key, description=value)
        team_obj.save()


# function 2 
def populate_roles(apps, schemaeditor):
    entries = {
        "devloper": "The person on the team who completes issues",
        "scrum master": "The team's coach",
        "product owner": "The person on the team who writes the issues"
    }
    Role = apps.get_model("accounts", "Role")
    for key, value in entries.items():
        role_obj = Role(name=key, description=value)
        role_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        #add operations here. 
        migrations.RunPython(populate_team),
        migrations.RunPython(populate_roles)
    ]
