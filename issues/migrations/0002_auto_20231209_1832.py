# Generated by Django 5.0 on 2023-12-09 18:32

from django.db import migrations

def populate_status(apps, schemaeditor):    #parameters must always be these and here
    entries = {
        "to do": "An issue that needs to be done",
        "in progress": "A task that is being worked on",
        "done": "A task that has been completed",
    }
    Status = apps.get_model("issues", "Status")   #where we want to retrieve it.
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()



class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
