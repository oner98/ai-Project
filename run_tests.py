#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys

def run_all_tests():
    """Tüm testleri çalıştır"""
    # Test bulucuyu oluştur
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Test modüllerini ekle
    suite.addTests(loader.discover('.', pattern='test_*.py'))
    
    # Test çalıştırıcı oluştur ve çalıştır
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Çıkış kodunu ayarla
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_all_tests())
