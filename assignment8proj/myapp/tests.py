from django.test import TestCase
from django.apps import apps
from django.urls import URLPattern, URLResolver, get_resolver


class ModelTests(TestCase):
	def test_app_models_have_primary_keys(self):
		models = list(apps.get_app_config("myapp").get_models())
		self.assertTrue(models, "Expected at least one model in myapp")

		for model in models:
			with self.subTest(model=model.__name__):
				self.assertIsNotNone(model._meta.pk)


class ViewTests(TestCase):
	def test_registered_app_views_are_callable(self):
		def iter_patterns(patterns):
			for pattern in patterns:
				if isinstance(pattern, URLPattern):
					yield pattern
				elif isinstance(pattern, URLResolver):
					yield from iter_patterns(pattern.url_patterns)

		views = [
			pattern.callback
			for pattern in iter_patterns(get_resolver().url_patterns)
			if getattr(pattern.callback, "__module__", "").startswith("myapp.views")
		]
		self.assertTrue(views, "Expected at least one URL-backed view in myapp")

		for view in views:
			with self.subTest(view=view):
				self.assertTrue(callable(view))