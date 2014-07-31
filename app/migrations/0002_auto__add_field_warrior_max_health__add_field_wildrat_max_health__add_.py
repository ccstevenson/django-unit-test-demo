# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Warrior.max_health'
        db.add_column(u'app_warrior', 'max_health',
                      self.gf('django.db.models.fields.IntegerField')(default=30),
                      keep_default=False)

        # Adding field 'WildRat.max_health'
        db.add_column(u'app_wildrat', 'max_health',
                      self.gf('django.db.models.fields.IntegerField')(default=30),
                      keep_default=False)

        # Adding field 'Mage.max_health'
        db.add_column(u'app_mage', 'max_health',
                      self.gf('django.db.models.fields.IntegerField')(default=30),
                      keep_default=False)

        # Adding field 'RatKing.max_health'
        db.add_column(u'app_ratking', 'max_health',
                      self.gf('django.db.models.fields.IntegerField')(default=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Warrior.max_health'
        db.delete_column(u'app_warrior', 'max_health')

        # Deleting field 'WildRat.max_health'
        db.delete_column(u'app_wildrat', 'max_health')

        # Deleting field 'Mage.max_health'
        db.delete_column(u'app_mage', 'max_health')

        # Deleting field 'RatKing.max_health'
        db.delete_column(u'app_ratking', 'max_health')


    models = {
        u'app.encounter': {
            'Meta': {'object_name': 'Encounter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Scenario']"})
        },
        u'app.game': {
            'Meta': {'object_name': 'Game'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.mage': {
            'Meta': {'object_name': 'Mage'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Game']"}),
            'health': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_health': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Player']"})
        },
        u'app.player': {
            'Meta': {'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'app.ratking': {
            'Meta': {'object_name': 'RatKing'},
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Encounter']"}),
            'health': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_health': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.warrior': {
            'Meta': {'object_name': 'Warrior'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Game']"}),
            'health': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_health': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Player']"})
        },
        u'app.wildrat': {
            'Meta': {'object_name': 'WildRat'},
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Encounter']"}),
            'health': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_health': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['app']