# Đối chiếu yêu cầu đề 8 của nhóm 8

## Yêu cầu chung

| Yêu cầu | Vị trí đáp ứng |
| --- | --- |
| Nhóm 4–5 người, dự kiến 3 tuần | 5 thành viên ở bìa và mục 11.1. Kế hoạch đề xuất 3 tuần ở mục 10.1. |
| Công cụ và bước xử lý | Báo cáo mục 1.2, 10; README và scripts/analysis.py. |
| Ghi rõ dữ liệu mô phỏng | Bìa, mục 1, 9 và README. Không trình bày như số đo thật. |
| Seed, dữ liệu gốc, mã và kết quả | Seed 20261104; data/, results/, scripts/, README. |
| Ý nghĩa 5%, tin cậy 95% | Hai kiểm định hai phía α=0,05; KTC Welch và Wilson 95%. |
| Ước lượng từ từng mẫu | SD ddof=1, SE và df từ mẫu. Tham số thật tách riêng tại mục 2.2 và nhãn JSON generator_theory_for_evaluation_only. |
| Lý do chọn, điều kiện và ý nghĩa | Báo cáo mục 4–9. Nêu rõ giới hạn của dữ liệu lệch và thiết kế độc lập. |

## Bảy yêu cầu riêng của đề 8

| Nội dung | Vị trí đáp ứng |
| --- | --- |
| Trung bình, trung vị, SD và IQR | Mục 3, results/descriptive.csv. |
| Histogram và biểu đồ hộp | Mục 3–4, figures/, slide 3–4. |
| Mann-Whitney hai phía và giả thuyết | Mục 5, results/detail_tests.csv. |
| Gộp mẫu, hạng, thống kê U và hạng trùng | Mục 5–6, đủ 80 dòng trong data/pooled_ranks.csv. |
| Welch và khác biệt về đại lượng kiểm định | Mục 7, có KTC chênh lệch trung bình. |
| 200 lần mới và tỷ lệ phát hiện | Mục 8, data/simulation_200_raw.csv, results/simulation_200.csv. |
| Vì sao không dùng ghép cặp | Mục 4.1, README. |

Kết luận mục 9 phân biệt mẫu chưa đủ bằng chứng với tính chất B dịch trái 4 ms của mô hình. Mann-Whitney không mặc nhiên kiểm định trung bình. Diễn giải vị trí dựa vào cùng dạng phân phối.

## Sản phẩm theo trang cuối tài liệu

| Sản phẩm | Tệp |
| --- | --- |
| Báo cáo 8–12 trang | bao_cao/Bao_cao_De_8_Nhom_8.pdf, bản chỉnh sửa .docx, 12 trang. |
| Dữ liệu mẫu và bảng mô phỏng | data/ và results/, có đủ 200 lần. |
| Mã, hướng dẫn chạy và seed | scripts/analysis.py, requirements.txt, README.md. |
| Trình chiếu 8–10 trang | Bài trình chiếu Canva 10 trang, liên kết trong trinh_chieu/LIEN_KET_CANVA.md. |
| Phân công và đóng góp từng người | Báo cáo mục 11.1 và phan_cong.csv. Tỷ lệ là dự kiến, nhóm cần xác nhận thực tế. |

Mục 2.1 của báo cáo chỉ rõ kiến thức nền chương 1–5 và vai trò đối với kiểm định ở chương 7. Tài liệu giao bài không kèm mục lục giáo trình, nên báo cáo không tự gán các tên nội dung cho từng chương riêng lẻ.
