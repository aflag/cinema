# -*- coding: utf-8 -*-
import json
import os
import sys
reload(sys)
sys.path.append(os.path.dirname(__file__) + '/..')
sys.setdefaultencoding('utf-8')

from sys import argv
from jinja2 import Environment
from cinema import constants


TEMPLATE = u"""<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Cinemas da Barra</title>
  <style type="text/css">
    ul {
      list-style-type: none;
      padding: 0;
    }
    li + li {
      border-top: 1px solid #555;
      padding-top: 40px;
    }
  </style>
</head>
<body>
  <h1>Cinemas da Barra</h1>
  {% if delux %}
    <h2>Salas luxosas</h2>
    <ul>
      {% for movie in delux %}
        <li>
          {% if movie.image %}
            <img src="{{ movie.image }}" height="120px" />
          {% endif %}
          <dl>
            {% if movie.title %}
              <dt>Nome</dt><dd><a href="{{ movie.url }}">{{ movie.title.title() }}</a></dd>
            {% endif %}
            {% if movie.sessions %}
              <dt>Sessões</dt><dd>{{ movie.sessions }}</dd>
            {% endif %}
            {% if movie.director %}
              <dt>Diretor</dt><dd>{{ movie.director }}</dd>
            {% endif %}
            {% if movie.theater %}
              <dt>Cinema</dt><dd><img height="25" src="{{ movie.theater.replace(' ', '')+'-logo.jpg' }}" /></dd>
            {% endif %}
            {% if movie.desc %}
              <dt>Descrição</dt><dd>{{ movie.desc }}</dd>
            {% endif %}
            {% if movie.room %}
              <dt>Sala</dt><dd>{{ movie.room }}</dd>
            {% endif %}
          </dl>
        </li>
      {% endfor %}
    </ul>
  {% endif %}
  {% if imax %}
    <h2>Salas IMAX</h2>
    <ul>
      {% for movie in imax %}
        <li>
          {% if movie.image %}
            <img src="{{ movie.image }}" height="120px" />
          {% endif %}
          <dl>
            {% if movie.title %}
              <dt>Nome</dt><dd><a href="{{ movie.url }}">{{ movie.title.title() }}</a></dd>
            {% endif %}
            {% if movie.sessions %}
              <dt>Sessões</dt><dd>{{ movie.sessions }}</dd>
            {% endif %}
            {% if movie.director %}
              <dt>Diretor</dt><dd>{{ movie.director }}</dd>
            {% endif %}
            {% if movie.theater %}
              <dt>Cinema</dt><dd><img height="25" src="{{ movie.theater.replace(' ', '')+'-logo.jpg' }}" /></dd>
            {% endif %}
            {% if movie.desc %}
              <dt>Descrição</dt><dd>{{ movie.desc }}</dd>
            {% endif %}
            {% if movie.room %}
              <dt>Sala</dt><dd>{{ movie.room }}</dd>
            {% endif %}
          </dl>
        </li>
      {% endfor %}
    </ul>
  {% endif %}
  {% if regular %}
    <h2>Salas normais</h2>
    <ul>
      {% for movie in regular %}
        <li>
          {% if movie.image %}
            <img src="{{ movie.image }}" height="120px" />
          {% endif %}
          <dl>
            {% if movie.title %}
              <dt>Nome</dt><dd><a href="{{ movie.url }}">{{ movie.title.title() }}</a></dd>
            {% endif %}
            {% if movie.sessions %}
              <dt>Sessões</dt><dd>{{ movie.sessions }}</dd>
            {% endif %}
            {% if movie.director %}
              <dt>Diretor</dt><dd>{{ movie.director }}</dd>
            {% endif %}
            {% if movie.theater %}
              <dt>Cinema</dt><dd><img height="25" src="{{ movie.theater.replace(' ', '')+'-logo.jpg' }}" /></dd>
            {% endif %}
            {% if movie.desc %}
              <dt>Descrição</dt><dd>{{ movie.desc }}</dd>
            {% endif %}
            {% if movie.room %}
              <dt>Sala</dt><dd>{{ movie.room }}</dd>
            {% endif %}
          </dl>
        </li>
      {% endfor %}
    </ul>
  {% endif %}
</body>
</html>"""

delux = []
imax = []
regular = []
with open(argv[1]) as f:
    for line in f:
        movie = json.loads(line)
        if movie['room_type'] == constants.ROOM_TYPE['vip']:
            delux.append(movie)
        elif movie['room_type'] == constants.ROOM_TYPE['imax']:
            imax.append(movie)
        else:
            regular.append(movie)

print Environment().from_string(TEMPLATE).render(delux=delux, imax=imax, regular=regular)
