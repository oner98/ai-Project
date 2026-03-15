import random
from datetime import datetime
import re


class AIAssistant:
    def __init__(self):
        self.name = "AI Asistanı"
        self.greeting_responses = [
            "Merhaba! Sana nasıl yardımcı olabilirim?",
            "Selam! Ne yapmak istiyorsun?",
            "Hoş geldin! Bana ne sorabilirim?",
        ]
        
        self.farewell_responses = [
            "Hoşça kalın! İyi günler!",
            "Görüşmek üzere!",
            "Allah sana selam versin!",
        ]

    def greet(self):
        """Karşılama mesajı gönder"""
        return random.choice(self.greeting_responses)

    def say_goodbye(self):
        """Veda mesajı gönder"""
        return random.choice(self.farewell_responses)

    def get_time(self):
        """Şu anki saati döndür"""
        return datetime.now().strftime("%H:%M:%S")

    def get_date(self):
        """Şu anki tarihi döndür"""
        return datetime.now().strftime("%d.%m.%Y")

    def respond_to_query(self, query):
        """Kullanıcı sorgusuna yanıt ver"""
        query_lower = query.lower().strip()
        
        # Saat sorgusu
        if any(word in query_lower for word in ["saat", "zaman", "kaçta"]):
            return f"Şu anki saat: {self.get_time()}"
        
        # Tarih sorgusu
        elif any(word in query_lower for word in ["tarih", "bugün", "date"]):
            return f"Bugünün tarihi: {self.get_date()}"
        
        # Karşılama
        elif any(word in query_lower for word in ["merhaba", "selam", "hello", "hi"]):
            return self.greet()
        
        # Hoşçakal
        elif any(word in query_lower for word in ["hoşça", "bye", "quit", "exit", "çıkış"]):
            return self.say_goodbye()
        
        # Genel yanıt
        else:
            return f"'{query}' hakkında daha fazla bilgiye ihtiyacım var. Lütfen daha spesifik olabilir misin?"

    def analyze_sentiment(self, text):
        """
        Metin duygusunu analiz et (basit)
        1: Pozitif, 0: Nötr, -1: Negatif
        """
        positive_words = ["harika", "güzel", "iyi", "seviyorum", "mükemmel", "süper"]
        negative_words = ["kötü", "üzücü", "nefret", "berbat", "hoşuma gitmiyor"]
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return 1, "Pozitif 😊"
        elif negative_count > positive_count:
            return -1, "Negatif 😞"
        else:
            return 0, "Nötr 😐"

    def word_count(self, text):
        """Metindeki kelime sayısını hesapla"""
        words = nltk.word_tokenize(text)
        return len(words)

    def char_count(self, text):
        """Metindeki karakter sayısını hesapla"""
        return len(text)
