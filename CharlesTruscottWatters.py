
""" Authored by Charles Truscott Watters without instruction solving alone. Rubik's cube 2 x 2 optimal solution. Next few weeks working on this - great time to be alive."""
class RubiksState(object):
	def __init__(self, flt, frt, flb, frb, blt, brt, bld, brd, moves):
		self.moves = moves
		self.flt = flt
		self.frt = frt
		self.flb = flb
		self.frb = frb
		self.blt = blt
		self.brt = brt
		self.bld = bld
		self.brd = brd
		self.top_face = [self.flt[2], self.frt[2], self.blt[2], self.brt[2]]
		self.front_face = [self.flt[0], self.frt[0], self.flb[0], self.frb[0]]
		self.left_face = [self.flt[1], self.flb[1], self.blt[1], self.bld[1]]
		self.right_face = [self.frt[1], self.frb[1], self.brt[1], self.brd[1]]
		self.back_face = [self.blt[0], self.brt[0], self.bld[0], self.brd[0]]
		self.bottom_face = [self.flb[2], self.frb[2], self.bld[2], self.brd[2]]
		print("Left face: {} Right face: {} Front face {} Back face: {} Top face: {} Bottom face: {}".format(self.left_face, self.right_face, self.front_face, self.back_face, self.top_face, self.bottom_face))
	def L1(self):
			"""Avalanching, each cubit is rearranged and reordered """
			temp_blt = self.blt.copy()
			temp_flt = self.flt.copy()
			temp_bld = self.bld.copy()
			temp_flb = self.flb.copy()
			new_blt = [temp_flt[2], temp_flt[1], temp_flt[0]]
			new_flt = [temp_flb[2], temp_flb[1], temp_flb[0]]
			new_flb = [temp_bld[2], temp_bld[1], temp_bld[0]]
			new_bld = [temp_blt[2], temp_blt[1], temp_blt[0]]
			self.moves.append("L1")
			return RubiksState(new_flt, self.frt, new_flb, self.frb, new_blt, self.brt, new_bld, self.brd, self.moves)
	def L2(self):
		self.moves.append("L2")
		for n in range(0, 1):
			temp_blt = self.blt.copy()
			temp_flt = self.flt.copy()
			temp_bld = self.bld.copy()
			temp_flb = self.flb.copy()
			new_blt = [temp_flt[2], temp_flt[1], temp_flt[0]]
			new_flt = [temp_flb[2], temp_flb[1], temp_flb[0]]
			new_flb = [temp_bld[2], temp_bld[1], temp_bld[0]]
			new_bld = [temp_blt[2], temp_blt[1], temp_blt[0]]
			self.blt = new_blt
			self.flt = new_flt
			self.bld = new_bld
			self.flb = new_flb
			side = RubiksState(new_flt, self.frt, new_flb, self.frb, new_blt, self.brt, new_bld, self.brd, self.moves)
		return side
	def Linv(self):
		temp_blt = self.blt.copy()
		temp_flt = self.flt.copy()
		temp_bld = self.bld.copy()
		temp_flb = self.flb.copy()
		
		new_flt = [temp_blt[2], temp_blt[1], temp_blt[0]]
		new_flb = [temp_flt[2], temp_flt[1], temp_flt[0]]
		new_bld = [temp_flb[2], temp_flb[1], temp_flb[0]]
		new_blt = [temp_bld[2], temp_bld[1], temp_bld[0]]
		self.moves.append("L inverse")
		return RubiksState(new_flt, self.frt, new_flb, self.frb, new_blt, self.brt, new_bld, self.brd, self.moves)
#	def R1(self):
#			pass
#		def R2(self):
#			pass
#		def Rinv(self):
#			pass
#		def F1(self):
#			pass
#		def F2(self):
#			pass
#		def Finv(self):
#			pass
#		def B1(self):
#			pass
#		def B2(self):
#			pass
#		def Binv(self):
#			pass
#		def U1(self):
#			pass
#		def U2(self):
#			pass
#		def Uinv(self):
#			pass
#		def D1(self):
#			pass
#		def D2(self):
#			pass
#		def Dinv(self):
#			pass
	def __str__(self):
		return str(("Left face: {} Right face: {} Front face {} Back face: {} Top face: {} Bottom face: {}".format(self.left_face, self.right_face, self.front_face, self.back_face, self.top_face, self.bottom_face)))
			
		def is_solved(self):
			pass
from queue import deque
def Charles():
	
	""" flt, frt, flb, frb, blt, brt, bld, brd, moves """
	cube = RubiksState(["G", "O", "W"], ["G", "R", "W"], ["G", "O", "Y"], ["Y", "B", "O"], ["B", "O", "W"], ["B", "R", "W"], ["R", "B", "Y"], ["Y", "R", "G"], [])
#	nextmove = cube.Linv()
#	print(nextmove, nextmove.moves)
	temp = []
	ops = [lambda x: x.L1(), lambda x: x.L2(), lambda x: x.Linv()]
	for op in ops:
		new = op(cube)
		temp.append(new)
		print(new, new.moves)
	print("State array: {}".format(temp))
	for state in temp:
		print("State: {} Moves: {}".format(state, state.moves))
if __name__ == """__main__""": Charles()