from flask import Blueprint, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv


views = Blueprint('views', __name__)


def get_synonyms(word):
    
    load_dotenv()
    API_KEY =  os.getenv('API_SECRET_KEY')
    BASE_URL = f'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/'

    response = requests.get(BASE_URL + word + f'?key={API_KEY}')

    data = response.json()

    entries = []

    for entry in data:
        # Prepare a dictionary to store entry data
        entry_dict = {
            'part_of_speech': entry.get('fl', 'N/A'),  # Default to 'N/A' if not present
            'synonyms': [],
            'antonyms': [],
            'definitions': []  
        }

        
        if 'def' in entry:
            for definition_set in entry['def']:
                for sense in definition_set['sseq']:
                    for item in sense:
                        # Extract synonyms
                        if item[0] == 'sense' and 'syn_list' in item[1]:
                            for syn_group in item[1]['syn_list']:
                                for syn in syn_group:
                                    entry_dict['synonyms'].append(syn['wd'])

                        # Extract antonyms
                        if item[0] == 'sense' and 'ant_list' in item[1]:
                            for ant_group in item[1]['ant_list']:
                                for ant in ant_group:
                                    entry_dict['antonyms'].append(ant['wd'])

                        # Extract definitions
                        if item[0] == 'sense' and 'dt' in item[1]:
                            for def_item in item[1]['dt']:
                                if def_item[0] == 'text':
                                    # Remove the {it} tags
                                    clean_definition = def_item[1].replace('{it}', '').replace('{/it}', '')
                                    entry_dict['definitions'].append(clean_definition)

        entries.append(entry_dict)
    return entries


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.is_json:
        word = request.json.get('word')
        synonyms_dict = get_synonyms(word)
        return jsonify(synonyms_dict)
        
    return render_template('index.html')


@views.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@views.route('/contactus')
def contactus():
    return render_template('contactus.html')

@views.route('/socials')
def socials():
    return render_template('socials.html')