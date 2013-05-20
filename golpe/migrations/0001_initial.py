# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Golpe'
        db.create_table('golpe_golpe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poder', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('velocidade', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('nivel', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('tipo2', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('golpe', ['Golpe'])


    def backwards(self, orm):
        # Deleting model 'Golpe'
        db.delete_table('golpe_golpe')


    models = {
        'golpe.golpe': {
            'Meta': {'object_name': 'Golpe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'poder': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tipo2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'velocidade': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['golpe']