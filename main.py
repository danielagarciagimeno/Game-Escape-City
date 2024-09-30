#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Configuración de rutas
import sys
import os

# Añadir el directorio raiz al PYTHONPATH
proj_dir = os.path.abspath(os.path.join(os.path.dirname(''), '..', '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)

print("Project directory added to PYTHONPATH:", proj_dir)

# Importar módulos del paquete game
from game.locations import INIT_GAME_STATE
from game.functions import start_game

# Inicializar el estado inicial del juego
game_state = INIT_GAME_STATE.copy()

def main():
    start_game(game_state)

if __name__ == "__main__":
    main()

