# -*- coding: utf-8 -*-
from django.db import models

import datetime
from django.utils.timezone import utc

class Noticia(models.Model):
	pass

class Anunci(models.Model):
	uri = models.CharField(max_length = 1024)
	pass

class Seccio(models.Model):
	nom = models.CharField(max_length = 1024, null = False, blank = False)
	parent_section = models.ForeignKey("self", null = True, blank = True)
