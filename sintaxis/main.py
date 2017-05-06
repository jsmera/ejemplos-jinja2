# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, FileSystemLoader



html_jinja2_env = Environment(
  loader = FileSystemLoader(os.path.abspath('.')),
  trim_blocks = True
)

file = html_jinja2_env.get_template('ejemplo1.html')
file_render = file.render(title='Ejemplos de sintaxis',
              cities=["Cali", "Bogota", "Medellin", "Barranquilla", "Pereira"],
              user_authenticated=True, number=50,
              imgs=[{'nombre': 'Albert Camus', 'url': 'http://www.biografiasyvidas.com/biografia/c/fotos/camus.jpg'},
              {'nombre': 'San Agustin de Hipona', 'url':'http://filosofia.laguia2000.com/wp-content/uploads/2008/09/biografia-de-san-agustin-de-hipona.jpg'},
              {'nombre': 'Habermas', 'url': 'http://citelighter-cards.s3.amazonaws.com/p16pimj0bh1rip1oni161e1qfod450_16166.jpg'},
              {'nombre': 'Michel Foucault', 'url': 'https://media1.britannica.com/eb-media/88/61988-004-DDE63C75.jpg'}
              ]).encode("utf-8")
print(file_render)

# Guardar el archivo renderizado
with open("ejemplo1_render.html", "w") as f:
  f.write(file_render)
