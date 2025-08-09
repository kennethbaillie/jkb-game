import os
import sys
scriptpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(scriptpath, 'pythonista-spritekit/'))
from spritekit import *
import ui, math, random
import vector

class game_scene(Scene):
	
	def touch_moved(self, touch):
    if self.cue_ball.collision_bitmask == 1:
      p = ui.Path()
      p.line_to(*(self.cue_ball.position - touch.location))
      self.power_indicator.path = p
      self.power_indicator.position = touch.location
      self.power_indicator.hidden = False
    else:
      self.cue_ball.position = touch.location
	
  def touch_ended(self, touch):
    self.player.velocity = (3, 0)
    
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
    density=500,
    affected_by_gravity = False,
  )

class playersprite(CircleNode):
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
