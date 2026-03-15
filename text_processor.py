import re
from collections import Counter


class TextProcessor:
    """Metin işleme ve analiz sınıfı"""
    
    @staticmethod
    def clean_text(text):
        """Metini temizle (özel karakterler, fazla boşluklar vb.)"""
        # Fazla boşlukları kaldır
        text = re.sub(r'\s+', ' ', text)
        # Başındaki ve sonundaki boşlukları kaldır
        text = text.strip()
        return text
    
    @staticmethod
    def tokenize(text):
        """Metni kelime ve cümlelere böl"""
        # Cümleleri ayır
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        # Kelimeleri ayır
        tokens = re.findall(r'\b\w+\b', text.lower())
        return {
            "sentences": sentences,
            "words": tokens
        }
    
    @staticmethod
    def get_word_frequency(text, top_n=10):
        """En sık kullanılan kelimeleri bul"""
        words = re.findall(r'\b\w+\b', text.lower())
        # Kısa kelimeler filtrele
        words = [w for w in words if len(w) > 2 and w.isalpha()]
        freq = Counter(words)
        return dict(freq.most_common(top_n))
    
    @staticmethod
    def remove_stopwords(text):
        """Turkish stop words kaldır (basit)"""
        turkish_stopwords = {
            've', 'veya', 'ya', 'ama', 'ancak', 'fakat', 'gibi', 'kadar',
            'göre', 'şekilde', 'ise', 'için', 'de', 'da', 'mi', 'mı', 'mu', 'mü',
            'ne', 'nedir', 'bu', 'şu', 'o', 'ben', 'sen', 'biz', 'siz'
        }
        
        words = re.findall(r'\b\w+\b', text.lower())
        filtered = [w for w in words if w.isalpha() and w not in turkish_stopwords]
        return ' '.join(filtered)
    
    @staticmethod
    def get_text_stats(text):
        """Metin istatistikleri hesapla"""
        cleaned = TextProcessor.clean_text(text)
        tokens = re.findall(r'\b\w+\b', cleaned)
        sentences = re.split(r'[.!?]+', cleaned)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        return {
            "character_count": len(cleaned),
            "word_count": len(tokens),
            "sentence_count": len(sentences),
            "avg_word_length": sum(len(w) for w in tokens) / len(tokens) if tokens else 0,
            "avg_sentence_length": len(tokens) / len(sentences) if sentences else 0
        }
    
    @staticmethod
    def translate_simple(text, target_lang='en'):
        """Basit çeviri (yapay zeka kütüphanesi olmadan)"""
        # Not: Bu basit bir örnek, gerçek çeviri için Google Translate API vb. kullanılmalı
        simple_dict = {
            'merhaba': 'hello',
            'dünya': 'world',
            'iyiyim': 'i am fine',
            'teşekkür': 'thank you'
        }
        return f"Çeviri için daha güçlü bir tool gerekli. Şu anda '{text}' çevrilemedi."
