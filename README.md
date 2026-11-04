# Đề 8 - So sánh hai phương án định tuyến

Nhóm 8. Kho mã của nhóm: `PPTKDL-BTLN8`.

Toàn bộ số liệu là **dữ liệu mô phỏng**, không phải độ trễ đo trên mạng thật.

## Thiết kế và seed

- Mỗi mẫu gồm hai nhóm độc lập: A có 40 phiên với `20 + Exponential(scale=10)`; B có 40 phiên với `16 + Exponential(scale=10)`. Đơn vị: ms.
- Seed gốc: **20261104**. Không đổi seed sau khi xem kết quả.
- `SeedSequence(20261104).spawn(2)` tách mẫu phân tích chi tiết (khóa `(0,)`) khỏi mô phỏng lặp (khóa `(1,)`).
- Nhánh mô phỏng lặp sinh 200 luồng con có khóa `(1, 0)` đến `(1, 199)`. Mỗi lần lặp sinh mới đầy đủ 80 quan sát; hai phương pháp dùng cùng dữ liệu của lần lặp đó để so sánh công bằng.
- Bộ sinh số: `numpy.random.default_rng` (PCG64). Phương sai mẫu dùng `ddof=1`; tứ phân vị dùng nội suy tuyến tính của NumPy. Dữ liệu gốc không được làm tròn trước phân tích.

## Chạy lại

Cần Python 3.12 và các thư viện trong `requirements.txt`. Chạy từ thư mục gốc repo:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe scripts/analysis.py --seed 20261104 --out-dir .
```

Trên macOS/Linux, thay `.venv\Scripts\python.exe` bằng `.venv/bin/python`.

Có thể giữ nguyên các tệp hiện tại và xuất sang thư mục mới để đối chiếu:

```powershell
.venv\Scripts\python.exe scripts/analysis.py --seed 20261104 --out-dir chay_lai
```

`results/sha256_data.json` chứa SHA-256 của các CSV. Cùng seed và phiên bản thư viện trong `requirements.txt` phải tạo lại đúng các CSV. Hình PNG có thể khác siêu dữ liệu/hệ thống font giữa các máy. Đổi seed sẽ tạo một mẫu khác và kết quả khác; không chọn seed theo p-value.

## Các tệp dữ liệu và kết quả

| Tệp | Nội dung |
| --- | --- |
| `data/sample_detail.csv` | 80 quan sát của mẫu phân tích chi tiết; ID, nhóm, độ trễ ms. |
| `data/pooled_ranks.csv` | Toàn bộ 80 quan sát gộp, thứ tự tăng dần và hạng trung bình nếu trùng. |
| `data/simulation_200_raw.csv` | 16.000 quan sát thô của 200 mẫu mới; cột `replicate` xác định lần lặp. |
| `results/descriptive.csv` | n, trung bình, trung vị, SD mẫu, Q1, Q3, IQR và các thống kê bổ sung. |
| `results/detail_tests.csv` | Thống kê U, tổng hạng, p-value Mann-Whitney; t, df, p-value và KTC Welch của mẫu chi tiết. |
| `results/simulation_200.csv` | Một dòng mỗi lần lặp: thống kê, p-value và quyết định của cả hai kiểm định. |
| `results/simulation_summary.csv` | Số lần phát hiện, tỷ lệ, SE Monte Carlo và khoảng Wilson 95%. |
| `results/summary.json` | Toàn bộ số liệu tổng hợp, phiên bản, seed, khóa luồng và giá trị lý thuyết để đánh giá. |
| `results/sha256_data.json` | Dấu vân tay SHA-256 để đối chiếu tệp CSV sau khi chạy lại. |
| `figures/*.png` | Histogram, biểu đồ hộp, tỷ lệ phát hiện và phân bố p-value. |

CSV dùng UTF-8 có BOM, dấu phẩy phân cách, dấu chấm thập phân và 17 chữ số có nghĩa để bảo toàn số thực. Nếu Excel mở sai cột, dùng Data > From Text/CSV, chọn UTF-8 và dấu phẩy; không thay dữ liệu rồi chạy kiểm định trên các số đã làm tròn.

Các ID A01 và B01 chỉ xác định vị trí trong từng nhóm, không xác định một cặp thử nghiệm. Không dùng kiểm định t ghép cặp hoặc Wilcoxon hạng có dấu.

## Phương pháp và kiểm tra

- Mann-Whitney hai phía: `method='asymptotic'`, `use_continuity=True`, có hiệu chỉnh phương sai cho hạng trùng. H0: hai phân phối bằng nhau. Khi hai phân phối cùng dạng và chỉ dịch vị trí như mô hình đã cho, kết quả có thể diễn giải là khác vị trí/trung vị. Đây không mặc nhiên là kiểm định trung bình.
- Welch hai phía: `equal_var=False`. H0: hai kỳ vọng bằng nhau. Sai số chuẩn, bậc tự do Satterthwaite và khoảng tin cậy 95% của trung bình A trừ B đều ước lượng từ mẫu. Với dữ liệu mũ lệch phải, suy luận t ở n=40 mỗi nhóm là xấp xỉ.
- Histogram hai nhóm dùng cùng ranh giới lớp theo quy tắc Freedman-Diaconis trên mẫu gộp và cùng thang trục. Biểu đồ hộp dùng râu 1,5 IQR; các điểm ngoài râu không tự động được xem là lỗi dữ liệu.
- Mức ý nghĩa 0,05. Mỗi lần có `p < 0.05` được tính là phát hiện khác biệt. Trong mô hình có khác biệt thật này, tỷ lệ phát hiện là ước lượng thực nghiệm của lực kiểm định; không phải tỷ lệ sai lầm loại I.
- SE Monte Carlo là `sqrt(p_hat*(1-p_hat)/200)`; khoảng tỷ lệ dùng Wilson 95%. Các khoảng này biểu diễn độ không chắc chắn do chỉ lặp 200 lần.
- Mã tự kiểm tra cho cả 201 mẫu: tổng hạng; `U_A+U_B=1600`; U từ tổng hạng bằng U từ đếm cặp và bằng SciPy; p-value Mann-Whitney tính theo công thức bằng SciPy; t, bậc tự do và p-value Welch tính thủ công bằng SciPy. Mã cũng kiểm tra đủ 200 luồng con và đủ 16.000 quan sát, không trùng khóa bản ghi.
- Các đại lượng lý thuyết trong JSON có nhãn `generator_theory_for_evaluation_only`: dùng giải thích/đánh giá mô phỏng, không thay cho ước lượng của mẫu chi tiết.

## Phạm vi kết luận

Kết quả chỉ áp dụng cho hai phân phối mô phỏng nêu trên. Không suy ra hiệu quả triển khai, chi phí, độ mất gói hoặc năng lượng của một giao thức định tuyến thực tế. Tỷ lệ phát hiện từ 200 lần không chứng minh một kiểm định luôn tốt hơn kiểm định còn lại.

## Thông tin nhóm và bộ sản phẩm

Học viện Công nghệ Bưu chính Viễn thông, Khoa Viễn thông 1. Giảng viên: **Vũ Quang Minh**. Nhóm **8**, thực hiện đề **8**.

| Thành viên | MSSV |
| --- | --- |
| Phạm Gia Minh | B24DCKD057 |
| Phương Bảo Vỹ | B24DCKD105 |
| Nguyễn Đức Thành | B24DCKD085 |
| Nguyễn Mạnh Duy | B24DCKD024 |
| Phùng Quốc Khánh Nam | B24DCKD059 |

- `bao_cao/Bao_cao_De_8_Nhom_8.pdf`: báo cáo 12 trang để đọc và in.
- `bao_cao/Bao_cao_De_8_Nhom_8.docx`: bản chỉnh sửa của cùng báo cáo.
- `trinh_chieu/Bai_trinh_chieu_De_8_Nhom_8.pptx`: bài trình chiếu 10 trang, biểu đồ và chữ chỉnh sửa được.
- `phan_cong.csv`: phân công và tỷ lệ đóng góp **dự kiến**, có ô để nhóm ghi đóng góp thực tế và minh chứng. Nhóm cần xác nhận trước khi nộp.
- `scripts/analysis.py`, dữ liệu, bảng kết quả và biểu đồ: toàn bộ phân tích có thể chạy lại.

Mẫu chi tiết chưa có đủ bằng chứng khác biệt: Mann-Whitney p = 0,292037; Welch p = 0,859422. KTC 95% cho trung bình A trừ B là [-4,348620; 5,200927] ms. Trong 200 lần lặp mới, Mann-Whitney phát hiện 153/200 (76,5%) và Welch 99/200 (49,5%). Các kết quả này phân biệt với tính chất lý thuyết B dịch trái 4 ms của mô hình sinh.

Mã tạo Word `scripts/build_report.py` là phần bổ sung, cần `python-docx`. Sau khi đã có dữ liệu/kết quả, chạy `python scripts/build_report.py` để tạo lại Word. Chuyển Word sang PDF bằng Word hoặc LibreOffice; số trang có thể thay đổi nếu thay font hay cài đặt trang. Mã phân tích chính không phụ thuộc Word, PowerPoint hoặc bộ công cụ tạo slide.

## Đối chiếu yêu cầu

Đủ báo cáo 8–12 trang, slide 8–10 trang, dữ liệu mẫu, bảng 200 lần lặp, mã/seed/hướng dẫn và bảng phân công. Báo cáo có mục kiến thức nền chương 1–5. Nhóm có 5 thành viên; kế hoạch đề xuất trong 3 tuần được nêu trong báo cáo. Dữ liệu mô phỏng được ghi rõ; mọi kiểm định dùng 5%, KTC dùng 95%; ước lượng từ mẫu và điều kiện/giới hạn phương pháp được giải thích riêng.

## Tài liệu tham khảo

1. Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu do người học cung cấp, trang 1, 9 và 12.
2. [SciPy Mann-Whitney](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html).
3. [SciPy Welch t-test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html).
4. [NumPy SeedSequence](https://numpy.org/doc/stable/reference/random/parallel.html).
