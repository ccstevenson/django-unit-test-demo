# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'app_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'app', ['Game'])

        # Adding model 'Scenario'
        db.create_table(u'app_scenario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Game'])),
        ))
        db.send_create_signal(u'app', ['Scenario'])

        # Adding model 'Encounter'
        db.create_table(u'app_encounter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Scenario'])),
        ))
        db.send_create_signal(u'app', ['Encounter'])

        # Adding model 'Player'
        db.create_table(u'app_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'app', ['Player'])

        # Adding model 'WildRat'
        db.create_table(u'app_wildrat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('health', self.gf('django.db.models.fields.IntegerField')()),
            ('encounter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Encounter'])),
        ))
        db.send_create_signal(u'app', ['WildRat'])

        # Adding model 'RatKing'
        db.create_table(u'app_ratking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('health', self.gf('django.db.models.fields.IntegerField')()),
            ('encounter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Encounter'])),
        ))
        db.send_create_signal(u'app', ['RatKing'])

        # Adding model 'Warrior'
        db.create_table(u'app_warrior', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('health', self.gf('django.db.models.fields.IntegerField')()),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Game'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Player'])),
        ))
        db.send_create_signal(u'app', ['Warrior'])

        # Adding model 'Mage'
        db.create_table(u'app_mage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('health', self.gf('django.db.models.fields.IntegerField')()),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Game'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Player'])),
        ))
        db.send_create_signal(u'app', ['Mage'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'app_game')

        # Deleting model 'Scenario'
        db.delete_table(u'app_scenario')

        # Deleting model 'Encounter'
        db.delete_table(u'app_encounter')

        # Deleting model 'Player'
        db.delete_table(u'app_player')

        # Deleting model 'WildRat'
        db.delete_table(u'app_wildrat')

        # Deleting model 'RatKing'
        db.delete_table(u'app_ratking')

        # Deleting model 'Warrior'
        db.delete_table(u'app_warrior')

        # Deleting model 'Mage'
        db.delete_table(u'app_mage')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Player']"})
        },
        u'app.wildrat': {
            'Meta': {'object_name': 'WildRat'},
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Encounter']"}),
            'health': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']