import ppb
from ppb import keycodes
from ppb.events import KeyPressed, KeyReleased

class Player(ppb.Sprite):
  image = ppb.Image("smokey.png")
  size = 5
  position = ppb.Vector(0, -3)
  direction = ppb.Vector(0, 0)
  speed = 4
  left = keycodes.Left
  right = keycodes.Right
  
  def on_update(self, update_event, signal):
    self.position += self.direction * self.speed * update_event.time_delta
    
  def on_key_pressed(self, key_event: KeyPressed, signal):
    if key_event.key == self.left:
      self.direction += ppb.Vector(-1, 0)
    elif key_event.key == self.right:
      self.direction += ppb.Vector(1, 0)

  def on_key_released(self, key_event: KeyReleased, signal):
    if key_event.key == self.left:
      self.direction += ppb.Vector(1, 0)
    elif key_event.key == self.right:
      self.direction += ppb.Vector(-1, 0)

def setup(scene):
  scene.add(Player())

ppb.run(setup=setup)