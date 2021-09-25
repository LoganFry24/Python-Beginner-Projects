import pygame
#the window
class Window:
	#Constants
	def __init__(self):
		pygame.init()

class View(Window):
	def __init__(self,WIDTH,HEIGHT,bgcolor,linecolor, LINEWIDTH,CIRCLE_COLOR,CROSS_COLOR):
		self.WIDTH=WIDTH
		self.HEIGHT=HEIGHT
		self.bgcolor=bgcolor
		self.linecolor=linecolor
		self.LINEWIDTH=LINEWIDTH
		self.CIRCLE_COLOR=CIRCLE_COLOR
		self.CROSS_COLOR=CROSS_COLOR
		self.SetWindow()
	def SetWindow(self):
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_caption('TIC TAC TOE')
		self.screen.fill(self.bgcolor)
	def Drawlines(self):
		#draw the vertical lines
		pygame.draw.line(self.screen, self.linecolor, (self.WIDTH/3,0),(self.WIDTH/3,self.HEIGHT),self.LINEWIDTH)
		pygame.draw.line(self.screen, self.linecolor, (self.WIDTH/3*2,0),(self.WIDTH/3*2,self.HEIGHT),self.LINEWIDTH)
		# draw the horizontal lines
		pygame.draw.line(self.screen, self.linecolor, (0,self.HEIGHT/3),(self.WIDTH,self.HEIGHT/3),self.LINEWIDTH)
		pygame.draw.line(self.screen, self.linecolor, (0,self.HEIGHT/3*2),(self.WIDTH,self.HEIGHT/3*2),self.LINEWIDTH)
	def restart(self):
		self.screen.fill( self.bgcolor )
		self.Drawlines()
	def draw_figures(self,board):
		SPACE=55
		CIRCLE_RADIUS = 60
		for row in range(3):
			for col in range(3):
				#draw circle
				if board[row][col] == 2:
					pygame.draw.circle( self.screen, self.CIRCLE_COLOR, (int( col * (self.WIDTH/3) + (self.WIDTH/3)//2 ), int( row * (self.WIDTH/3) + (self.WIDTH/3)//2 )), CIRCLE_RADIUS, self.LINEWIDTH )
				#draw cross
				elif board[row][col] == 1:
					pygame.draw.line( self.screen, self.CROSS_COLOR, (col * ((self.WIDTH/3)) + SPACE, row * (self.WIDTH/3) + (self.WIDTH/3) - SPACE), (col * (self.WIDTH/3) + (self.WIDTH/3) - SPACE, row * (self.WIDTH/3) + SPACE), self.LINEWIDTH )	
					pygame.draw.line( self.screen, self.CROSS_COLOR, (col * (self.WIDTH/3) + SPACE, row * (self.WIDTH/3) + SPACE), (col * (self.WIDTH/3) + (self.WIDTH/3) - SPACE, row * (self.WIDTH/3) + (self.WIDTH/3) - SPACE), self.LINEWIDTH )
	def VerticalLine(self,col, player):
		posX = col * self.WIDTH/3 + (self.WIDTH/3)//2
		if player == 1:
			color = self.CROSS_COLOR
		elif player == 2:
			color = self.CIRCLE_COLOR
		pygame.draw.line( self.screen, color, (posX, 15), (posX, self.HEIGHT - 15), self.LINEWIDTH )
	def HorizontalLine(self,row, player):
		posY = row * self.WIDTH/3 + (self.WIDTH/3)//2
		if player == 1:
			color = self.CROSS_COLOR
		elif player == 2:
			color = self.CIRCLE_COLOR
		pygame.draw.line( self.screen, color, (15, posY), (self.WIDTH - 15, posY), self.LINEWIDTH )
	def Adiagonal(self,player):
		if player == 1:
			color = self.CROSS_COLOR
		elif player == 2:
			color = self.CIRCLE_COLOR
		pygame.draw.line( self.screen, color, (15, self.HEIGHT - 15), (self.WIDTH - 15, 15), self.LINEWIDTH )
	def Ddiagonal(self,player):
		if player == 1:
			color = self.CROSS_COLOR
		elif player == 2:
			color = self.CIRCLE_COLOR
		pygame.draw.line( self.screen, color, (15, 15), (self.WIDTH - 15, self.HEIGHT - 15), self.LINEWIDTH )