# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import utc
import datetime

class Entrada(models.Model):
	titol = models.CharField(max_length = 256)
	entradeta = models.CharField(max_length = 1024)
	cos = models.CharField(max_length = 4000)
	data_creacio = models.DateTimeField()
	data_publicacio = models.DateTimeField()

class Enllac(models.Model):
	pass
