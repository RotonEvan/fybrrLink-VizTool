import networkx as nx
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import base64
import io


def draw_graph(node_rem):
	size = 20
	sz = int(size / 2)
	G = nx.grid_2d_graph(sz, sz)

	pos = list(G.nodes())

	for i in range(sz * sz):
		if pos[i][0] % 2 != 0:
			pos[i] = (pos[i][0], pos[i][1] + 0.5)
		pos[i] = (pos[i][0] * 2, int(pos[i][1] * 2))

	a = (2, 1)
	b = (8, 10)
	a1, a2 = a[0], a[1]
	b1, b2 = b[0], b[1]
	# node_rem = list(bresenhamMod(a1, a2, b1, b2))

	G_new = nx.Graph()

	G_new.add_nodes_from(pos)

	fig = plt.figure(figsize=(sz, sz))

	pos1 = {(x, y): (x, y) for x, y in G_new.nodes()}

	G_new.add_edges_from([
		 ((x, y), (x + 2, y + 1))
		 for x in range(0, size - 2, 2)
		 for y in range(1, size - 1, 2)
		 if (x / 2) % 2 != 0] + [
		 ((x, y), (x + 2, y + 1))
		 for x in range(0, size - 2, 2)
		 for y in range(0, size - 1, 2)
		 if (x / 2) % 2 == 0] + [
		 ((x, y), (x + 2, y - 1))
		 for x in range(0, size - 4, 2)
		 for y in range(1, size, 2)
		 if (x / 2) % 2 != 0] + [
		 ((x, y), (x + 2, y - 1))
		 for x in range(0, size - 2, 2)
		 for y in range(2, size, 2)
		 if (x / 2) % 2 == 0] + [
		 ((x, y), (x, y + 2))
		 for x in range(0, size - 2, 2)
		 for y in range(0, size - 2, 2)
		 if (x / 2) % 2 == 0] + [
		 ((x, y), (x, y + 2))
		 for x in range(0, size - 1, 2)
		 for y in range(1, size - 2, 2)
		 if (x / 2) % 2 != 0])

	# print(node_rem)

	nx.draw(G_new, pos=pos1,
			node_color='lightblue',
			with_labels=True,
			node_size=600)
	# G_new.add_edge(a,b, edge_color='b',width = 6)
	# nx.draw(G_new, pos=pos1, node_color="lightblue", with_labels=True, node_size=600)
	for i in node_rem:
		color = "%06x" % random.randint(0, 0xFFFFFF)
		color = "#"+color
		nx.draw(G_new, pos=pos1, nodelist=i, node_color=color, with_labels=True, node_size=600)
	
	# plt.show()
	canvas = FigureCanvas(fig)

	pic_IObytes = io.BytesIO()
	plt.savefig(pic_IObytes, format='png')
	pic_IObytes.seek(0)
	pic_hash = base64.b64encode(pic_IObytes.read())

	return pic_hash



def get_line(start, end):
	x1, y1 = start
	x2, y2 = end

	dx = abs(x2 - x1)
	dy = abs(y2 - y1)

	is_steep = dy > dx

	# Swap start and end points if necessary and store swap state
	swapped = False
	if x1 > x2:
		x1, x2 = x2, x1
		y1, y2 = y2, y1
		swapped = True

	# Recalculate differentials
	dx = abs(x2 - x1)
	dy = abs(y2 - y1)

	decision_var = 2*dy - dx

	is_source_up = False

	if y1 < y2:
		ystep = 2
	else:
		is_source_up = True
		ystep = -2

	# Iterate over bounding box generating points between start and end
	x, y = x1, y1
	points = []
	if is_steep:
		while x <= x2+1:
			if not is_source_up and y > y2:
				break
			elif is_source_up and y < y2:
				break
			points.append((x, y))

			if decision_var < 0:
				decision_var += 4*dy
				x += 1
			else:
				decision_var += 2*(dy-2*dx)
				y += ystep
			x += 1
	else:		
		while x <= x2:
			points.append((x, y))

			if decision_var < 0:
				decision_var += 4*dy
				x += 1
			else:
				decision_var += 2*(dy-2*dx)
				y += ystep
			x += 1
	if points[-1] != (x2, y2):
		extra_point = get_line(points[-1], (x2, y2))
		points.extend(extra_point[1:])

	if swapped:
		points.reverse()
	return points

def find_route(F):
	F_new = []
	lines = []
	for j in F:
		p = (j[1], j[0])
		F_new.append(p)
	for i in range(0, len(F_new)-1, 2):
		print("Source Coordinate \t: ", F[i])
		print("Destination Coordinate \t: ", F[i+1])
		line = get_line(F_new[i], F_new[i + 1])
		line_new = []
		for j in line:
			p = (j[1], j[0])
			line_new.append(p)
		print("Path	\t \t: ", line_new)
		lines.append(line_new)
	
	pic_hash = draw_graph(lines)

	return pic_hash

if __name__ == "__main__":
	F = [(12, 2), (8, 10), (14, 11), (6, 3), (2, 1), (10, 17), (2, 17), (14, 15), (2, 15), (16, 2)]
	# F.reverse()
	F_new = []
	lines = []
	for j in F:
		p = (j[1], j[0])
		F_new.append(p)
	for i in range(0, len(F_new)-1, 2):
		print("Source Coordinate \t: ", F[i])
		print("Destination Coordinate \t: ", F[i+1])
		line = get_line(F_new[i], F_new[i + 1])
		line_new = []
		for j in line:
			p = (j[1], j[0])
			line_new.append(p)
		print("Path	\t \t: ", line_new)
		lines.append(line_new)
	
	draw_graph(lines)
