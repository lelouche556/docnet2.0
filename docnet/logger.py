from datetime import datetime

from docnet.models import Action
from docnet.models import Statistics

def log(type, description, user):
    action = Action(
        type=type,
        timePerformed=datetime.now(),
        description=description,
        user=user,
    )
    action.save()


def statlog(stats):
    stat = Statistics(
        stats = stats)
    stat.save()
