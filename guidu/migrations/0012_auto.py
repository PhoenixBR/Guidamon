# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field golpes_aprendidos on 'Guidu'
        db.create_table('guidu_guidu_golpes_aprendidos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guidu', models.ForeignKey(orm['guidu.guidu'], null=False)),
            ('livro', models.ForeignKey(orm['golpe.livro'], null=False))
        ))
        db.create_unique('guidu_guidu_golpes_aprendidos', ['guidu_id', 'livro_id'])


    def backwards(self, orm):
        # Removing M2M table for field golpes_aprendidos on 'Guidu'
        db.delete_table('guidu_guidu_golpes_aprendidos')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'preco': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'guidu.guidu': {
            'Meta': {'object_name': 'Guidu'},
            'banheiro': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '8'}),
            'banheiro_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'diversao': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'diversao_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'energia': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'energia_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'esta_dormindo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esta_morto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fome': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'fome_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'golpes_aprendidos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['golpe.Livro']", 'max_length': '5', 'blank': 'True'}),
            'higiene': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '7'}),
            'higiene_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'humor': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '50'}),
            'humor_guicoin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'humor_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jogador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guidus'", 'null': 'True', 'to': "orm['jogador.Jogador']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'social': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '6'}),
            'social_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['guidu.GuiduTipo']"})
        },
        'guidu.guidutipo': {
            'Meta': {'object_name': 'GuiduTipo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'jogador.jogador': {
            'Meta': {'object_name': 'Jogador'},
            'guicoin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'guimoves': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'livros': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['golpe.Livro']", 'symmetrical': 'False', 'blank': 'True'}),
            'update_guimoves': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['guidu']