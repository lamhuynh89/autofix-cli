import sys
import subprocess
import os

def get_last_error():
    """Giả lập lấy lỗi cuối cùng từ clipboard hoặc history."""
    return "git pus origin main\nerror: src refspec main does not match any"

def suggest_fix(error_text):
    """Phân tích lỗi cơ bản để đề xuất cách sửa (Mock AI)."""
    error_text = error_text.lower()
    if "git pus" in error_text:
        return "git push origin main"
    elif "python:" in error_text and "no such file" in error_text:
        return "Kiểm tra lại đường dẫn file Python của bạn."
    elif "module not found" in error_text:
        return "pip install <tên-module>"
    else:
        return "Thử thêm 'sudo' hoặc kiểm tra chính tả."

def main():
    print("🚀 AutoFix CLI - Đang phân tích lỗi gần nhất...")
    
    # 1. Lấy lỗi
    error_text = get_last_error()
    print(f"\n[Lỗi phát hiện]:\n{error_text}")
    
    # 2. Đề xuất
    suggestion = suggest_fix(error_text)
    print(f"\n[Đề xuất sửa lỗi]:\n👉 {suggestion}")
    
    # 3. Tuỳ chọn thực thi
    confirm = input("\nBạn có muốn thực thi lệnh này không? (y/n): ")
    if confirm.lower() == 'y':
        print(f"Đang chạy: {suggestion}")
        # Trong thực tế sẽ gọi: os.system(suggestion)
        print("✅ Đã thực thi thành công!")
    else:
        print("Đã huỷ thao tác.")

if __name__ == "__main__":
    main()
