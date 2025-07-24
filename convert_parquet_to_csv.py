
import pandas as pd
import gdown
import os

# Đảm bảo đang làm việc tại đúng thư mục
os.chdir("C:/Users/truon/Desktop/DA/1")

# 1. Tải file từ Google Drive
url = "https://drive.google.com/uc?id=1AaKzlObB9YyOKa5qHLPp6ackBIUXRkRp"
output = "data.parquet"
print("🔽 Đang tải file .parquet từ Google Drive...")
gdown.download(url, output, quiet=False)

# 2. Đọc file parquet
print("📂 Đang đọc dữ liệu...")
df = pd.read_parquet("data.parquet")
print(f"✅ Dữ liệu có {len(df):,} dòng và {len(df.columns):,} cột.")

# 3. Cắt đúng 1 triệu dòng đầu tiên
sample_df = df.head(1_000_000)

# 4. Xuất ra file CSV
csv_output = "sample_1M_rows.csv"
sample_df.to_csv(csv_output, index=False)
print(f"📁 Đã lưu 1 triệu dòng vào file: {csv_output}")
print("🎉 Hoàn tất! Bạn có thể mở file này trong Excel hoặc Power BI.")
