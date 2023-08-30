from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import plotly.graph_objects as go
import os
import re
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math



        



#########################################################""
class ActionShowCube(Action):
    def name(self) -> Text:
        return "action_show_window"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = tracker.latest_message.get('text')
        pattern = r"\b(\d+(\.\d+)?)\s*(?:x|par|by|sur|sur\s)?\s*(\d+(\.\d+)?)\s*(?:x|par|by|sur|sur\s)?\s*(\d+(\.\d+)?)\b"  # Expression régulière pour trouver les valeurs de taille
        match = re.search(pattern, message, re.IGNORECASE)

        length = 2
        width = 2
        height = 2

        verticies = (
        (length / 2, -width / 2, -height / 2),  # Coin avant-gauche en bas
        (length / 2, width / 2, -height / 2),   # Coin avant-droit en bas
        (-length / 2, width / 2, -height / 2),  # Coin arrière-droit en bas
        (-length / 2, -width / 2, -height / 2), # Coin arrière-gauche en bas
        (length / 2, -width / 2, height / 2),   # Coin avant-gauche en haut
        (length / 2, width / 2, height / 2),    # Coin avant-droit en haut
        (-length / 2, -width / 2, height / 2),  # Coin arrière-gauche en haut
        (-length / 2, width / 2, height / 2)    # Coin arrière-droit en haut
    )
        edges = (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7)
            )
        def draw_cylinders():
            glColor3f(0.5, 0.5, 0.5)
            bottom_offset = 0.1
            top_offset = 0.1
            glPushMatrix()
            glTranslatef(0, 1.1 - bottom_offset, 0)  # Décalage vers le bas
            glRotatef(90, 1, 0, 0)  # Rotation du cylindre
            gluCylinder(gluNewQuadric(), 0.4, 0.4, 2.0 + bottom_offset + top_offset, 20, 1)
            glPopMatrix()

        def Cube():
            glBegin(GL_LINES)
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(verticies[vertex])
            glEnd()

        
        def main():
            pygame.init()
            display = (800, 400)
            pygame.display.set_mode(display, DOUBLEBUF | OPENGL)           
            gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
            glTranslatef(0.0, 0.0, -5)
            while True:
                 for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return

                 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                 glRotatef(0.05, 1, 0, 0)  # Rotation lente autour de l'axe OY
                 glRotatef(0.5, 1, 0, 0)
                 glColor3f(1.0, 1.0, 1.0)  # Couleur blanche
                 Cube()
                 draw_cylinders()
                 pygame.display.flip()
                 pygame.time.wait(10)                
        main()        
        return[]
    
class ExtractCubeSize(Action):
    def name(self) -> Text:
        return "extract_cube_size"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = tracker.latest_message.get('text')
        pattern = r"\b(\d+(\.\d+)?)\s*(?:x|par|by|sur|sur\s)?\s*(\d+(\.\d+)?)\s*(?:x|par|by|sur|sur\s)?\s*(\d+(\.\d+)?)\b"  # Expression régulière pour trouver les valeurs de taille
        match = re.search(pattern, message, re.IGNORECASE)
        
        if match:
            length = float(match.group(1))
            width = float(match.group(3))
            height = float(match.group(5))

        verticies = (
        (length / 2, -width / 2, -height / 2),  # Coin avant-gauche en bas
        (length / 2, width / 2, -height / 2),   # Coin avant-droit en bas
        (-length / 2, width / 2, -height / 2),  # Coin arrière-droit en bas
        (-length / 2, -width / 2, -height / 2), # Coin arrière-gauche en bas
        (length / 2, -width / 2, height / 2),   # Coin avant-gauche en haut
        (length / 2, width / 2, height / 2),    # Coin avant-droit en haut
        (-length / 2, -width / 2, height / 2),  # Coin arrière-gauche en haut
        (-length / 2, width / 2, height / 2)    # Coin arrière-droit en haut
    )
        edges = (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7)
            )

        def Cube():
            glBegin(GL_LINES)
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(verticies[vertex])
            glEnd()

        
        def main():
            pygame.init()
            display = (800, 400)
            pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
            

          

            gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

            glTranslatef(0.0, 0.0, -5)

            while True:
                 for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return

                 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

                 glRotatef(0.2, 0, 1, 0)  # Rotation lente autour de l'axe OY
            
                 Cube()  # Dessine le cube

                 glPushMatrix()
                 glTranslatef(1.5, 0.0, 0.0)  # Translation pour positionner la sphère près du cube
                  # Dessine la sphère
                 glPopMatrix()

                 pygame.display.flip()
                 pygame.time.wait(10)
                

        main()
        

        return[]

