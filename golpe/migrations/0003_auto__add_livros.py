# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Livro'
        db.create_table('golpe_livro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('preco', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('golpe', ['Livro'])

        # Adding M2M table for field golpe on 'Livro'
        db.create_table('golpe_livro_golpe', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('livro', models.ForeignKey(orm['golpe.livro'], null=False)),
            ('golpe', models.ForeignKey(orm['golpe.golpe'], null=False))
        ))
        db.create_unique('golpe_livro_golpe', ['livro_id', 'golpe_id'])


    def backwards(self, orm):
        # Deleting model 'Livro'
        db.delete_table('golpe_livro')

        # Removing M2M table for field golpe on 'Livro'
        db.delete_table('golpe_livro_golpe')


    models = {
        'golpe.golpe': {
            'Meta': {'object_name': 'Golpe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'poder': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'velocidade': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'golpe.livro': {
            'Meta': {'object_name': 'Livro'},
            'golpe': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['golpe.Golpe']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'preco': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['golpe']