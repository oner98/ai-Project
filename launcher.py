#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🤖 Yapay Zeka Yardımcısı - Launcher (CLI veya GUI seçimi)
"""

import sys
import os


def main():
    """Başlatıcı menü"""
    print("\n" + "="*60)
    print("🤖 YAPAY ZEKA YARDIMCISI")
    print("="*60)
    print("\nBaşlatma Modu Seçiniz:\n")
    print("1. 🖥️  GUI (Grafik Arayüz)")
    print("2. 📟 CLI (Komut Satırı)")
    print("0. Çıkış")
    print("="*60)
    
    choice = input("\nSeçiminiz (0-2): ").strip()
    
    if choice == "1":
        print("\n🖥️  GUI uygulaması başlatılıyor...")
        try:
            from gui_app import main as gui_main
            gui_main()
        except ImportError:
            print("❌ Hata: GUI uygulaması bulunamadı!")
            print("Lütfen gui_app.py dosyasının proje klasöründe olduğundan emin olun.")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Hata: {str(e)}")
            sys.exit(1)
    
    elif choice == "2":
        print("\n📟 CLI uygulaması başlatılıyor...")
        try:
            from main import show_menu, chatbot_menu, text_analysis_menu
            from ai_assistant import AIAssistant
            from text_processor import TextProcessor
            from data_handler import DataHandler
            
            # CLI menüsü burada çalıştırabilir
            print("CLI uygulamasını başlatmak için: python main.py")
            import main as cli_main
            cli_main.main()
        except Exception as e:
            print(f"❌ Hata: {str(e)}")
            sys.exit(1)
    
    elif choice == "0":
        print("\n👋 Hoşça kalın!")
        sys.exit(0)
    
    else:
        print("\n❌ Geçersiz seçim! Lütfen 0-2 arasında bir sayı giriniz.")
        main()


if __name__ == "__main__":
    main()
