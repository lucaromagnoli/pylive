from live.constants import *

import live.query
import live.object

import random

class Scene(live.LoggingObject):
	""" An object representing a single scene in a Live set.

	Properties:
	index -- index of this scene
	name -- human-readable name
	"""

	def __init__(self, set, index):
		""" Create a new scene.
		
		Arguments:
		index -- index of this scene
		"""
		self.set = set
		self.index = index
		self.name = None
		self.indent = 2

	def __str__(self):
		name = ": %s" % self.name if self.name else ""
		
		return "live.scene(%d)%s" % (self.index, name)

	def play(self):
		""" Start playing scene. """
		self.trace("playing")
		self.set.play_scene(self.index)
