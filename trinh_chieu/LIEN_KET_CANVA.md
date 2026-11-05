# Bài trình chiếu Canva - Đề 8, Nhóm 8

**[Mở bài trình chiếu Canva 10 trang](https://canva.link/501qey52s0wqhti)**

[Liên kết Canva đầy đủ, chỉ xem](https://www.canva.com/design/DAHaA3KPt4c/BppV63r11zDIIqbR95-p5w/view) · [Tải bản PDF 10 trang](Bai_trinh_chieu_Canva_Nhom_8.pdf) · [Xem ảnh tổng quan](Xem_truoc_trinh_chieu_Nhom_8.jpg).

- Học viện Công nghệ Bưu chính Viễn thông, Khoa Viễn thông 1.
- Học phần: Phương pháp thống kê dữ liệu.
- Đề 8: So sánh hai phương án định tuyến bằng dữ liệu độ trễ.
- Nhóm 8. Giảng viên: **Vũ Quang Minh**.
- Bài trình chiếu gồm đúng **10 trang**, khổ 16:9.
- Quyền truy cập: **chỉ xem công khai**, không cần đăng nhập để mở; liên kết này không cấp quyền chỉnh sửa.

## Thiết kế cuối và nguồn chỉnh sửa

Bản cuối áp dụng Taste Skill adaptation: nền ngà, chữ màu mực, nhấn cobalt và cam; heading Times New Roman, nội dung và số liệu Arial. Các biểu đồ là đối tượng vector dựng từ số liệu phân tích.

- [Nguồn HTML để nhập Canva](nguon_canva/deck-canva.html) hoặc [gói nguồn ZIP](nguon_canva/deck-canva-assets.zip).
- [Bản HTML xem trước](nguon_canva/preview.html) dùng để xem trên trình duyệt.
- [Hướng dẫn nguồn và cách dựng lại](nguon_canva/README_NGUON_CANVA.md). Chạy `python scripts/build_canva_html.py` từ thư mục gốc kho để dựng lại nguồn.
- [Nội dung và ghi chú thuyết trình](NOI_DUNG_CANVA.md) tương ứng với bản cuối.

Phân công trong trang 10 là **đề xuất 20% mỗi thành viên**, cần nhóm xác nhận theo đóng góp thực tế.

## Nội dung và nguồn số liệu

[Nội dung chi tiết, ghi chú thuyết trình và tài liệu tham khảo](NOI_DUNG_CANVA.md) trình bày đầy đủ 10 trang. Các biểu đồ được dựng từ số liệu phân tích, không dùng dữ liệu giả để minh họa kết quả.

| Nguồn | Vai trò trong trình chiếu |
| --- | --- |
| [data/sample_detail.csv](../data/sample_detail.csv) | 80 quan sát của hai nhóm độc lập, dùng cho thống kê mô tả, histogram và biểu đồ hộp. |
| [data/pooled_ranks.csv](../data/pooled_ranks.csv) | Toàn bộ bảng gộp hạng và ví dụ minh họa Mann–Whitney. |
| [results/descriptive.csv](../results/descriptive.csv) | Trung bình, trung vị, SD, Q1, Q3 và IQR. |
| [results/detail_tests.csv](../results/detail_tests.csv) | Kết quả Mann–Whitney, Welch và khoảng tin cậy chênh lệch trung bình. |
| [results/simulation_200.csv](../results/simulation_200.csv) | Kết quả của từng lần trong 200 lần mô phỏng mới. |
| [results/simulation_summary.csv](../results/simulation_summary.csv) | Tỷ lệ phát hiện và khoảng Wilson 95%. |
| [results/summary.json](../results/summary.json) | Seed, phiên bản thư viện và toàn bộ số liệu tổng hợp. |

Toàn bộ dữ liệu là **dữ liệu mô phỏng**, seed **20261104**. Mẫu chi tiết chưa đủ bằng chứng khác biệt ở mức 5% bằng cả hai kiểm định; B thấp hơn 4 ms là đặc điểm của mô hình tạo dữ liệu. Hướng dẫn chạy lại nằm trong [README](../README.md).
