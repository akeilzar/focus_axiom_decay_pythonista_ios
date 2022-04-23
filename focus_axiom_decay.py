# draw a solid circle by placing a new point at each x y value in the circle qunatized to a bit depth of 128 lololol jajajajaj \/NaSteaknee^ useth scene , how accurate can u draw the shape? or just creative or multiphone movement games why the headset for vr sound interfaces touch interface with vibrate intention of vibration describes object au eng freq 

from scene import *
from math import *
from objc_util import ObjCClass
import random

try:
	def taptic(n: int = 2):
	    ObjCClass('UIDevice').new()._tapticEngine().actuateFeedback_(n)
except:
	pass

# give to me my frenemies

class Game(Scene):
	def setup(self):
		self.decay = 0.001
		self.tick = 1
		#self.frenemies = []
		self.score = 0
		self.square = [50,50]
		self.d = [1, 0]
		self.snake = [[150,150], [150,160], [150,170]]
		self.mag = 1
		self.background_color = False
		self.locations = []
		self.locations_2 = []
		self.p2 = 0
		self.circle_two = []
		self.circle_three = []
		self.sl = LabelNode(str(self.score), position=(self.size.w/2,self.size.h/2), parent=self)
		for x in range(1000):
			self.circle_two.insert(0, [(3*sin(self.tick/4))+get_screen_size()[0]/2+100*sin(x),get_screen_size()[1]/2+100*cos(x)])
		for x in range(1000):
			self.circle_three.insert(0, [get_screen_size()[0]/2+300*sin(x),get_screen_size()[1]/2+300*cos(x)])

	def draw(self):
		g = gravity()
		for cell in self.snake:
			rect(cell[0],cell[1],10,10)
		#print(self.mag)
		for x in range(10):
			self.locations.insert(0, [(3*sin(self.tick/4))+get_screen_size()[0]/2+self.mag*sin(x),get_screen_size()[1]/2+self.mag*cos(x)])
		for div in range(1, 2):
			for x in range(div * 250):
				self.locations_2.insert(0, [sin(g.x)+get_screen_size()[0]/2+2*self.mag/(div+0)*sin(x),get_screen_size()[1]/2+2*self.mag/(div-0)*cos(x)])
		fill('#00ff31')
		for div in range(1, 2):
			for x in range(div * 250):
				self.locations.insert(0, [(sin(g.x)*20)+get_screen_size()[0]/2+self.mag/(div+0)*sin(x),(sin(g.y)*20)+get_screen_size()[1]/2+self.mag/(div-0)*cos(x)])
		for pt in self.locations:
			rect(pt[0],pt[1],1,1)
		fill('white')
		for pt in self.locations_2:
			rect(pt[0],pt[1],1,1)
		fill('#ffa500')
		for pt in self.circle_two:
			rect(pt[0],pt[1],1,1)
		fill('#92ff00')
		for pt in self.circle_three:
			rect(pt[0],pt[1],1,1)
		fill('red')
		for pt in self.circle_three:
			rect((self.size.w/2)+(400*sin(g.x)),(self.size.h/2)+(400*sin(g.y)),1,1)
			
		fill('#ffffff')
		self.tick += 1
		if self.tick == 100:
			self.tick = 0
		
		rect(self.square[0],self.square[1],22,22)
		
		self.square[0] = (3*sin(self.tick/4)) + self.square[0]
		
		self.square[1] = 3*cos(self.tick/4) + self.square[1]
		
		self.d[0] = -0.5*sin(self.tick/8) + self.d[0]
		
		self.d[1] = -0.5*cos(self.tick/8) + self.d[1]
		
		
		fill('#ff3900')
		self.j = sin(g.x) + 128 * sin(self.tick/8) + (self.size.w/2)-5
		self.k = cos(g.y) + 128 * cos(self.tick/8) + (self.size.h/2)-5
		rect(self.j,self.k,10,10)
		
		self.w = sin(g.x) + 256 * sin(self.tick/8) + (self.size.w/1.6)-5
		self.m = cos(g.y) + 256 * cos(self.tick/8) + (self.size.h/1.8)-5
		fill('blue')
		rect(self.w,self.m,10,10)
		
		# eat me with thyme
		
		if self.score == 100:
			self.decay *= 2
		self.score -= self.decay
		self.sl.text = str(int(self.score))
		
		if self.snake[0][0] > self.square[0] and self.snake[0][0] < self.square[0] + 10 and self.snake[0][1] > self.square[1] and self.snake[0][1] < self.square[1] + 10:
			self.score += 1
			self.sl.text = str(self.score)
			try:
				taptic()
			except:
				pass
			self.square[0] = 30*sin(self.tick) + random.choice(range(70,int(self.size.w)-70))
			self.square[1] = 30*sin(self.tick) + random.choice(range(120,int(self.size.h)-120))
		
		if self.snake[0][0] > self.j and self.snake[0][0] < self.j + 10 and self.snake[0][1] > self.k and self.snake[0][1] < self.k + 10:
			self.score = 0
			self.sl.text = str(self.score)
			try:
				taptic()
			except:
				pass
			self.square[0] = 30*sin(self.tick) + random.choice(range(70,int(self.size.w)-70))
			self.square[1] = 30*sin(self.tick) + random.choice(range(120,int(self.size.h)-120))
		
		if self.snake[0][0] > self.w and self.snake[0][0] < self.w + 10 and self.snake[0][1] > self.m and self.snake[0][1] < self.m + 10:
			self.score = 0
			self.sl.text = str(self.score)
			try:
				taptic()
			except:
				pass
			self.square[0] = 30*sin(self.tick) + random.choice(range(70,int(self.size.w)-70))
			self.square[1] = 30*sin(self.tick) + random.choice(range(120,int(self.size.h)-120))
		
		if self.snake[0][0] > self.size.w or self.snake[0][0] < 0 or self.snake[0][1] > self.size.h or self.snake[0][1] < 0:
			try:
				taptic()
			except:
				pass
			if self.score > 0:
				self.score -= 1
				self.sl.text = str(self.score)
		
	def update(self):
		g = gravity()
		self.snake.insert(0, [self.snake[0][0] + self.d[0], self.snake[0][1] + self.d[1]])
		self.snake.pop()
		self.d[0] = sin(g.x) * 3.14159265 * 11
		self.d[1] = sin(g.y) * 3.14159265 * 11
		
		# why does sin work here?
		'''
		the values are always been 0 and 1 since sin is cyclical
		
		gyroscope already takes care of motion sin is used to scale the output of g to a useful value
		'''
		self.mag += 8
		self.locations = []
		self.locations_2 = []
		if self.mag > self.size.h:
			self.mag = 1

if __name__ == '__main__':
	run(Game(),PORTRAIT,show_fps=True)
