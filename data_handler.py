import json
import csv
from pathlib import Path


class DataHandler:
    """Veri işleme ve dosya yönetimi sınıfı"""
    
    @staticmethod
    def read_text_file(filepath):
        """Metin dosyasını oku"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"Hata: '{filepath}' dosyası bulunamadı"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    @staticmethod
    def write_text_file(filepath, content):
        """Metin dosyasına yaz"""
        try:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"✓ '{filepath}' dosyasına başarıyla yazıldı"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    @staticmethod
    def read_json_file(filepath):
        """JSON dosyasını oku"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return f"Hata: '{filepath}' dosyası bulunamadı"
        except json.JSONDecodeError:
            return "Hata: JSON dosyası geçersiz"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    @staticmethod
    def write_json_file(filepath, data):
        """JSON dosyasına yaz"""
        try:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return f"✓ '{filepath}' dosyasına başarıyla yazıldı"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    @staticmethod
    def read_csv_file(filepath):
        """CSV dosyasını oku"""
        try:
            rows = []
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            return {"status": "success", "data": rows}
        except FileNotFoundError:
            return {"status": "error", "message": f"'{filepath}' dosyası bulunamadı"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    @staticmethod
    def write_csv_file(filepath, data, fieldnames=None):
        """CSV dosyasına yaz"""
        try:
            if not data:
                return "Hata: Veri boş"
            
            if fieldnames is None:
                fieldnames = list(data[0].keys()) if isinstance(data[0], dict) else None
            
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            return f"✓ '{filepath}' dosyasına başarıyla yazıldı"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    @staticmethod
    def list_files(directory):
        """Klasördeki dosyaları listele"""
        try:
            files = list(Path(directory).glob('*'))
            return [str(f) for f in files]
        except FileNotFoundError:
            return f"Hata: '{directory}' klasörü bulunamadı"
        except Exception as e:
            return f"Hata: {str(e)}"
    
    @staticmethod
    def file_size(filepath):
        """Dosya boyutunu öğren"""
        try:
            size = Path(filepath).stat().st_size
            if size < 1024:
                return f"{size} B"
            elif size < 1024 * 1024:
                return f"{size / 1024:.2f} KB"
            else:
                return f"{size / (1024 * 1024):.2f} MB"
        except FileNotFoundError:
            return "Hata: Dosya bulunamadı"
        except Exception as e:
            return f"Hata: {str(e)}"
