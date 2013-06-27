# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Guidu.esta_treinando'
        db.add_column('guidu_guidu', 'esta_treinando',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Guidu.esta_treinando'
        db.delete_column('guidu_guidu', 'esta_treinando')


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
        },
        'guidu.guidu': {
            'Meta': {'object_name': 'Guidu'},
            'banheiro': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
            'banheiro_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'diversao': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '7'}),
            'diversao_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'energia': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'energia_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'esta_dormindo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esta_morto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'esta_treinando': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fome': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'fome_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'golpe_aprendido1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['golpe.Golpe']"}),
            'golpe_aprendido2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['golpe.Golpe']"}),
            'golpe_aprendido3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['golpe.Golpe']"}),
            'golpe_aprendido4': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['golpe.Golpe']"}),
            'golpe_aprendido5': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['golpe.Golpe']"}),
            'golpe_tempo_treinado': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'golpe_treinando': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['golpe.Golpe']"}),
            'golpe_treinando_desde': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'higiene': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '6'}),
            'higiene_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'humor': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '50'}),
            'humor_guicoin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'humor_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jogador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guidus'", 'null': 'True', 'to': "orm['jogador.Jogador']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'social': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
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