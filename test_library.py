import sys
import os

# Добавляем путь к вашей библиотеке
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from actions_demo.library import *  # замените на ваши функции

def test_example():
    """Простой тест для проверки"""
    assert 1 + 1 == 2

# Добавьте здесь тесты для вашей библиотеки
