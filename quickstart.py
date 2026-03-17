#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🤖 YAPAY ZEKA YARDIMCISI - KURULUM VE BAŞLATMA REHBERI

Bu dosyayı çalıştırarak uygulamayı test edebilir ve başlatabilirsiniz.
python quickstart.py
"""

import os
import sys
import subprocess
from pathlib import Path


def print_header(text):
    """Başlık yazdır"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70)


def check_python_version():
    """Python versiyonunu kontrol et"""
    print_header("🔍 PYTHON VERSİYON KONTROLÜ")
    
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"✅ Python Versiyonu: {version}")
    
    if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 7):
        print("❌ Hata: Python 3.7+ gereklidir!")
        return False
    
    print("✅ Python versiyonu gereksinimini karşılıyor.")
    return True


def check_tkinter():
    """Tkinter kontrol et"""
    print_header("🔍 TKİNTER KONTROLÜ")
    
    try:
        import tkinter as tk
        print("✅ Tkinter başarıyla yüklü.")
        return True
    except ImportError:
        print("❌ Tkinter bulunamadı!")
        print("\n💡 Yükleme talimatları:")
        print("   Windows: python -m pip install tk")
        print("   macOS: brew install python-tk@3.9")
        print("   Linux (Ubuntu): sudo apt-get install python3-tk")
        return False


def check_requirements():
    """Gerekli paketleri kontrol et"""
    print_header("🔍 GEREKLI PAKETLER KONTROLÜ")
    
    required = [
        'nltk',
        'requests',
        'pandas',
        'numpy',
        'python-dotenv'
    ]
    
    missing = []
    for package in required:
        try:
            __import__(package.replace('-', '_'))
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package}")
            missing.append(package)
    
    if missing:
        print(f"\n❌ {len(missing)} paket eksik!")
        print("\nYüklemek için komutu çalıştırın:")
        print(f"  pip install {' '.join(missing)}")
        return False
    
    print("\n✅ Tüm gerekli paketler yüklü.")
    return True


def check_project_files():
    """Proje dosyalarını kontrol et"""
    print_header("🔍 PROJE DOSYALARI KONTROLÜ")
    
    required_files = [
        'main.py',
        'gui_app.py',
        'launcher.py',
        'ai_assistant.py',
        'text_processor.py',
        'data_handler.py',
        'requirements.txt',
        'README.md',
        'GUI_REHBERI.md'
    ]
    
    project_path = Path(__file__).parent
    missing = []
    
    for file in required_files:
        file_path = project_path / file
        if file_path.exists():
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file}")
            missing.append(file)
    
    if missing:
        print(f"\n❌ {len(missing)} dosya eksik!")
        return False
    
    print("\n✅ Tüm proje dosyaları mevcut.")
    return True


def install_requirements():
    """Gerekli paketleri yükle"""
    print_header("📦 PAKET YÜKLEME")
    
    print("requirements.txt'den paketler yükleniyor...\n")
    
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
        ])
        print("\n✅ Paketler başarıyla yüklendi.")
        return True
    except subprocess.CalledProcessError:
        print("\n❌ Paket yükleme sırasında hata oluştu.")
        return False


def run_tests():
    """Testleri çalıştır"""
    print_header("🧪 TESTLERI ÇALIŞTIR")
    
    if os.path.exists('run_tests.py'):
        try:
            subprocess.check_call([sys.executable, 'run_tests.py'])
            print("\n✅ Testler başarıyla tamamlandı.")
            return True
        except subprocess.CalledProcessError:
            print("\n⚠️  Bazı testler başarısız oldu.")
            return False
    else:
        print("⚠️  run_tests.py dosyası bulunamadı.")
        return True


def launch_app():
    """Uygulamayı başlat"""
    print_header("🚀 UYGULAMAYI BAŞLAT")
    
    print("\nBaşlatma seçenekleri:\n")
    print("1. 🖥️  GUI (Grafik Arayüz)")
    print("2. 📟 CLI (Komut Satırı)")
    print("3. <Enter> varsayılan seçim (GUI)")
    print("\n" + "-"*70)
    
    choice = input("\nSeçiminiz: ").strip()
    
    if choice == "1" or choice == "":
        print("\n🖥️  GUI uygulaması başlatılıyor...\n")
        try:
            from gui_app import main
            main()
        except Exception as e:
            print(f"❌ Hata: {e}")
            return False
    
    elif choice == "2":
        print("\n📟 CLI uygulaması başlatılıyor...\n")
        try:
            from main import show_menu, chatbot_menu
            from ai_assistant import AIAssistant
            import main as cli_main
            cli_main.main()
        except Exception as e:
            print(f"❌ Hata: {e}")
            return False
    
    else:
        print("❌ Geçersiz seçim!")
        return False
    
    return True


def main():
    """Ana kurulum ve başlatma işlemi"""
    print("\n")
    print("█" * 70)
    print("█" + " " * 68 + "█")
    print("█" + "  🤖 YAPAY ZEKA YARDIMCISI - KURULUM VE BAŞLATMA".center(68) + "█")
    print("█" + " " * 68 + "█")
    print("█" * 70)
    
    # Kontroller
    checks = [
        ("Python Versiyonu", check_python_version),
        ("Tkinter (GUI için gerekli)", check_tkinter),
        ("Proje Dosyaları", check_project_files),
        ("Gerekli Paketler", check_requirements),
    ]
    
    all_ok = True
    for check_name, check_func in checks:
        if not check_func():
            all_ok = False
    
    if not all_ok:
        print_header("⚠️  KURULUM UYARISI")
        print("\n❌ Eksik bileşenler var!")
        
        print("\n💡 Çözüm önerileri:")
        print("1. requirements.txt paketlerini yükleyin:")
        print("   pip install -r requirements.txt")
        print("\n2. Tkinter yükleyin:")
        print("   python -m pip install tk")
        print("\n3. Tüm dosyaları kontrol edin")
        
        choice = input("\nGerekli paketleri yüklemek istiyorsunuz? (E/H): ").strip().lower()
        if choice == 'e':
            if not install_requirements():
                return
        else:
            return
    
    # Başarılı kurulum
    print_header("✅ KURULUM BAŞARILI")
    print("\n✨ Sistem hazır!")
    print("\nUygulamayı başlatmak için bir seçim yapın:")
    
    # Uygulamayı başlat
    launch_app()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Çıkılıyor...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Beklenmeyen hata: {e}")
        sys.exit(1)
