import unittest
from math_ops import is_even, safe_divide

class TestMathOps(unittest.TestCase):
    
    # Тест 1: Проверка на чётность (чётное число)
    def test_is_even_true(self):
        self.assertTrue(is_even(4))
        
    # Тест 2: Проверка на чётность (нечётное число)
    def test_is_even_false(self):
        self.assertFalse(is_even(5))
        
    # Тест 3: Нормальное деление
    def test_safe_divide_normal(self):
        self.assertEqual(safe_divide(10, 2), 5.0)
        
    # Тест 4: Деление на ноль (ожидаем ошибку)
    def test_safe_divide_by_zero(self):
        with self.assertRaises(ValueError):
            safe_divide(10, 0)

if __name__ == '__main__':
    unittest.main()