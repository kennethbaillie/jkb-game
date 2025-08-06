import os
import sys
scriptpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(scriptpath, 'pythonista-spritekit/'))
from spritekit import *
import ui, math, random
import vector

ball_radius = 13

class PoolScene(Scene):
  
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
    if self.cue_ball.collision_bitmask == 1:
      t = self.cue_ball.position - touch.location
      self.cue_ball.velocity = (3*t.x, 3*t.y)
      self.power_indicator.hidden = True
    else:
      play_area = Rect(-118, -228, 236, 456)
      if play_area.contains_point(touch.location):
        self.cue_ball.collision_bitmask = 1
        self.cue_ball.category_bitmask = 1
      else:
        self.cue_ball.position = (0, -290)

scene = PoolScene(
  background_color='green',
  physics=BilliardsPhysics,
  anchor_point=(0.5,0.5),
  #physics_debug=True,
)

v = 240
h = 130

ball_pos = vector.Vector(0, 110)

platforms = (
  (60, "blue"),
  (180, "blue"),
  (120, "blue")
)

to_next_ball = vector.Vector(2*ball_radius,0)
for angle, color in platforms:
  to_next_ball.degrees = angle
  ball_pos += to_next_ball
  x,y = ball_pos
  
  BoxNode(
    radius=ball_radius,
    fill_color=color,
    line_color=color,
    category_bitmask=1,
    collision_bitmask=1,
    parent=scene,
    position=(x,y),
  )

p = ui.Path()
p.line_to(10,10)
scene.power_indicator = ShapeNode(p,
  hidden=True,
  no_body=True,
  hull=True,
  line_color=(1,1,1,0.3),
  line_width=3,
  glow_width=2,
  parent=scene
)

class CueBall(CircleNode):
  pass
    
scene.cue_ball = CueBall(
  radius=ball_radius,
  fill_color='white',
  parent=scene,
  category_bitmask=1,
  collision_bitmask=1,
  position=(0, -125),
)
  
run(scene, 'full_screen', hide_title_bar=True)
