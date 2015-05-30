# Show this dictionary using a template
# The template is in the folder views/
# The name of the template is the filename without the .tpl extension

import bottle

mythings = ['Brown paper packages', 'string', 'raindrops', 'large scaly thinges with teeth']

@bottle.route('/')
def home_page():
#    mythings = ['Brown paper packages', 'string', 'raindrops', 'large scaly thinges with teeth']
    return bottle.template('hello_template', things=mythings)

@bottle.post('/fav')
def myfavs():
    thing = bottle.request.forms.get("favthing")
    return bottle.template('hello_template', things=mythings, favthing=thing)

bottle.debug(True)
bottle.run(host='localhost', port=8080)
