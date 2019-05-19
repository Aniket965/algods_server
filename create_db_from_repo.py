
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','algods_server.settings')


import django
django.setup()

from Algorithm.models import  Algorithm, Language, Category, Code
import json



def add_Language(lang):
   l,_ = Language.objects.get_or_create(lang_name=lang)
   return l
def add_algorithm(name,langs):
    algo,_ = Algorithm.objects.get_or_create(name=name)
    for lang in langs:
        try:    
            algoCode = json.load(open("_api/algoLang/"+name+"-"+lang+".json"))
            algo.langs.add(add_Language(lang))
            algo.save()
            code,_ = Code.objects.get_or_create(content=algoCode['mainALGO'],algo = algo,lang = add_Language(lang))
        except:
            print("[+]  ","_api/algoLang/"+name+"-"+lang+".json"," Something went wrong !")

        
try:
    langs_json  = open('_api/langs.json')
    algos_json = open('_api/algoList.json')

    langs = json.load(langs_json)
    algos_files = json.load(algos_json)
    for lang in langs['languages']:
        add_Language(lang)
    for algo in algos_files['availabe_algo']:
        algo_data = json.load(open('_api/algos/' + algo +".json"))
        langs = algo_data['langauges']
        add_algorithm(algo,langs)
        
except:
    print("You haven't build algopack api see README for instructions")