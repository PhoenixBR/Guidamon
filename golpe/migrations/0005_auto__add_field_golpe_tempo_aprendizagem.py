# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Golpe.tempo_aprendizagem'
        db.add_column('golpe_golpe', 'tempo_aprendizagem',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=7200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Golpe.tempo_aprendizagem'
        db.delete_column('golpe_golpe', 'tempo_aprendizagem')


    models = {
        'golpe.golpe': {
            'Meta': {'object_name': 'Golpe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'poder': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'tempo_aprendizagem': ('django.db.models.fields.PositiveIntegerField', [], {'default': '7200'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'velocidade': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'golpe.livro': {
            'Meta': {'object_name': 'Livro'},
            'golpe': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['golpe.Golpe']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'preco': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['golpe']