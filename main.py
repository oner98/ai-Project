#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ai_assistant import AIAssistant
from text_processor import TextProcessor
from data_handler import DataHandler


def show_menu():
    """Menüyü göster"""
    print("\n" + "="*50)
    print("🤖 YAPay ZEKa YARDIMCISI")
    print("="*50)
    print("\n1. Chatbot")
    print("2. Metin Analizi")
    print("3. Metin İstatistikleri")
    print("4. Veri İşleme (Dosya Okuma/Yazma)")
    print("5. Dosya Yönetimi")
    print("6. Kelime Frekansı Analizi")
    print("7. Duygu Analizi")
    print("0. Çıkış")
    print("="*50)


def chatbot_menu(assistant):
    """Chatbot menüsü"""
    print(f"\n{assistant.greet()}")
    print("(Çıkmak için 'çıkış' veya 'quit' yazın)\n")
    
    while True:
        user_input = input("Sen: ").strip()
        if not user_input:
            continue
        
        if any(word in user_input.lower() for word in ["çıkış", "quit", "exit"]):
            print(f"AI: {assistant.say_goodbye()}")
            break
        
        response = assistant.respond_to_query(user_input)
        print(f"AI: {response}")


def text_analysis_menu():
    """Metin analizi menüsü"""
    text = input("\nMetni giriniz:\n> ")
    
    print("\n" + "="*50)
    print("METIN ANALİZİ SONUÇLARI")
    print("="*50)
    
    sentiment_value, sentiment_text = AIAssistant().analyze_sentiment(text)
    stats = TextProcessor.get_text_stats(text)
    
    print(f"📊 İstatistikler:")
    print(f"   • Karakter Sayısı: {stats['character_count']}")
    print(f"   • Kelime Sayısı: {stats['word_count']}")
    print(f"   • Cümle Sayısı: {stats['sentence_count']}")
    print(f"   • Ortalama Kelime Uzunluğu: {stats['avg_word_length']:.2f}")
    print(f"   • Ortalama Cümle Uzunluğu: {stats['avg_sentence_length']:.2f}")
    print(f"\n😊 Duygu: {sentiment_text}")


def text_statistics_menu():
    """Metin istatistikleri menüsü"""
    text = input("\nMetni giriniz:\n> ")
    stats = TextProcessor.get_text_stats(text)
    
    print("\n" + "="*50)
    print("DETAYLI İSTATİSTİKLER")
    print("="*50)
    print(f"Karakter Sayısı: {stats['character_count']}")
    print(f"Kelime Sayısı: {stats['word_count']}")
    print(f"Cümle Sayısı: {stats['sentence_count']}")
    print(f"Ort. Kelime Uzunluğu: {stats['avg_word_length']:.2f}")
    print(f"Ort. Cümle Uzunluğu: {stats['avg_sentence_length']:.2f}")


def data_processing_menu():
    """Veri işleme menüsü"""
    print("\n1. Metin Dosyası Oku")
    print("2. Metin Dosyası Yaz")
    print("3. JSON Dosyası Oku")
    print("4. JSON Dosyası Yaz")
    print("5. CSV Dosyası Oku")
    print("6. Geri Dön")
    
    choice = input("\nSeçim: ").strip()
    
    if choice == "1":
        filepath = input("Dosya yolu: ")
        content = DataHandler.read_text_file(filepath)
        print(f"\n{content}")
    
    elif choice == "2":
        filepath = input("Dosya yolu: ")
        content = input("İçerik:\n> ")
        result = DataHandler.write_text_file(filepath, content)
        print(result)
    
    elif choice == "3":
        filepath = input("Dosya yolu: ")
        data = DataHandler.read_json_file(filepath)
        print(data)
    
    elif choice == "4":
        filepath = input("Dosya yolu: ")
        print("JSON veri giriniz (örn: {\"ad\": \"John\", \"yaş\": 30}): ")
        try:
            data = eval(input("> "))
            result = DataHandler.write_json_file(filepath, data)
            print(result)
        except:
            print("Hata: Geçersiz JSON formatı")
    
    elif choice == "5":
        filepath = input("Dosya yolu: ")
        result = DataHandler.read_csv_file(filepath)
        if result.get("status") == "success":
            print(f"\n{len(result['data'])} satır bulundu:")
            for row in result['data'][:5]:
                print(row)
            if len(result['data']) > 5:
                print(f"... ve {len(result['data']) - 5} satır daha")
        else:
            print(f"Hata: {result.get('message')}")


def file_management_menu():
    """Dosya yönetimi menüsü"""
    print("\n1. Klasördeki Dosyaları Listele")
    print("2. Dosya Boyutunu Öğren")
    print("3. Geri Dön")
    
    choice = input("\nSeçim: ").strip()
    
    if choice == "1":
        directory = input("Klasör yolu: ")
        files = DataHandler.list_files(directory)
        print(f"\nBulunan dosyalar ({len(files)}):")
        for f in files:
            print(f"  • {f}")
    
    elif choice == "2":
        filepath = input("Dosya yolu: ")
        size = DataHandler.file_size(filepath)
        print(f"Dosya boyutu: {size}")


def word_frequency_menu():
    """Kelime frekansı menüsü"""
    text = input("\nMetni giriniz:\n> ")
    top_n = input("Kaç kelime gösterilsin? (varsayılan: 10): ").strip()
    top_n = int(top_n) if top_n.isdigit() else 10
    
    freq = TextProcessor.get_word_frequency(text, top_n)
    
    print("\n" + "="*50)
    print("EN SIK KULLANILAN KELİMELER")
    print("="*50)
    for i, (word, count) in enumerate(freq.items(), 1):
        print(f"{i}. {word}: {count}")


def sentiment_analysis_menu():
    """Duygu analizi menüsü"""
    text = input("\nMetni giriniz:\n> ")
    assistant = AIAssistant()
    
    sentiment_value, sentiment_text = assistant.analyze_sentiment(text)
    
    print("\n" + "="*50)
    print("DUYGU ANALİZİ SONUCU")
    print("="*50)
    print(f"Sonuç: {sentiment_text}")
    print(f"Değer: {sentiment_value}")
    
    if sentiment_value > 0:
        print("📈 Metin pozitif duygular içeriyor.")
    elif sentiment_value < 0:
        print("📉 Metin negatif duygular içeriyor.")
    else:
        print("➡️ Metin nötr bir tonla yazılmış.")


def main():
    """Ana program"""
    print("\n🤖 YAPay ZEKa YARDIMCISINA HOŞGELDINIZ!")
    print("Lütfen bir işlem seçiniz.\n")
    
    while True:
        show_menu()
        choice = input("\nSeçim (0-7): ").strip()
        
        if choice == "0":
            print("\nYazılımdan çıkılıyor... Hoşça kalın! 👋")
            break
        elif choice == "1":
            chatbot_menu(AIAssistant())
        elif choice == "2":
            text_analysis_menu()
        elif choice == "3":
            text_statistics_menu()
        elif choice == "4":
            data_processing_menu()
        elif choice == "5":
            file_management_menu()
        elif choice == "6":
            word_frequency_menu()
        elif choice == "7":
            sentiment_analysis_menu()
        else:
            print("\n❌ Geçersiz seçim. Lütfen 0-7 arasında bir sayı girin.")


if __name__ == "__main__":
    main()
