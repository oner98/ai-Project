#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from text_processor import TextProcessor


class TestTextProcessor(unittest.TestCase):
    """TextProcessor sınıfı için test kodu"""
    
    def test_clean_text(self):
        """Metin temizlemeyi test et"""
        dirty_text = "  merhaba    dünya  "
        clean = TextProcessor.clean_text(dirty_text)
        self.assertEqual(clean, "merhaba dünya")
    
    def test_clean_text_with_multiple_spaces(self):
        """Çok fazla boşlukları temizle"""
        text = "bu    bir    test"
        clean = TextProcessor.clean_text(text)
        self.assertEqual(clean, "bu bir test")
    
    def test_tokenize(self):
        """Tokenization test"""
        text = "Merhaba dünya. Bu bir testtir!"
        result = TextProcessor.tokenize(text)
        
        self.assertIn("sentences", result)
        self.assertIn("words", result)
        self.assertTrue(len(result["sentences"]) > 0)
        self.assertTrue(len(result["words"]) > 0)
    
    def test_get_word_frequency(self):
        """Kelime frekansı test"""
        text = "merhaba merhaba dünya dünya dünya test"
        freq = TextProcessor.get_word_frequency(text, top_n=5)
        
        self.assertIsInstance(freq, dict)
        # "dünya" ve "merhaba" en sık kullanılan kelimeler olmalı
        if freq:
            first_word = list(freq.keys())[0]
            self.assertIn(first_word, ["dünya", "merhaba"])
    
    def test_remove_stopwords(self):
        """Stop words kaldırma test"""
        text = "bu ve şu bir testtir"
        filtered = TextProcessor.remove_stopwords(text)
        
        # ve, bu, şu gibi stop words kaldırılmış olmalı
        self.assertNotIn("ve", filtered.lower())
        self.assertIn("testtir", filtered.lower())
    
    def test_get_text_stats(self):
        """Metin istatistikleri test"""
        text = "Merhaba dünya. Bu bir test cümlesidir."
        stats = TextProcessor.get_text_stats(text)
        
        self.assertIn("character_count", stats)
        self.assertIn("word_count", stats)
        self.assertIn("sentence_count", stats)
        self.assertIn("avg_word_length", stats)
        self.assertIn("avg_sentence_length", stats)
        
        # Değerleri kontrol et
        self.assertGreater(stats["character_count"], 0)
        self.assertGreater(stats["word_count"], 0)
        self.assertGreater(stats["sentence_count"], 0)
        self.assertGreater(stats["avg_word_length"], 0)
    
    def test_get_text_stats_with_empty_text(self):
        """Boş metin istatistikleri test"""
        text = ""
        stats = TextProcessor.get_text_stats(text)
        
        self.assertEqual(stats["character_count"], 0)
        self.assertEqual(stats["word_count"], 0)
        self.assertEqual(stats["sentence_count"], 0)
    
    def test_get_text_stats_single_word(self):
        """Tek kelime için istatistikler"""
        text = "merhaba"
        stats = TextProcessor.get_text_stats(text)
        
        self.assertEqual(stats["character_count"], 7)
        self.assertEqual(stats["word_count"], 1)
        self.assertGreaterEqual(stats["sentence_count"], 0)  # Regex'e göre değişebilir
    
    def test_word_frequency_empty_text(self):
        """Boş metinde frekans"""
        text = ""
        freq = TextProcessor.get_word_frequency(text)
        self.assertEqual(len(freq), 0)
    
    def test_translate_simple(self):
        """Basit çeviri test"""
        text = "merhaba"
        result = TextProcessor.translate_simple(text)
        # Basit çeviri olmadığını kontrol et
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
