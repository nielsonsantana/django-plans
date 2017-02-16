# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Plan'
        db.create_table('plans_plan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('customized', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('plans', ['Plan'])

        # Adding model 'BillingInfo'
        db.create_table('plans_billinginfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('tax_number', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=200, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('shipping_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('shipping_street', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('shipping_zipcode', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('shipping_city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('plans', ['BillingInfo'])

        # Adding model 'UserPlan'
        db.create_table('plans_userplan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plans.Plan'])),
            ('expire', self.gf('django.db.models.fields.DateField')(default=None, null=True, db_index=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
        ))
        db.send_create_signal('plans', ['UserPlan'])

        # Adding model 'Pricing'
        db.create_table('plans_pricing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('period', self.gf('django.db.models.fields.PositiveIntegerField')(default=30, null=True, db_index=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('plans', ['Pricing'])

        # Adding model 'Quota'
        db.create_table('plans_quota', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('codename', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_boolean', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('plans', ['Quota'])

        # Adding model 'PlanPricing'
        db.create_table('plans_planpricing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plans.Plan'])),
            ('pricing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plans.Pricing'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2, db_index=True)),
        ))
        db.send_create_signal('plans', ['PlanPricing'])

        # Adding model 'PlanQuota'
        db.create_table('plans_planquota', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plans.Plan'])),
            ('quota', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plans.Quota'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, blank=True)),
        ))
        db.send_create_signal('plans', ['PlanQuota'])

        # Adding model 'Order'
        db.create_table('plans_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('flat_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plan_order', to=orm['plans.Plan'])),
            ('pricing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plans.Pricing'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('completed', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2, db_index=True)),
            ('tax', self.gf('django.db.models.fields.DecimalField')(db_index=True, null=True, max_digits=4, decimal_places=2, blank=True)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='EUR', max_length=3)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('order_id', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('plans', ['Order'])

        # Adding model 'Invoice'
        db.create_table('plans_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plans.Order'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('full_number', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=1, db_index=True)),
            ('issued', self.gf('django.db.models.fields.DateField')(db_index=True)),
            ('issued_duplicate', self.gf('django.db.models.fields.DateField')(db_index=True, null=True, blank=True)),
            ('selling_date', self.gf('django.db.models.fields.DateField')(db_index=True, null=True, blank=True)),
            ('payment_date', self.gf('django.db.models.fields.DateField')(db_index=True)),
            ('unit_price_net', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('total_net', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('tax_total', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('tax', self.gf('django.db.models.fields.DecimalField')(db_index=True, null=True, max_digits=4, decimal_places=2, blank=True)),
            ('rebate', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=4, decimal_places=2)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='EUR', max_length=3)),
            ('item_description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('buyer_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('buyer_street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('buyer_zipcode', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('buyer_city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('buyer_country', self.gf('django_countries.fields.CountryField')(default='PL', max_length=2)),
            ('buyer_tax_number', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('shipping_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shipping_street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shipping_zipcode', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shipping_city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shipping_country', self.gf('django_countries.fields.CountryField')(default='PL', max_length=2)),
            ('require_shipment', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('issuer_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('issuer_street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('issuer_zipcode', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('issuer_city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('issuer_country', self.gf('django_countries.fields.CountryField')(default='PL', max_length=2)),
            ('issuer_tax_number', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('plans', ['Invoice'])


    def backwards(self, orm):
        # Deleting model 'Plan'
        db.delete_table('plans_plan')

        # Deleting model 'BillingInfo'
        db.delete_table('plans_billinginfo')

        # Deleting model 'UserPlan'
        db.delete_table('plans_userplan')

        # Deleting model 'Pricing'
        db.delete_table('plans_pricing')

        # Deleting model 'Quota'
        db.delete_table('plans_quota')

        # Deleting model 'PlanPricing'
        db.delete_table('plans_planpricing')

        # Deleting model 'PlanQuota'
        db.delete_table('plans_planquota')

        # Deleting model 'Order'
        db.delete_table('plans_order')

        # Deleting model 'Invoice'
        db.delete_table('plans_invoice')


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
        'plans.billinginfo': {
            'Meta': {'object_name': 'BillingInfo'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'shipping_city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'shipping_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tax_number': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'plans.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'buyer_city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'buyer_country': ('django_countries.fields.CountryField', [], {'default': "'PL'", 'max_length': '2'}),
            'buyer_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'buyer_street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'buyer_tax_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'buyer_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'EUR'", 'max_length': '3'}),
            'full_number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issued': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'issued_duplicate': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'issuer_city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'issuer_country': ('django_countries.fields.CountryField', [], {'default': "'PL'", 'max_length': '2'}),
            'issuer_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'issuer_street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'issuer_tax_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'issuer_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'item_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plans.Order']"}),
            'payment_date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'rebate': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '4', 'decimal_places': '2'}),
            'require_shipment': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'selling_date': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'shipping_city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shipping_country': ('django_countries.fields.CountryField', [], {'default': "'PL'", 'max_length': '2'}),
            'shipping_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shipping_street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shipping_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'db_index': 'True', 'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'tax_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'total_net': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1', 'db_index': 'True'}),
            'unit_price_net': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'plans.order': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Order'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2', 'db_index': 'True'}),
            'completed': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'EUR'", 'max_length': '3'}),
            'flat_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plan_order'", 'to': "orm['plans.Plan']"}),
            'pricing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plans.Pricing']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'db_index': 'True', 'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'plans.plan': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Plan'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'customized': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'quotas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['plans.Quota']", 'through': "orm['plans.PlanQuota']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'plans.planpricing': {
            'Meta': {'ordering': "('pricing__period',)", 'object_name': 'PlanPricing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plans.Plan']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2', 'db_index': 'True'}),
            'pricing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plans.Pricing']"})
        },
        'plans.planquota': {
            'Meta': {'object_name': 'PlanQuota'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plans.Plan']"}),
            'quota': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plans.Quota']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'})
        },
        'plans.pricing': {
            'Meta': {'ordering': "('period',)", 'object_name': 'Pricing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'period': ('django.db.models.fields.PositiveIntegerField', [], {'default': '30', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'plans.quota': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Quota'},
            'codename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_boolean': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'plans.userplan': {
            'Meta': {'object_name': 'UserPlan'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'expire': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plans.Plan']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['plans']