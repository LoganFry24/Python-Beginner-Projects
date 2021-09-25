import pygame
import sys
import math
from view import *
from model import Model
class Controller(Window):
	def __init__(self,WIDTH,HEIGHT,bgcolor,linecolor, LINEWIDTH,CIRCLE_COLOR,CROSS_COLOR):
		self.end=False
		self.method=0
		self.WIDTH=WIDTH
		self.HEIGHT=HEIGHT
		self.bgcolor=bgcolor
		self.linecolor=linecolor
		self.LINEWIDTH=LINEWIDTH
		self.CIRCLE_COLOR=CIRCLE_COLOR
		self.CROSS_COLOR=CROSS_COLOR
	def Input(self,cord):
		if cord>=0 and cord <= self.WIDTH/3:
				c=0
		elif cord>self.WIDTH/3 and cord <= (self.WIDTH/3)*2:
				c=1
		elif cord>=(self.WIDTH/3)*2:
				c=2
		return c
	def Start(self):
		window= View(self.WIDTH,self.HEIGHT,self.bgcolor,self.linecolor,self.LINEWIDTH,self.CIRCLE_COLOR,self.CROSS_COLOR)
		window.Drawlines()
		judge= Model()
		#game loop
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN and self.end==False:
						mouseX = event.pos[0]
						mouseY = event.pos[1]
						#convert the input
						col=self.Input(mouseX)
						row=self.Input(mouseY)
						board=judge.Update(row,col)
						self.end,self.method=judge.Check()
						if self.end != False:
							if self.method=="Horizontal":
								window.HorizontalLine(row, self.end)
							elif self.method=="Vertical":
								window.VerticalLine(col, self.end)
							elif self.method=="Adiagonal":
								window.Adiagonal(self.end)
							elif self.method=="Ddiagonal":
								window.Ddiagonal(self.end)
						window.draw_figures(board)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_r:
						self.end = False
						self.Start()
			pygame.display.update()
	