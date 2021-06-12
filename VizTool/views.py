from .code import bresenham
from django.shortcuts import render
import urllib

import networkx as nx
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import base64
import io


# Create your views here.

def index(request):
	F = [(2, 15), (16, 2)]
	pic_hash, t_d, t_b = bresenham.find_route(F)
	uri =  urllib.parse.quote(pic_hash)
	return render(request, 'index.html', {'data': uri, 'time_d': t_d, 'time_b': t_b})

def input(request):
	if request.method == 'POST':
		print(request.POST.get('start-x'))
		startX = int(request.POST.get('start-x'))
		startY = int(request.POST.get('start-y'))
		endX = int(request.POST.get('end-x'))
		endY = int(request.POST.get('end-y'))

		F = [(startX, startY), (endX, endY)]
		pic_hash, t_d, t_b = bresenham.find_route(F)
		uri =  urllib.parse.quote(pic_hash)
		return render(request, 'index.html', {'data': uri, 'time_d': t_d, 'time_b': t_b})
	

def plot_graph(request):
	F = [(12, 2), (8, 10)]
	pic_hash, t_d, t_b = bresenham.find_route(F)
	uri =  urllib.parse.quote(pic_hash)
	return render(request, 'index.html', {'data': uri, 'time_d': t_d, 'time_b': t_b})