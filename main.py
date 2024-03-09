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
    up = keycodes.Up
    down = keycodes.Down
    projector = keycodes.Space

    def on_update(self, update_event, signal):
        self.position += self.direction * self.speed * update_event.time_delta

    def on_key_pressed(self, key_event: KeyPressed, signal):
        if key_event.key == self.left:
            self.direction += ppb.Vector(-1, 0)
        elif key_event.key == self.right:
            self.direction += ppb.Vector(1, 0)
        elif key_event.key == self.up:
            self.direction += ppb.Vector(0, 1)
        elif key_event.key == self.down:
            self.direction += ppb.Vector(0, -1)
        elif  key_event.key == self.projector:
          key_event.scene.add(Projectile(position=self.position + ppb.Vector(0, 0.5)))

    def on_key_released(self, key_event: KeyReleased, signal):
        if key_event.key == self.left:
            self.direction += ppb.Vector(1, 0)
        elif key_event.key == self.right:
            self.direction += ppb.Vector(-1, 0)
        elif key_event.key == self.up:
            self.direction += ppb.Vector(0, -1)
        elif key_event.key == self.down:
            self.direction += ppb.Vector(0, 1)


class Projectile(ppb.Sprite):
  size = 0.25
  direction = ppb.Vector(0, 1)
  speed = 6
  
  def on_update(self, update_event, signal):
    if self.direction:
      direction = self.direction.normalize()
    else:
      direction = self.direction
    self.position += direction * self.speed * update_event.time_delta


class Target(ppb.Sprite):
  
  def on_update(self, update_event, signal):
    for p in update_event.scene.get(kind=Projectile):
      if (p.position - self.position).length <= self.size:
        update_event.scene.remove(self)
        update_event.scene.remove(p)


def setup(scene):
  scene.add(Player())
  
  for x in range(-4, 5, 2):
    scene.add(Target(position=ppb.Vector(x, 3)))

ppb.run(setup=setup)
