#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os
import json
import csv
from pathlib import Path
from data_handler import DataHandler


class TestDataHandler(unittest.TestCase):
    """DataHandler sınıfı için test kodu"""
    
    def setUp(self):
        """Her testten önce test dizini oluştur"""
        self.test_dir = "test_files"
        Path(self.test_dir).mkdir(exist_ok=True)
    
    def tearDown(self):
        """Her testten sonra test dosyalarını sil"""
        import shutil
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_write_and_read_text_file(self):
        """Metin dosyası yazma ve okuma test"""
        filepath = os.path.join(self.test_dir, "test.txt")
        content = "Merhaba Dünya!"
        
        # Yaz
        result = DataHandler.write_text_file(filepath, content)
        self.assertIn("✓", result)
        
        # Oku
        read_content = DataHandler.read_text_file(filepath)
        self.assertEqual(read_content, content)
    
    def test_read_nonexistent_file(self):
        """Olmayan dosya okuma test"""
        filepath = os.path.join(self.test_dir, "nonexistent.txt")
        result = DataHandler.read_text_file(filepath)
        self.assertIn("Hata", result)
    
    def test_write_and_read_json_file(self):
        """JSON dosyası yazma ve okuma test"""
        filepath = os.path.join(self.test_dir, "test.json")
        data = {"ad": "Ahmet", "yaş": 25, "şehir": "İstanbul"}
        
        # Yaz
        result = DataHandler.write_json_file(filepath, data)
        self.assertIn("✓", result)
        
        # Oku
        read_data = DataHandler.read_json_file(filepath)
        self.assertEqual(read_data, data)
    
    def test_read_invalid_json(self):
        """Geçersiz JSON okuma test"""
        filepath = os.path.join(self.test_dir, "invalid.json")
        
        # Geçersiz JSON dosyası oluştur
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("{invalid json}")
        
        result = DataHandler.read_json_file(filepath)
        self.assertIn("Hata", result)
    
    def test_write_and_read_csv_file(self):
        """CSV dosyası yazma ve okuma test"""
        filepath = os.path.join(self.test_dir, "test.csv")
        data = [
            {"ad": "Ahmet", "yaş": 25},
            {"ad": "Fatma", "yaş": 30},
            {"ad": "Mehmet", "yaş": 28}
        ]
        
        # Yaz
        result = DataHandler.write_csv_file(filepath, data)
        self.assertIn("✓", result)
        
        # Oku
        read_result = DataHandler.read_csv_file(filepath)
        self.assertEqual(read_result["status"], "success")
        self.assertEqual(len(read_result["data"]), 3)
    
    def test_list_files(self):
        """Klasör dosya listeleme test"""
        # Test dosyaları oluştur
        Path(os.path.join(self.test_dir, "file1.txt")).touch()
        Path(os.path.join(self.test_dir, "file2.txt")).touch()
        
        files = DataHandler.list_files(self.test_dir)
        self.assertIsInstance(files, list)
        self.assertGreaterEqual(len(files), 2)
    
    def test_list_files_nonexistent_directory(self):
        """Olmayan klasör listeleme test"""
        result = DataHandler.list_files("nonexistent_dir")
        # Boş liste dönebilir veya hata mesajı
        self.assertTrue(isinstance(result, (list, str)))
    
    def test_file_size(self):
        """Dosya boyutu test"""
        filepath = os.path.join(self.test_dir, "test.txt")
        DataHandler.write_text_file(filepath, "Merhaba")
        
        size = DataHandler.file_size(filepath)
        self.assertIsInstance(size, str)
        self.assertIn("B", size)  # Bytes, KB, MB içermelidir
    
    def test_file_size_nonexistent(self):
        """Olmayan dosya boyutu test"""
        result = DataHandler.file_size("nonexistent.txt")
        self.assertIn("Hata", result)
    
    def test_write_csv_without_fieldnames(self):
        """CSV yazma (fieldnames otomatik)"""
        filepath = os.path.join(self.test_dir, "test2.csv")
        data = [
            {"isim": "Ahmet", "soyad": "Yılmaz"},
            {"isim": "Fatma", "soyad": "Demir"}
        ]
        
        result = DataHandler.write_csv_file(filepath, data)
        self.assertIn("✓", result)
        
        # Dosya var mı kontrol et
        self.assertTrue(os.path.exists(filepath))
    
    def test_write_empty_csv(self):
        """Boş CSV yazma test"""
        filepath = os.path.join(self.test_dir, "empty.csv")
        result = DataHandler.write_csv_file(filepath, [])
        self.assertIn("Hata", result)


if __name__ == '__main__':
    unittest.main()
