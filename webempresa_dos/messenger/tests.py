from django.test import TestCase
from django.contrib.auth.models import User
from messenger.models import Thread, Message

# Create your tests here.

class ThreadTestCase(TestCase):
    '''clase con métodos para preparar y probar la prueba unitaria'''
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')
        
        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()), 2)
        # python manage.py test messenger.tests.ThreadTestCase.test_add_users_to_thread
    
    def test_filter_thread_by_useres(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread, threads[0]) # prtimera psoscion del queriset

    def test_filter_noo_existen_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(threads), 0)
    
    def test_add_messages_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        messaje1 = Message.objects.create(user=self.user1, content='Muy buenas')
        messaje2 = Message.objects.create(user=self.user2, content='Hola')
        self.thread.messages.add(messaje1, messaje2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        for messaje in self.thread.messages.all():
            print(f'({messaje.user}) dice, {messaje.content}')
