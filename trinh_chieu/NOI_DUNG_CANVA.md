# Nội dung Canva đề 8 nhóm 8

Bản thiết kế mới theo Taste Skill adaptation. Khổ 1600 × 900, 10 trang. Nền ivory `#F4F3EE`, near-black `#172326`, cobalt `#1946D2`, burnt orange `#D75D2A`. Heading Times New Roman, tracking 0. Body và toàn bộ số liệu Arial. Lề 80 px. Chỉ hai trang accent: trang 6 cobalt, trang 10 near-black. Không gradient, glow, nền mạng hay lưới card bo góc.

Tất cả dữ liệu là mô phỏng, seed 20261104. Mẫu chi tiết chưa phát hiện khác biệt ở mức 5%. Mức 4 ms là đặc điểm của mô hình tạo dữ liệu, không phải ước lượng được thay vào kết quả mẫu.

Nguồn nhập chính: `deck-canva.html`, chỉ có HTML/CSS tĩnh. Bản `preview.html` là xem trước tương tác riêng, không dùng để nhập. `deck-canva-assets.zip` chứa đúng nguồn tĩnh dưới tên `index.html`; không cần ảnh nền hay tài nguyên mạng ngoài.

## 01 So sánh hai phương án định tuyến

**Bố cục:** Bìa chữ Times New Roman lớn trên nền ivory, 40 phiên A cobalt và 40 phiên B orange.

**Chữ hiển thị**

- PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU
- ĐỀ 8  /  NHÓM 8
- So sánh hai / phương án định tuyến
- Dữ liệu độ trễ mô phỏng
- Mann–Whitney / và kiểm định t Welch
- A
- B
- phiên truyền độc lập
- Học viện Công nghệ Bưu chính Viễn thông / Khoa Viễn thông 1
- Giảng viên Vũ Quang Minh

**Ghi chú thuyết trình và nguồn**

Báo cáo bài tập nhóm về so sánh hai mẫu độ trễ độc lập. Toàn bộ dữ liệu là mô phỏng theo mô hình đề bài, không phải số đo mạng thực tế. Nhóm 8 gồm Phạm Gia Minh B24DCKD057, Phương Bảo Vỹ B24DCKD105, Nguyễn Đức Thành B24DCKD085, Phan Nguyễn Trung Khánh B24DCKD041 và Phùng Quốc Khánh Nam B24DCKD059. Kết luận được phân biệt giữa mẫu phân tích chi tiết và đặc điểm thật của mô hình tạo dữ liệu.

Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.

Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.

## 02 Hai mẫu độc lập

**Bố cục:** Hai cột mở A và B, công thức Arial và đường kẻ màu. Seed, số lần lặp, mức ý nghĩa ở một hàng cuối.

**Chữ hiển thị**

- PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU
- THIẾT KẾ MÔ PHỎNG
- Hai mẫu độc lập
- Mỗi quan sát là một phiên truyền. Đơn vị độ trễ là ms.
- PHƯƠNG ÁN A
- PHƯƠNG ÁN B
- X = 20 + Z
- Y = 16 + Z′
- 40 phiên
- 40 phiên
- Z và Z′ độc lập, cùng phân phối mũ với trung bình 10 ms.
- Seed 20261104
- 200 lần sinh mẫu mới
- α = 0,05     KTC 95%
- Dữ liệu mô phỏng. Seed 20261104.

**Ghi chú thuyết trình và nguồn**

Chọn seed cố định trước khi chạy, không đổi seed để tìm một mẫu có ý nghĩa thống kê. SeedSequence tách luồng cho mẫu chi tiết và 200 lần mô phỏng, mỗi lần sinh mới 40 giá trị A và 40 giá trị B. Không tái sử dụng mẫu chi tiết trong bảng tỷ lệ phát hiện. Tham số 20, 16 và 10 chỉ định nghĩa mô hình tạo dữ liệu. Các trung bình, phương sai và sai số chuẩn trong phân tích được tính từ từng mẫu. Hướng dẫn chạy cùng phiên bản thư viện nằm trong README và requirements.txt.

Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.

Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.

https://numpy.org/doc/stable/reference/random/parallel.html

## 03 Trung bình mẫu gần nhau

**Bố cục:** Bảng mô tả bên trái và histogram lớn bên phải, không khung card.

**Chữ hiển thị**

- PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU
- MẪU PHÂN TÍCH CHI TIẾT
- Trung bình mẫu gần nhau
- Cả hai mẫu lệch phải. Mỗi phương án có 40 quan sát.
- THỐNG KÊ  (ms)
- A
- B
- Trung bình
- 28,12
- 27,70
- Trung vị
- 23,91
- 23,69
- Độ lệch chuẩn
- 10,33
- 11,10
- Q1
- 22,01
- 19,12
- Q3
- 29,57
- 34,29
- IQR
- 7,56
- 15,17
- TẦN SỐ
- Độ trễ (ms)
- 16–24
- 24–32
- 32–40
- 40–48
- 48–56
- 56–64
- 64–72
- Độ lệch chuẩn mẫu dùng n−1. Q1 và Q3 theo nội suy tuyến tính.

Dữ liệu histogram theo các lớp 16–24, 24–32, 32–40, 40–48, 48–56, 56–64, 64–72 ms. A: 20, 11, 3, 3, 2, 0, 1. B: 20, 8, 7, 1, 4, 0, 0. Mỗi nhóm tổng 40.

**Ghi chú thuyết trình và nguồn**

Trung bình A 28,12 ms và B 27,70 ms gần nhau trong mẫu chi tiết này. Trung vị lần lượt 23,91 và 23,69 ms. Độ lệch chuẩn dùng mẫu số n−1. Q1 và Q3 dùng nội suy tuyến tính của NumPy, IQR bằng Q3−Q1. Histogram có bảy lớp chung bề rộng 8 ms, từ 16 đến 72 ms. Mỗi lớp đóng bên trái và mở bên phải, lớp cuối chứa cả cận phải. Hai phân phối có đuôi phải dài. IQR của B lớn hơn A trong mẫu không phủ định việc hai phân phối tạo dữ liệu có cùng dạng và độ phân tán thật.

Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.

Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.

## 04 Độ phân tán trong mẫu

**Bố cục:** Biểu đồ hộp rộng và IQR lớn theo màu nhóm.

**Chữ hiển thị**

- PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU
- PHÂN PHỐI ĐỘ TRỄ
- Độ phân tán trong mẫu
- Giữ các giá trị ngoài râu khi kiểm định. Chúng thuộc mô hình mũ.
- Độ trễ (ms)
- A
- B
- IQR
- 7,56
- A  /  ms
- 15,17
- B  /  ms
- Hộp: Q1 đến Q3. Vạch giữa: trung vị. Râu: quy tắc 1,5 IQR.

Hộp và râu tính từ toàn bộ `sample_detail.csv` cùng Q1/Q3 trong `summary.json`. Trục độ trễ 10–70 ms. A cobalt, B orange. Giữ toàn bộ các điểm ngoài râu.

**Ghi chú thuyết trình và nguồn**

Q1 và Q3 dùng cùng quy ước nội suy tuyến tính với thống kê mô tả. Râu dưới kéo đến quan sát nhỏ nhất còn trong khoảng Q1−1,5IQR. Râu trên kéo đến quan sát lớn nhất còn trong khoảng Q3+1,5IQR. Các điểm ngoài râu được thể hiện riêng. Các điểm lớn không tự động là lỗi nhập liệu, vì mô hình mũ tạo ra những độ trễ lớn với xác suất dương. Cần giữ các điểm này khi thực hiện cả hai kiểm định. Đuôi phải dài làm trung bình và kiểm định dựa trên trung bình nhạy hơn với giá trị lớn.

Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.

Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.

## 05 Xếp hạng 80 quan sát

**Bố cục:** Dải 80 marks xếp hạng và bảng minh họa sáu hạng.

**Chữ hiển thị**

- PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU
- MANN–WHITNEY
- Xếp hạng 80 quan sát
- Gộp hai mẫu, sắp tăng dần. Hạng trùng nhận hạng trung bình.
- H₀  Cùng phân phối / H₁  Phân phối khác nhau
- U(A) = R(A) − 40 × 41 / 2
- R(A) = 1730     R(B) = 1510
- Mã
- Nhóm
- ms
- Hạng
- B10
- B
- 19,943
- B18
- B
- 20,040
- B37
- B
- 20,190
- A39
- A
- 20,327
- A25
- A
- 20,341
- A31
- A
- 20,639
- Dải màu: A cobalt, B orange. Mẫu không có hạng trùng. Kiểm định dùng đủ 80 giá trị.

Dải màu gồm đúng 80 marks đọc từ `pooled_ranks.csv`, theo thứ tự tăng dần. Bảng chỉ minh họa hạng 13–18.

**Ghi chú thuyết trình và nguồn**

Giả thuyết không là hai phân phối tổng thể giống nhau. Đối thuyết hai phía là các phân phối khác nhau theo cách kiểm định Mann–Whitney phát hiện. Khi hai phân phối cùng dạng và chỉ khác vị trí, có thể diễn giải kết quả theo dịch chuyển vị trí. Mann–Whitney không mặc nhiên kiểm định sự bằng nhau của trung bình. Gộp toàn bộ 80 giá trị, xếp hạng tăng dần, tính tổng hạng của mỗi nhóm. Nếu trùng giá trị, dùng midrank và hiệu chỉnh phương sai theo số lượng phần tử của từng nhóm trùng. Bảng chỉ minh họa sáu hạng nối tiếp. Toàn bộ bảng 80 hạng nằm trong pooled_ranks.csv.

Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.

Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html

## 06 Mẫu chưa đủ bằng chứng về khác biệt

**Bố cục:** Trang accent cobalt với kết luận và p-value, chữ ivory.

**Chữ hiển thị**

- PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU
- KẾT QUẢ MANN–WHITNEY
- Mẫu chưa đủ bằng chứng / về khác biệt
- 0,292
- p-value hai phía
- U(A) = 910 / U(B) = 690
- P̂(A > B) = 56,9%
- Ở mức ý nghĩa 5%. Chưa bác bỏ H₀ không chứng minh hai phương án tương đương.
- Xấp xỉ chuẩn. Hiệu chỉnh liên tục. Kiểm định hai phía.

**Ghi chú thuyết trình và nguồn**

Tổng hạng A là 1730 và B là 1510. U_A bằng 1730−820 = 910, U_B bằng 1600−910 = 690. Tại H0, trung bình U bằng 800, phương sai bằng 10800 khi không có hạng trùng. Dùng hiệu chỉnh liên tục 0,5 cho p hai phía được |z| = 1,0537 và p = 0,2920. Không bác bỏ H0 vì p lớn hơn 0,05. Ước lượng xác suất một phiên A có độ trễ lớn hơn một phiên B ngẫu nhiên là U_A/(40×40) = 0,56875. Đây không phải bằng chứng đủ để xác nhận B tốt hơn ở mức 5% trong mẫu chi tiết. Giả thiết cùng dạng trong mô hình cho phép diễn giải theo vị trí, nhưng quyết định kiểm định vẫn dựa trên mẫu.

Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.

Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html

## 07 Chênh lệch trung bình

**Bố cục:** Khoảng tin cậy là hình dữ liệu chính, mốc 0 rõ.

**Chữ hiển thị**

- PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU
- KIỂM ĐỊNH t WELCH
- Chênh lệch trung bình
- Khoảng tin cậy 95% chứa 0.
- 0,426
- ms
- t = 0,178 / df = 77,604 / p = 0,859
- KTC 95%  [−4,349 ; 5,201] ms
- −6
- −4
- −2
- Chênh lệch A − B (ms). Welch xét trung bình, dùng phương sai ước lượng từ mẫu.

Đoạn KTC từ −4,348619909 đến 5,200927040 ms; điểm ước lượng tại 0,426153566 ms; trục −6 đến 6 ms.

**Ghi chú thuyết trình và nguồn**

Welch dùng sai số chuẩn căn của s_A²/40 + s_B²/40, với hai phương sai đều ước lượng từ mẫu. Không thay độ lệch chuẩn thật 10 ms của mô hình vào công thức. Sai số chuẩn là 2,3982 ms và bậc tự do Welch–Satterthwaite xấp xỉ 77,6038. P-value hai phía là 0,8594. Khoảng tin cậy 95% cho chênh lệch trung bình A−B chạy từ −4,3486 đến 5,2009 ms. Khoảng chứa 0 nên phù hợp với kết luận chưa bác bỏ. Welch không yêu cầu hai phương sai bằng nhau. Với dữ liệu lệch phải và n=40, xấp xỉ t vẫn cần thận trọng vì đuôi dài; mô phỏng lặp giúp đánh giá khả năng phát hiện trong đúng thiết kế này.

Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.

Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html

## 08 Khả năng phát hiện qua 200 lần lặp

**Bố cục:** Hai thanh ngang tỷ lệ, nhãn trực tiếp 76,5% và 49,5%.

**Chữ hiển thị**

- PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU
- MÔ PHỎNG LẶP
- Khả năng phát hiện / qua 200 lần lặp
- Lực kiểm định trong mô hình đề bài. Mỗi lần sinh hai mẫu mới.
- Mann–Whitney
- 153 / 200
- 76,5%
- KTC Wilson 95%  70,2–81,8%
- Welch
- 99 / 200
- 49,5%
- KTC Wilson 95%  42,6–56,4%
- α = 0,05. Sai số Monte Carlo: 3,0 và 3,5 điểm phần trăm. Không phải tỷ lệ bác bỏ sai.

Thanh ngang có tỷ lệ 0,765 và 0,495, số lần phát hiện 153 và 99 trên 200. KTC Wilson và sai số Monte Carlo giữ nguyên kết quả phân tích.

**Ghi chú thuyết trình và nguồn**

Mann–Whitney phát hiện 153 trong 200 lần, tỷ lệ 76,5%; Welch phát hiện 99 trong 200 lần, tỷ lệ 49,5%. Sai số Monte Carlo lần lượt khoảng 3,00 và 3,54 điểm phần trăm. Khoảng tin cậy Wilson 95% cho tỷ lệ phát hiện lần lượt 70,16–81,84% và 42,65–56,37%. Hai kiểm định chạy trên cùng bộ mẫu trong mỗi lần lặp để so sánh công bằng. Có 98 lần cùng phát hiện, 55 lần chỉ Mann–Whitney phát hiện, 1 lần chỉ Welch phát hiện và 46 lần cùng không phát hiện. Do mô hình thật có chênh lệch vị trí 4 ms, các tỷ lệ bác bỏ phản ánh lực kiểm định, không ước lượng sai lầm loại I. Kết quả không chứng minh Mann–Whitney luôn tốt hơn Welch trong mọi phân phối.

Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.

Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.

## 09 Mẫu độc lập và giới hạn rõ ràng

**Bố cục:** Thiết kế độc lập, vai trò kiến thức chương 1–5 và giới hạn theo hai vùng mở.

**Chữ hiển thị**

- PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU
- ĐIỀU KIỆN VÀ GIỚI HẠN
- Mẫu độc lập, / giới hạn rõ ràng
- Ghép Aᵢ với Bᵢ theo thứ tự / sẽ tạo cặp tùy ý.
- KIẾN THỨC CHƯƠNG 1–5
- Biến và mẫu
- Độ trễ định lượng, hai nhóm khác nhau.
- Phân phối
- Mũ và độ lệch phải của dữ liệu.
- Mô tả
- Trung bình, trung vị, SD và IQR.
- Ước lượng
- KTC Welch và sai số mô phỏng.
- Chỉ cho mô hình này
- Phân phối mũ cùng độ phân tán. /  / Chưa xét tải mạng, jitter, mất gói. /  / Không suy luận chi phí hoặc năng lượng.
- Dữ liệu độc lập. Không dùng kiểm định ghép cặp. n = 40 mỗi nhóm, 200 lần lặp.

**Ghi chú thuyết trình và nguồn**

Kiến thức chương 1–5 cung cấp cơ sở nhận diện biến, thiết kế mẫu, phân phối xác suất, tóm tắt dữ liệu và ước lượng độ không chắc chắn. Nội dung chính của đề là kiểm định phi tham số, đối chiếu với Welch. Hai nhóm gồm những phiên khác nhau và độc lập, nên không có cặp tự nhiên như cùng phiên trước–sau. Ghép giá trị A_i với B_i theo số thứ tự tạo quan hệ tùy ý. Do đó không dùng t ghép cặp hoặc Wilcoxon hạng có dấu. Kết luận chỉ áp dụng trong mô hình tạo dữ liệu với phân phối mũ cùng scale 10, mức dịch 4 ms và cỡ mẫu 40. Chưa thể suy luận về chi phí định tuyến, năng lượng, độ mất gói, jitter, tải mạng hoặc hiệu năng thực tế.

Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.

Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.

## 10 Kết luận và phân công nhóm

**Bố cục:** Trang accent near-black, kết luận trong mô hình và bảng đủ năm thành viên.

**Chữ hiển thị**

- PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU
- KẾT LUẬN  /  NHÓM 8
- Kết luận trong / phạm vi mô hình
- 4 ms
- B thấp hơn trong mô hình
- Ưu tiên B nếu chỉ xét độ trễ của mô hình. / Mẫu chi tiết chưa đủ bằng chứng ở mức 5%.
- Phân công đề xuất 20% mỗi thành viên. Nhóm xác nhận theo thực tế.
- THÀNH VIÊN
- MSSV
- NHIỆM VỤ ĐỀ XUẤT
- Phạm Gia Minh
- B24DCKD057
- Thiết kế và dữ liệu
- Phương Bảo Vỹ
- B24DCKD105
- Mann–Whitney và bảng hạng
- Nguyễn Đức Thành
- B24DCKD085
- Welch và khoảng tin cậy
- Phan Nguyễn Trung Khánh
- B24DCKD041
- Mô phỏng và trực quan hóa
- Phùng Quốc Khánh Nam
- B24DCKD059
- Báo cáo và trình chiếu
- Dữ liệu mô phỏng. Phân công là đề xuất cần xác nhận.

**Ghi chú thuyết trình và nguồn**

Trong mô hình đề bài, B là phiên bản dịch trái 4 ms của A, vì vậy trung bình và trung vị thật đều thấp hơn 4 ms. Đây là đặc điểm của mô hình dùng để đánh giá phương pháp, không phải tham số được thay vào ước lượng mẫu. Mẫu chi tiết cố định seed chưa cho bằng chứng thống kê đủ mạnh bằng cả Mann–Whitney lẫn Welch. Mô phỏng 200 lần cho thấy Mann–Whitney phát hiện thường xuyên hơn trong thiết kế đang xét. Nếu chọn phương án chỉ theo độ trễ của mô hình này thì ưu tiên B. Để áp dụng thực tế cần dữ liệu đo độc lập, điều kiện mạng rõ ràng và ngưỡng cải thiện có ý nghĩa nghiệp vụ. Bảng phân công là đề xuất phân bổ đều 20%, nhóm cần xác nhận hoặc sửa theo công việc và đóng góp thực tế trước khi nộp.

Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.

Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.

## Phân công đề xuất đầy đủ

| Thành viên | MSSV | Nhiệm vụ | Dự kiến |
|---|---|---|---:|
| Phạm Gia Minh | B24DCKD057 | Thiết kế mô phỏng và quản lý dữ liệu gốc | 20% |
| Phương Bảo Vỹ | B24DCKD105 | Lập trình Mann–Whitney và kiểm tra bảng hạng | 20% |
| Nguyễn Đức Thành | B24DCKD085 | Phân tích Welch và khoảng tin cậy | 20% |
| Phan Nguyễn Trung Khánh | B24DCKD041 | Mô phỏng 200 lần và trực quan hóa | 20% |
| Phùng Quốc Khánh Nam | B24DCKD059 | Tổng hợp báo cáo và trình chiếu | 20% |

Nhóm xác nhận hoặc chỉnh lại theo đóng góp thực tế trước khi nộp.

## Nguồn và kiểm tra

Đề 8 trang 9; yêu cầu chung trang 1 và sản phẩm nộp trang 12 của tài liệu đề bài. Phương pháp tham khảo [SciPy Mann–Whitney](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html), [SciPy Welch](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) và [NumPy SeedSequence](https://numpy.org/doc/stable/reference/random/parallel.html).

Áp dụng [Taste Skill](https://github.com/Leonxlnx/taste-skill) qua bản thích nghi cục bộ. Không chạy hay tuyên bố đã chạy CLI/Chrome checker của bộ upstream. Việc kiểm tra mã và việc xem ảnh trình duyệt được ghi nhận riêng.
