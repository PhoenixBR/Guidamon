# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GuiduTipo'
        db.create_table('guidu_guidutipo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome_tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('img_normal', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('img_feliz', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('img_triste', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('img_entediado', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('guidu', ['GuiduTipo'])

        # Adding model 'Guidu'
        db.create_table('guidu_guidu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['guidu.GuiduTipo'])),
            ('jogador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='guidus', null=True, to=orm['jogador.Jogador'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fome', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
            ('higiene', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=5)),
            ('diversao', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=6)),
            ('banheiro', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
            ('social', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=5)),
            ('energia', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=6)),
            ('fome_update', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('higiene_update', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('diversao_update', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('banheiro_update', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('social_update', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('energia_update', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_nascimento', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('humor', self.gf('django.db.models.fields.CharField')(default='normal', max_length=50)),
        ))
        db.send_create_signal('guidu', ['Guidu'])


    def backwards(self, orm):
        # Deleting model 'GuiduTipo'
        db.delete_table('guidu_guidutipo')

        # Deleting model 'Guidu'
        db.delete_table('guidu_guidu')


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
        'guidu.guidu': {
            'Meta': {'object_name': 'Guidu'},
            'banheiro': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'banheiro_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'diversao': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '6'}),
            'diversao_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'energia': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '6'}),
            'energia_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fome': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'fome_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'higiene': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
            'higiene_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'humor': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '50'}),
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
            'img_entediado': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img_feliz': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img_normal': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img_triste': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nome_tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'jogador.jogador': {
            'Meta': {'object_name': 'Jogador'},
            'guicoin': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'guimoves': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_guimoves': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['guidu']