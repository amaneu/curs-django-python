# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Seccio.nom'
        db.add_column(u'contingut_seccio', 'nom',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024),
                      keep_default=False)

        # Adding field 'Seccio.parent_section'
        db.add_column(u'contingut_seccio', 'parent_section',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contingut.Seccio'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Seccio.nom'
        db.delete_column(u'contingut_seccio', 'nom')

        # Deleting field 'Seccio.parent_section'
        db.delete_column(u'contingut_seccio', 'parent_section_id')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'parent_section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contingut.Seccio']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contingut']