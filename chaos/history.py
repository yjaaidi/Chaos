
import json

from flask_restful import marshal
from flask import g
from fields import disruption_fields
from chaos.models import HistoryDisruption
from chaos import db

def save_in_database(disruption_id, disruption_json):
    history_disruption = HistoryDisruption()

    history_disruption.disruption_id = disruption_id
    history_disruption.data = disruption_json
    db.session.add(history_disruption)
    db.session.commit()

def clean_before_save_in_history(disruption):
    if not isinstance(disruption, dict) and not isinstance(disruption, list):
        return
    for key in disruption.keys():
        if key in ['self', 'href', 'pagination']:
            disruption.pop(key)
        elif isinstance(disruption[key], dict):
            clean_before_save_in_history(disruption[key])
        elif isinstance(disruption[key], list):
            for item in disruption[key]:
                clean_before_save_in_history(item)

def save_disruption_in_history(data):
    old_display_impacts = g.get('display_impacts')
    g.display_impacts = True
    disruption = marshal(data, disruption_fields)
    g.display_impacts = old_display_impacts

    clean_before_save_in_history(disruption)
    disruption['impacts'] = disruption['impacts']['impacts']
    save_in_database(data.id, json.dumps(disruption))
