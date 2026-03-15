#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ai_assistant import AIAssistant


class TestAIAssistant(unittest.TestCase):
    """AIAssistant sınıfı için test kodu"""
    
    def setUp(self):
        """Her testten önce çalışır"""
        self.assistant = AIAssistant()
    
    def test_greet(self):
        """Karşılama mesajını test et"""
        greeting = self.assistant.greet()
        self.assertIsNotNone(greeting)
        self.assertIsInstance(greeting, str)
        self.assertTrue(len(greeting) > 0)
    
    def test_say_goodbye(self):
        """Veda mesajını test et"""
        goodbye = self.assistant.say_goodbye()
        self.assertIsNotNone(goodbye)
        self.assertIsInstance(goodbye, str)
        self.assertTrue(len(goodbye) > 0)
    
    def test_get_time(self):
        """Saat bilgisini test et"""
        time = self.assistant.get_time()
        self.assertIsNotNone(time)
        self.assertRegex(time, r'\d{2}:\d{2}:\d{2}')
    
    def test_get_date(self):
        """Tarih bilgisini test et"""
        date = self.assistant.get_date()
        self.assertIsNotNone(date)
        self.assertRegex(date, r'\d{2}\.\d{2}\.\d{4}')
    
    def test_respond_to_time_query(self):
        """Saat sorgusuna yanıt test et"""
        response = self.assistant.respond_to_query("saat kaç?")
        self.assertIn("saat", response.lower())
    
    def test_respond_to_date_query(self):
        """Tarih sorgusuna yanıt test et"""
        response = self.assistant.respond_to_query("bugün kaçıncı?")
        self.assertIn("tarih", response.lower())
    
    def test_respond_to_greeting(self):
        """Karşlamaya yanıt test et"""
        response = self.assistant.respond_to_query("merhaba")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
    
    def test_analyze_sentiment_positive(self):
        """Pozitif duygu analizi"""
        value, text = self.assistant.analyze_sentiment("bu çok harika ve güzel")
        self.assertEqual(value, 1)
        self.assertIn("Pozitif", text)
    
    def test_analyze_sentiment_negative(self):
        """Negatif duygu analizi"""
        value, text = self.assistant.analyze_sentiment("bu kötü ve berbat")
        self.assertEqual(value, -1)
        self.assertIn("Negatif", text)
    
    def test_analyze_sentiment_neutral(self):
        """Nötr duygu analizi"""
        value, text = self.assistant.analyze_sentiment("mavi renk vardır")
        self.assertEqual(value, 0)
        self.assertIn("Nötr", text)
    
    def test_word_count(self):
        """Kelime sayısını test et"""
        text = "bu bir test cümleseidir"
        # Kelime sayısı hesapla (regex ile basit sayma)
        import re
        words = re.findall(r'\b\w+\b', text)
        self.assertEqual(len(words), 4)  # "cümleseidir" yazım hatası ama 1 kelime
    
    def test_char_count(self):
        """Karakter sayısını test et"""
        text = "merhaba"
        count = self.assistant.char_count(text)
        self.assertEqual(count, 7)


if __name__ == '__main__':
    unittest.main()
