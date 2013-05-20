# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Golpe.tipo2'
        db.delete_column('golpe_golpe', 'tipo2')

        # Adding field 'Golpe.nome'
        db.add_column('golpe_golpe', 'nome',
                      self.gf('django.db.models.fields.CharField')(default='nome', unique=True, max_length=50),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Golpe.tipo2'
        raise RuntimeError("Cannot reverse this migration. 'Golpe.tipo2' and its values cannot be restored.")
        # Deleting field 'Golpe.nome'
        db.delete_column('golpe_golpe', 'nome')


    models = {
        'golpe.golpe': {
            'Meta': {'object_name': 'Golpe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'poder': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'velocidade': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['golpe']