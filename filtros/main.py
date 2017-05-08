# -*- coding: utf-8 -*-
import os, json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML



html_jinja2_env = Environment(
  loader = FileSystemLoader(os.path.abspath('.')),
  trim_blocks = True
)

# Cargando el json

with open('playlist.json') as json_data:
  d = json.load(json_data)

songs = d['items']

file = html_jinja2_env.get_template('filtros.html')
file_render = file.render(title= 'Playlist-chan', songs=songs).encode("utf-8")

with open("filtros_render.html", "w") as f:
  f.write(file_render)

HTML(string=file_render).write_pdf("filtros.pdf", stylesheets=["style.css"])
