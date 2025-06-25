# tests/test_basic.py
import unittest
from django.test import TestCase

# Импортируем нашу модель, если она есть, или функцию из myapp/views.py
# Например, если у нас есть какая-то функция в views.py
# from myapp.views import some_simple_function # Если у тебя есть такая функция

class BasicFunctionalityTest(TestCase):
    def test_true_is_true(self):
        """
        Простой тест, который всегда проходит.
        Это чтобы мы увидели, что наши тесты вообще запускаются.
        """
        self.assertTrue(True)

    def test_sum_function(self):
        """
        Представим, что у нас есть функция, которая складывает два числа.
        Мы могли бы ее написать в myapp/views.py или где-то еще.
        """
        a = 5
        b = 3
        expected_sum = 8
        # Предположим, у нас есть функция add(a, b)
        # actual_sum = add(a, b)
        actual_sum = a + b # Пока просто складываем напрямую
        self.assertEqual(actual_sum, expected_sum)

    # Можешь добавить еще тестов для твоего приложения `myapp`,
    # например, на проверку URL-адресов, если ты их уже настроил.
    # from django.urls import reverse
    #
    # def test_homepage_url(self):
    #     response = self.client.get(reverse('home')) # Если у тебя есть URL-адрес 'home'
    #     self.assertEqual(response.status_code, 200)