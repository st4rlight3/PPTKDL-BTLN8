# Bài trình chiếu Canva - Đề 8, Nhóm 8

**[Mở bài trình chiếu Canva 10 trang](https://canva.link/rcifdyyoaund7yv)**

- Học viện Công nghệ Bưu chính Viễn thông, Khoa Viễn thông 1.
- Học phần: Phương pháp thống kê dữ liệu.
- Đề 8: So sánh hai phương án định tuyến bằng dữ liệu độ trễ.
- Nhóm 8. Giảng viên: **Vũ Quang Minh**.
- Bài trình chiếu gồm đúng **10 trang**, khổ 16:9.
- Quyền truy cập: **chỉ xem công khai**, không cần đăng nhập để mở; liên kết này không cấp quyền chỉnh sửa.

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
