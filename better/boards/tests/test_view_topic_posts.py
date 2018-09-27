from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from ..models import Board, Topic, post
from ..views import topic_posts

class TopicPostsTests(TestCase):
	def setUp(self):
		board = Board.objects.create(name='Django', description='Django Board')
		user = User.objects.create(username='kuldip', email='kk@gmail.com', password="abcdef12345")
		topic = Topic.objects.create(subject='Django forms', board=board, starter=user)
		post.objects.create(message="hey this is", topic=topic, created_by=user)
		url = reverse('topic_posts', kwargs={'pk': board.pk, 'topic_pk':topic.pk})
		self.response = self.client.get(url)

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_view_function(self):
		view = resolve('/boards/1/topics/1/')
		self.assertEquals(view.func, topic_posts)