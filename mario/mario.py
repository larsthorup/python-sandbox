class Field:
  mario_x = 0
  mario_y = 0
  score = 0
  dead = False
  done = False

  def load(self, field_path):
    with open(field_path) as f:
      text = f.read()
      self.cell = list(reversed(text.splitlines()))

  def update_score(self):
    if self.cell[self.mario_y][self.mario_x] == '*':
      self.score = self.score + 1
      self.done = True
    elif self.cell[self.mario_y][self.mario_x] == '#':
      self.dead = True
      self.done = True

  def move_mario(self, direction):
    if direction == 'L':
      self.mario_x = self.mario_x - 1
    elif direction == 'R':
      self.mario_x = self.mario_x + 1
    elif direction == 'U':
      self.mario_y = self.mario_y + 1
    elif direction == 'D':
      self.mario_y = self.mario_y - 1
    print(self.mario_y, self.mario_x)
    self.update_score()
  
  def simulate(self, moves):
    for move in moves:
      self.move_mario(move)
      if self.done:
        if self.dead:
          print('Mario died')
        else:
          print(f'Mario scored {self.score}')
        break
      

field = Field()
field.load('./mario/field.txt')
field.simulate('RRUUURUR')