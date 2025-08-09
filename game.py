import os
import sys
scriptpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(scriptpath, 'pythonista-spritekit/'))
from spritekit import *
import ui, math, random
import vector

class game_scene(Scene):
  
  def touch_moved(self, touch):
    if self.player.collision_bitmask == 1:
      p = ui.Path()
      p.line_to(*(self.player.position - touch.location))
    else:
      self.player.position = touch.location
  
  def touch_ended(self, touch):
    if self.player.collision_bitmask == 1:
      t = self.player.position - touch.location
      self.player.velocity = (3*t.x, 3*t.y)
    else:
      play_area = Rect(-118, -228, 236, 456)
      if play_area.contains_point(touch.location):
        self.player.collision_bitmask = 1
        self.player.category_bitmask = 1
      else:
        self.player.position = (0, -290)

scene = game_scene(
  background_color='black',
  anchor_point=(0.5,0.5),
  #physics = BilliardsPhysics,
  physics_debug=True,
)

platforms = (
  (-200, 200, 100, 10, "blue"),
  (-100, 200, 100, 10, "blue"),
  (-0, 200, 100, 10, "blue"),
  (100, 200, 100, 10, "blue"),
  (200, 200, 100, 10, "blue"),
  (-200, -200, 100, 10, "red"),
  (-100, -200, 100, 10, "red"),
  (-0, -200, 100, 10, "red"),
  (100, -200, 100, 10, "red"),
  (200, -200, 100, 10, "red"),
)

for x,y,w,h, color in platforms:
  BoxNode(
    fill_color=color,
    line_color=color,
    category_bitmask=1,
    collision_bitmask=1,
    parent=scene,
    position=(x,y),
    size=(w,h),
    mass=50,
    affected_by_gravity = False,
  )

class playersprite(BoxNode):
  pass
    
scene.player = playersprite(
  fill_color='white',
  parent=scene,
  category_bitmask=1,
  collision_bitmask=1,
  position=(0, 0),
  mass=0.5,
)
  
run(scene, 'full_screen', hide_title_bar=False)
