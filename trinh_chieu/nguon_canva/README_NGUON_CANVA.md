# Nguồn trình chiếu Canva

Bản nhập dùng `deck-canva.html` hoặc `deck-canva-assets.zip`. ZIP chỉ chứa `index.html` có cùng byte với nguồn HTML. Không có ảnh nền, font tải ngoài, JavaScript hay tài nguyên bắt buộc khác trong bản nhập. Các biểu đồ là hình chữ nhật, đường kẻ, điểm và nhãn HTML/CSS.

`preview.html` dùng JavaScript riêng để chuyển trang và co tỷ lệ theo màn hình. Không dùng tệp xem trước này để nhập Canva.

## Dựng lại bằng Python tiêu chuẩn

Đặt `build_canva_html.py` trong thư mục `scripts/` của kho có `results/summary.json`, `data/sample_detail.csv` và `data/pooled_ranks.csv`, rồi chạy:

```sh
python scripts/build_canva_html.py
```

Đầu ra mặc định nằm trong `trinh_chieu/nguon_canva/`. Có thể chọn vị trí khác:

```sh
python scripts/build_canva_html.py --repo-root . --output-dir work/canva_preview
```

Không cần cài thêm thư viện. Mã đọc dữ liệu gốc và kết quả đã có, không thay báo cáo hay dữ liệu.

## Thiết kế và kiểm tra

Ivory, ink, cobalt và burnt orange. Times New Roman cho heading tiếng Việt, Arial cho body và số liệu, lề 80 px. Hai trang accent tối đa. Nguồn thiết kế theo Taste Skill adaptation, không chạy bộ CLI upstream.

Giữ bản báo cáo và phân tích Python làm căn cứ kết quả. Nhóm cần xác nhận bảng phân công đề xuất 20% mỗi thành viên. Sau khi nhập Canva, xem lại đủ 10 trang và các biểu đồ trước khi dùng bản xuất.
