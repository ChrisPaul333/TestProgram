import unittest
import name_function as nf

class NmaesTestCase(unittest.TestCase):
    """测试 name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
        formatted_name = nf.get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """能够正确处理像 Wolfgang Amadeus Mozart这样的姓名吗？ """
        formatted_name = nf.get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()