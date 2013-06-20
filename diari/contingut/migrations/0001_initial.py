# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Noticia'
        db.create_table(u'contingut_noticia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'contingut', ['Noticia'])

        # Adding model 'Anunci'
        db.create_table(u'contingut_anunci', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'contingut', ['Anunci'])

        # Adding model 'Seccio'
        db.create_table(u'contingut_seccio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'contingut', ['Seccio'])


    def backwards(self, orm):
        # Deleting model 'Noticia'
        db.delete_table(u'contingut_noticia')

        # Deleting model 'Anunci'
        db.delete_table(u'contingut_anunci')

        # Deleting model 'Seccio'
        db.delete_table(u'contingut_seccio')


    models = {
        u'contingut.anunci': {
            'Meta': {'object_name': 'Anunci'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'contingut.noticia': {
            'Meta': {'object_name': 'Noticia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contingut.seccio': {
            'Meta': {'object_name': 'Seccio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['contingut']