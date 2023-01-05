class Player:

  def __init__(self, name, color):
    self.name = name
    self.color = color
    self.point = 0

  def __repr__(self):
    return f'Player: {self.name}\nColor: {self.color}\nPoints: {self.point}'