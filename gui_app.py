#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import os
import json
from ai_assistant import AIAssistant
from text_processor import TextProcessor
from data_handler import DataHandler


class AIAssistantGUI:
    """GUI uygulaması - Yapay Zeka Yardımcısı"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Yapay Zeka Yardımcısı")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        
        # Modülleri başlat
        self.assistant = AIAssistant()
        self.validator = TextProcessor()
        self.data_handler = DataHandler()
        
        # Tema için renkler
        self.bg_color = "#f0f0f0"
        self.header_color = "#2c3e50"
        self.button_color = "#3498db"
        self.accent_color = "#e74c3c"
        
        self.setup_gui()
    
    def setup_gui(self):
        """GUI'nin ana yapısını oluştur"""
        # Başlık
        header_frame = tk.Frame(self.root, bg=self.header_color, padx=20, pady=15)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            header_frame, 
            text="🤖 Yapay Zeka Yardımcısı",
            font=("Helvetica", 20, "bold"),
            bg=self.header_color,
            fg="white"
        )
        title_label.pack()
        
        # Tab ve menü sistemi oluştur
        self.create_notebook()
    
    def create_notebook(self):
        """Ana sekme sistemini oluştur"""
        notebook = ttk.Notebook(self.root, padding=10)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Sekmeleri oluştur
        self.chatbot_tab(notebook)
        self.text_analysis_tab(notebook)
        self.statistics_tab(notebook)
        self.file_management_tab(notebook)
        self.word_frequency_tab(notebook)
        self.sentiment_analysis_tab(notebook)
        
        # Tab stilini ayarla
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook.Tab', padding=[20, 10])
    
    def chatbot_tab(self, notebook):
        """Chatbot sekmesi"""
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text="💬 Chatbot")
        
        # Hoşgeldiniz mesajı
        greeting = tk.Label(
            frame,
            text=self.assistant.greet(),
            font=("Helvetica", 11),
            bg="#ecf0f1",
            wraplength=800,
            padx=10,
            pady=10,
            justify=tk.LEFT
        )
        greeting.pack(fill=tk.X, pady=(0, 15))
        
        # Sohbet tarihi alanı
        chat_frame = tk.Frame(frame, bg="white", height=300)
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            height=12,
            width=80,
            wrap=tk.WORD,
            font=("Courier", 10),
            bg="white",
            fg="#2c3e50",
            state=tk.DISABLED
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Giriş alanı
        input_frame = tk.Frame(frame)
        input_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(input_frame, text="Mesajınız:", font=("Helvetica", 10), bg="#f0f0f0").pack(anchor=tk.W)
        
        self.chat_input = tk.Entry(input_frame, font=("Helvetica", 10), width=80)
        self.chat_input.pack(fill=tk.X, pady=5)
        self.chat_input.bind("<Return>", lambda e: self.send_message())
        
        # Butonlar
        button_frame = tk.Frame(frame, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, pady=(5, 0))
        
        send_btn = tk.Button(
            button_frame,
            text="📤 Gönder",
            command=self.send_message,
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 10),
            padx=15,
            pady=8
        )
        send_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Temizle",
            command=self.clear_chat,
            bg="#95a5a6",
            fg="white",
            font=("Helvetica", 10),
            padx=15,
            pady=8
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
    
    def send_message(self):
        """Sohbet mesajı gönder"""
        message = self.chat_input.get().strip()
        
        if not message:
            messagebox.showwarning("Uyarı", "Lütfen bir mesaj giriniz!")
            return
        
        if any(word in message.lower() for word in ["çıkış", "quit", "exit"]):
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.insert(tk.END, f"Sen: {message}\n")
            self.chat_display.insert(tk.END, f"AI: {self.assistant.say_goodbye()}\n\n")
            self.chat_display.config(state=tk.DISABLED)
            self.chat_input.delete(0, tk.END)
            return
        
        # Update chat display
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"Sen: {message}\n")
        
        response = self.assistant.respond_to_query(message)
        self.chat_display.insert(tk.END, f"AI: {response}\n\n")
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_input.delete(0, tk.END)
    
    def clear_chat(self):
        """Sohbet geçmişini temizle"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def text_analysis_tab(self, notebook):
        """Metin analizi sekmesi"""
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text="📝 Metin Analizi")
        
        # Giriş alanı
        tk.Label(frame, text="Analiz edecek metni giriniz:", font=("Helvetica", 10, "bold")).pack(anchor=tk.W)
        
        input_area = scrolledtext.ScrolledText(
            frame,
            height=8,
            width=80,
            wrap=tk.WORD,
            font=("Courier", 10)
        )
        input_area.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        
        # Butonlar
        button_frame = tk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        analyze_btn = tk.Button(
            button_frame,
            text="🔍 Analiz Et",
            command=lambda: self.analyze_text(input_area),
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 10),
            padx=15,
            pady=8
        )
        analyze_btn.pack(side=tk.LEFT, padx=5)
        
        # Çıkış alanı
        tk.Label(frame, text="Analiz Sonuçları:", font=("Helvetica", 10, "bold")).pack(anchor=tk.W, pady=(10, 0))
        
        self.analysis_output = scrolledtext.ScrolledText(
            frame,
            height=8,
            width=80,
            wrap=tk.WORD,
            font=("Courier", 10),
            bg="#ecf0f1",
            state=tk.DISABLED
        )
        self.analysis_output.pack(fill=tk.BOTH, expand=True)
    
    def analyze_text(self, input_area):
        """Metni analiz et"""
        text = input_area.get(1.0, tk.END).strip()
        
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen analiz edilecek metni giriniz!")
            return
        
        try:
            # Metin temizleme ve analiz
            cleaned = self.validator.clean_text(text)
            tokens = self.validator.tokenize(cleaned)
            word_freq = self.validator.get_word_frequency(text, top_n=5)
            
            # Sonuçları göster
            self.analysis_output.config(state=tk.NORMAL)
            self.analysis_output.delete(1.0, tk.END)
            
            result = f"""
📊 METIN ANALİZİ SONUÇLARI
{'='*60}

📈 İstatistikler:
  • Kelime Sayısı: {len(tokens['words'])}
  • Cümle Sayısı: {len(tokens['sentences'])}
  • Karakter Sayısı: {len(cleaned)}
  • Ortalama Kelime Uzunluğu: {len(cleaned)/max(1, len(tokens['words'])):.2f}

🔝 En Sık Kullanılan Kelimeler (Top 5):
"""
            for idx, (word, count) in enumerate(word_freq.items(), 1):
                result += f"  {idx}. {word}: {count} kez\n"
            
            self.analysis_output.insert(tk.END, result)
            self.analysis_output.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Hata", f"Analiz sırasında hata oluştu: {str(e)}")
    
    def statistics_tab(self, notebook):
        """Metin istatistikleri sekmesi"""
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text="📊 İstatistikler")
        
        # Metin giriş
        tk.Label(frame, text="Metin:", font=("Helvetica", 10, "bold")).pack(anchor=tk.W)
        
        text_input = scrolledtext.ScrolledText(
            frame,
            height=8,
            width=80,
            wrap=tk.WORD,
            font=("Courier", 10)
        )
        text_input.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        
        # Butonlar
        btn_frame = tk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        stats_btn = tk.Button(
            btn_frame,
            text="📈 İstatistikleri Hesapla",
            command=lambda: self.calculate_statistics(text_input),
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 10),
            padx=15,
            pady=8
        )
        stats_btn.pack(side=tk.LEFT, padx=5)
        
        # Sonuçlar
        tk.Label(frame, text="Sonuçlar:", font=("Helvetica", 10, "bold")).pack(anchor=tk.W, pady=(10, 0))
        
        self.stats_output = scrolledtext.ScrolledText(
            frame,
            height=8,
            width=80,
            font=("Courier", 10),
            bg="#ecf0f1",
            state=tk.DISABLED
        )
        self.stats_output.pack(fill=tk.BOTH, expand=True)
    
    def calculate_statistics(self, text_input):
        """İstatistikleri hesapla"""
        text = text_input.get(1.0, tk.END).strip()
        
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen metin giriniz!")
            return
        
        try:
            tokens = self.validator.tokenize(text)
            words = tokens['words']
            sentences = tokens['sentences']
            
            self.stats_output.config(state=tk.NORMAL)
            self.stats_output.delete(1.0, tk.END)
            
            stats = f"""
📊 METIN İSTATİSTİKLERİ
{'='*60}

📈 Sayılar:
  • Karakter Sayısı: {len(text)}
  • Kelime Sayısı: {len(words)}
  • Cümle Sayısı: {len(sentences)}

📊 Ortalamalar:
  • Ortalama Kelime Uzunluğu: {sum(len(w) for w in words)/max(1, len(words)):.2f} karakter
  • Ortalama Cümle Uzunluğu: {len(words)/max(1, len(sentences)):.2f} kelime
  • Ortalama Cümle Uzunluğu: {len(text.split())/max(1, len(sentences)):.2f} karakter

🔍 Detaylı:
  • En uzun kelime: {max(words, key=len) if words else 'N/A'} ({max(len(w) for w in words) if words else 0} karakter)
  • En kısa kelime: {min(words, key=len) if words else 'N/A'} ({min(len(w) for w in words) if words else 0} karakter)
"""
            
            self.stats_output.insert(tk.END, stats)
            self.stats_output.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Hata", f"Hata: {str(e)}")
    
    def file_management_tab(self, notebook):
        """Dosya yönetimi sekmesi"""
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text="🗂️ Dosya Yönetimi")
        
        # Dosya yolu girişi
        path_frame = tk.Frame(frame)
        path_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(path_frame, text="Klasör Yolu:", font=("Helvetica", 10, "bold")).pack(anchor=tk.W)
        
        self.path_input = tk.Entry(path_frame, font=("Helvetica", 10), width=80)
        self.path_input.pack(fill=tk.X, pady=(5, 0))
        self.path_input.insert(0, os.getcwd())
        
        # Butonlar
        btn_frame = tk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        browse_btn = tk.Button(
            btn_frame,
            text="📂 Klasör Seç",
            command=self.browse_folder,
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 10),
            padx=10,
            pady=8
        )
        browse_btn.pack(side=tk.LEFT, padx=5)
        
        list_btn = tk.Button(
            btn_frame,
            text="📋 Dosyaları Listele",
            command=lambda: self.list_files(self.path_input.get()),
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 10),
            padx=10,
            pady=8
        )
        list_btn.pack(side=tk.LEFT, padx=5)
        
        # Dosya listesi
        tk.Label(frame, text="Dosyalar:", font=("Helvetica", 10, "bold")).pack(anchor=tk.W, pady=(10, 0))
        
        self.files_output = scrolledtext.ScrolledText(
            frame,
            height=15,
            width=80,
            font=("Courier", 9),
            bg="#ecf0f1"
        )
        self.files_output.pack(fill=tk.BOTH, expand=True)
    
    def browse_folder(self):
        """Klasör seç"""
        folder = filedialog.askdirectory(title="Klasör Seçiniz")
        if folder:
            self.path_input.delete(0, tk.END)
            self.path_input.insert(0, folder)
    
    def list_files(self, path):
        """Dosyaları listele"""
        try:
            if not os.path.exists(path):
                messagebox.showerror("Hata", "Klasör bulunamadı!")
                return
            
            self.files_output.config(state=tk.NORMAL)
            self.files_output.delete(1.0, tk.END)
            
            files = os.listdir(path)
            
            output = f"📂 Klasör: {path}\n{'='*60}\n\n"
            
            if not files:
                output += "Bu klasör boş.\n"
            else:
                for file in sorted(files):
                    full_path = os.path.join(path, file)
                    if os.path.isdir(full_path):
                        output += f"📁 {file}/\n"
                    else:
                        size = os.path.getsize(full_path)
                        output += f"📄 {file} ({size:,} bytes)\n"
            
            self.files_output.insert(tk.END, output)
            self.files_output.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Hata", f"Hata: {str(e)}")
    
    def word_frequency_tab(self, notebook):
        """Kelime frekansı sekmesi"""
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text="📈 Kelime Frekansı")
        
        # Metin girişi
        tk.Label(frame, text="Metin:", font=("Helvetica", 10, "bold")).pack(anchor=tk.W)
        
        text_input = scrolledtext.ScrolledText(
            frame,
            height=8,
            width=80,
            wrap=tk.WORD,
            font=("Courier", 10)
        )
        text_input.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        
        # Kontroller
        control_frame = tk.Frame(frame)
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(control_frame, text="Kaç kelime gösterilsin?", font=("Helvetica", 9)).pack(side=tk.LEFT, padx=(0, 5))
        
        self.freq_count = tk.Spinbox(
            control_frame,
            from_=1,
            to=50,
            width=5,
            font=("Helvetica", 10)
        )
        self.freq_count.delete(0, tk.END)
        self.freq_count.insert(0, 10)
        self.freq_count.pack(side=tk.LEFT, padx=5)
        
        # Buton
        freq_btn = tk.Button(
            control_frame,
            text="🔍 Analiz Et",
            command=lambda: self.analyze_frequency(text_input),
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 10),
            padx=15,
            pady=5
        )
        freq_btn.pack(side=tk.LEFT, padx=5)
        
        # Sonuçlar
        tk.Label(frame, text="Sonuçlar:", font=("Helvetica", 10, "bold")).pack(anchor=tk.W, pady=(10, 0))
        
        self.freq_output = scrolledtext.ScrolledText(
            frame,
            height=10,
            width=80,
            font=("Courier", 10),
            bg="#ecf0f1",
            state=tk.DISABLED
        )
        self.freq_output.pack(fill=tk.BOTH, expand=True)
    
    def analyze_frequency(self, text_input):
        """Kelime frekansını analiz et"""
        text = text_input.get(1.0, tk.END).strip()
        top_n = int(self.freq_count.get())
        
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen metin giriniz!")
            return
        
        try:
            freq = self.validator.get_word_frequency(text, top_n)
            
            self.freq_output.config(state=tk.NORMAL)
            self.freq_output.delete(1.0, tk.END)
            
            output = f"📈 KELİME FREKANS ANALİZİ (Top {top_n})\n{'='*60}\n\n"
            
            max_freq = max(freq.values()) if freq else 1
            
            for idx, (word, count) in enumerate(freq.items(), 1):
                bar_length = int((count / max_freq) * 30)
                bar = "█" * bar_length
                output += f"{idx:2}. {word:20} | {bar} {count}\n"
            
            self.freq_output.insert(tk.END, output)
            self.freq_output.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Hata", f"Hata: {str(e)}")
    
    def sentiment_analysis_tab(self, notebook):
        """Duygu analizi sekmesi"""
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text="😊 Duygu Analizi")
        
        # Metin girişi
        tk.Label(frame, text="Duygu analizi yapılacak metin:", font=("Helvetica", 10, "bold")).pack(anchor=tk.W)
        
        text_input = scrolledtext.ScrolledText(
            frame,
            height=8,
            width=80,
            wrap=tk.WORD,
            font=("Courier", 10)
        )
        text_input.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        
        # Buton
        btn_frame = tk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        analyze_btn = tk.Button(
            btn_frame,
            text="🔍 Duygu Analizi Yap",
            command=lambda: self.analyze_sentiment(text_input),
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 10),
            padx=15,
            pady=8
        )
        analyze_btn.pack(side=tk.LEFT, padx=5)
        
        # Sonuçlar
        tk.Label(frame, text="Sonuçlar:", font=("Helvetica", 10, "bold")).pack(anchor=tk.W, pady=(10, 0))
        
        self.sentiment_output = scrolledtext.ScrolledText(
            frame,
            height=10,
            width=80,
            font=("Courier", 10),
            bg="#ecf0f1",
            state=tk.DISABLED
        )
        self.sentiment_output.pack(fill=tk.BOTH, expand=True)
    
    def analyze_sentiment(self, text_input):
        """Duygu analizi yap"""
        text = text_input.get(1.0, tk.END).strip()
        
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen metin giriniz!")
            return
        
        try:
            sentiment = self.assistant.analyze_sentiment(text)
            
            self.sentiment_output.config(state=tk.NORMAL)
            self.sentiment_output.delete(1.0, tk.END)
            
            output = f"""
😊 DUYGU ANALİZİ SONUÇLARI
{'='*60}

Metin: "{text[:100]}{'...' if len(text) > 100 else ''}"

Sonuç:
  {sentiment}
"""
            
            self.sentiment_output.insert(tk.END, output)
            self.sentiment_output.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Hata", f"Hata: {str(e)}")


def main():
    """Ana fonksiyon"""
    root = tk.Tk()
    app = AIAssistantGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
