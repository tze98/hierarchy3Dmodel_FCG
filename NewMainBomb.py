import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame import OPENGLBLIT
from BombLoader import *

WIDTH = 800
HEIGHT = 600
class Hierarchy:
    def __init__(self):
        pygame.init()
        display = (WIDTH, HEIGHT)
        pygame.display.set_mode(display, OPENGL | DOUBLEBUF)
        pygame.display.set_caption('3D BOMB MODEL')
        glClearColor(0.8, 0.6, 1, 0)
        glLightfv(GL_LIGHT0, GL_POSITION,  (0, 0, 100, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.3, 0.2, 0.4, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.6, 0.6, 0.6, 1.0))
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        # LOAD OBJECT
        obj1 = OBJ("newbomb1.obj")
        obj2 = OBJ("o2.obj")
        obj3 = OBJ("o3.obj")
        obj4 = OBJ("newbombtop.obj")
        obj5 = OBJ("newbombeye1.obj")
        obj6 = OBJ("newbombeye2.obj")
        obj7 = OBJ("newbombleg1.obj")
        obj8 = OBJ("newbombleg2.obj")

        obj_list = [obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8]
        current_obj = obj_list[0]

        clock = pygame.time.Clock()

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90.0, WIDTH/float(HEIGHT), 0.1, 100.0)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)

        rotate = move = False
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        Main.Main()
                    elif event.key == K_1:
                        current_obj = obj_list[0]
                    elif event.key == K_2:
                        current_obj = obj_list[1]
                    elif event.key == K_3:
                        current_obj = obj_list[2]
                    elif event.key == K_4:
                        current_obj = obj_list[3]
                    elif event.key == K_5:
                        current_obj = obj_list[4]
                    elif event.key == K_6:
                        current_obj = obj_list[5]
                    elif event.key == K_7:
                        current_obj = obj_list[6]
                    elif event.key == K_8:
                        current_obj = obj_list[7]

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 4:
                        current_obj.zpos = max(1, current_obj.zpos - 1)
                    elif event.button == 5:
                        current_obj.zpos += 1
                    # LEFT CLICK
                    elif event.button == 1:
                        rotate = True
                    # RIGHT CLICK
                    elif event.button == 3:
                        move = False
                elif event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        rotate = False
                    elif event.button == 3:
                        move = False
                elif event.type == MOUSEMOTION:
                    i, j = event.rel
                    if rotate:
                        current_obj.rx += i
                        current_obj.ry += j
                    if move:
                        current_obj.tx += i
                        current_obj.ty -= j

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslatef(0, 0, -10)
            line()
            glTranslatef(0, 0, 10)

            # obj1--WHOLE BOMB
            glPushMatrix()
            glTranslate(obj_list[0].tx, obj_list[0].ty + 3, -obj_list[0].zpos)
            glRotate(obj_list[0].ry+20, 1, 0, 0)
            glRotate(obj_list[0].rx, 0, 1, 0)
            glScale(0.3, 0.3, 0.3)
            glCallList(obj_list[0].gl_list)
            glPopMatrix()
            obj_list[0].rx += 3

            # obj2--BOMB BODY
            glPushMatrix()
            glTranslate(obj_list[1].tx-2.5, obj_list[1].ty+0.5, -obj_list[1].zpos)
            glRotate(obj_list[1].ry, 1, 0, 0)
            glRotate(obj_list[1].rx, 0, 1, 0)
            glScale(0.3, 0.3, 0.3)
            glCallList(obj_list[1].gl_list)
            glPopMatrix()
            obj_list[1].rx += 2

            # obj3--BOMB KEY
            glPushMatrix()
            glTranslate(obj_list[2].tx +2.5, obj_list[2].ty+1, - obj_list[2].zpos)
            glRotate(obj_list[2].ry, 0, 1, 0)
            glRotate(obj_list[2].rx, 0, 1, 0)
            glScale(0.5, 0.5, 0.5)
            glCallList(obj_list[2].gl_list)
            glPopMatrix()
            obj_list[2].ry += -3

            # obj4--BOMB TOP
            glPushMatrix()
            glTranslate(obj_list[3].tx-4, obj_list[3].ty -2, - obj_list[3].zpos)
            glRotate(obj_list[3].ry, 1, 0, 0)
            glRotate(obj_list[3].rx, 0, 1, 0)
            glScale(1.5, 1.5, 1.5)
            glCallList(obj_list[3].gl_list)
            glPopMatrix()
            obj_list[3].rx += 3

            # obj5--BOMB EYE 1
            glPushMatrix()
            glTranslate(obj_list[4].tx -2 , obj_list[4].ty - 4, - obj_list[4].zpos)
            glRotate(obj_list[4].ry+20, 1, 0, 0)
            glRotate(obj_list[4].rx, 0, 1, 0)
            glScale(1.5, 1.5, 1.5)
            glCallList(obj_list[4].gl_list)
            glPopMatrix()
            obj_list[4].rx += 3

            # obj6--BOMB EYE 2
            glPushMatrix()
            glTranslate(obj_list[2].tx, obj_list[5].ty - 2, - obj_list[5].zpos)
            glRotate(obj_list[5].ry, 1, 0, 0)
            glRotate(obj_list[5].rx, 0, 1, 0)
            glScale(1.5, 1.5, 1.5)
            glCallList(obj_list[5].gl_list)
            glPopMatrix()
            obj_list[5].ry += -3

            # obj7--BOMB LEG 1
            glPushMatrix()
            glTranslate(obj_list[2].tx+2, obj_list[6].ty - 4, - obj_list[6].zpos)
            glRotate(obj_list[6].ry, 0, 1, 0)
            glRotate(obj_list[6].rx, 0, 1, 0)
            glScale(0.5, 0.5, 0.5)
            glCallList(obj_list[6].gl_list)
            glPopMatrix()
            obj_list[6].ry += -3

            # obj8--BOMB LEG 2
            glPushMatrix()
            glTranslate(obj_list[2].tx + 4, obj_list[7].ty - 2, - obj_list[7].zpos)
            glRotate(obj_list[7].ry, 0, 1, 0)
            glRotate(obj_list[7].rx, 0, 1, 0)
            glScale(0.5, 0.5, 0.5)
            glCallList(obj_list[7].gl_list)
            glPopMatrix()
            obj_list[7].ry += -3

            pygame.display.flip()

def line():
    glLineWidth(3)
    glBegin(GL_LINES)
    glColor(0, 0, 0)
    glVertex2f(0, 5.5)
    glVertex2f(0, 4)
    glVertex2f(-5, 4)
    glVertex2f(5,4)
    glVertex2f(-5, 4)
    glVertex2f(-5, 3.5)
    glVertex2f(5, 4)
    glVertex2f(5, 3.5)
    glVertex2f(-5, 0.5)
    glVertex2f(-5, -1.5)
    glVertex2f(5, 0.5)
    glVertex2f(5, -1.5)
    glVertex2f(-8, -1.5)
    glVertex2f(8, -1.5)
    glVertex2f(-8, -1.5)
    glVertex2f(-8, -2)
    glVertex2f(-4, -1.5)
    glVertex2f(-4, -5.5)
    glVertex2f(0, -1.5)
    glVertex2f(0, -2)
    glVertex2f(4, -1.5)
    glVertex2f(4, -5.5)
    glVertex2f(8, -1.5)
    glVertex2f(8, -2)
    glEnd()

if __name__ == '__main__':
    Hierarchy()