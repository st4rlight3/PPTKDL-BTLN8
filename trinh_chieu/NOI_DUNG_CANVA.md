# Nội dung Canva cho đề 8 nhóm 8

Đây là nội dung hoàn chỉnh cho bài trình chiếu Canva gồm đúng **10 trang**, bao gồm bìa. Dữ liệu thống kê giữ nguyên từ phân tích seed **20261104**. Tất cả là **dữ liệu mô phỏng**, không phải số đo mạng thực tế. Điểm cần giữ rõ: **mẫu chi tiết chưa phát hiện khác biệt** bằng cả Mann–Whitney và Welch; **B thấp hơn 4 ms là đặc điểm của mô hình tạo dữ liệu**.

## Hướng thiết kế

- Khổ trình chiếu 16:9.
- Phong cách trực quan, hiện đại, sinh động theo chủ đề viễn thông.
- Nền midnight navy, đường truyền sợi quang và nút mạng cyan/teal. Bìa sáng nổi bật hơn. Nền nội dung dịu để bảo đảm tương phản chữ.
- Bảng màu: navy `#06152B`, chữ trắng `#F6FAFF`, chữ phụ `#B9CFE3`, cyan `#59D8F0`, teal `#27D5B2`.
- Font Arial hoặc font sans có đầy đủ dấu tiếng Việt. Tiêu đề lớn, ít nhóm chữ, tránh các ô giao diện trang trí dày đặc.
- Duy trì màu A cyan và B teal ở biểu đồ so sánh nhóm.
- Giữ chữ, bảng và biểu đồ có thể chỉnh sửa trong Canva khi công cụ hỗ trợ. Không dùng số giả để tạo hình đẹp.
- Ảnh nền có sẵn: `network_background.png` cho bìa và `network_background_quiet.png` cho các trang nội dung. Hai ảnh là minh họa AI, không phải số liệu hay ảnh đo mạng.

## Tài liệu nguồn và dữ liệu chung

- Đề bài: *Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên*, đề 8 trang 9, yêu cầu chung trang 1, sản phẩm nộp trang 12.
- Mã phân tích `analysis.py`, dữ liệu `sample_detail.csv`, bảng hạng `pooled_ranks.csv`, kết quả `summary.json`, bảng lặp `simulation_200.csv`.
- [SciPy Mann–Whitney](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html).
- [SciPy Welch với ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html).
- [NumPy SeedSequence và các luồng ngẫu nhiên](https://numpy.org/doc/stable/reference/random/parallel.html).

Mỗi phần dưới gồm nội dung hiển thị, hướng bố cục và ghi chú thuyết trình. Giữ các ghi chú ở phần notes của Canva, không đưa toàn bộ ghi chú lên trang trình chiếu.

## Slide 1 So sánh hai phương án định tuyến bằng dữ liệu độ trễ

**Bố cục:** Nền viễn thông nổi bật toàn khung. Tiêu đề trắng lớn ở bên trái, chi tiết sợi quang dồn dưới và bên phải.

**Nội dung trên slide**

HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG  
KHOA VIỄN THÔNG 1

**So sánh hai phương án định tuyến bằng dữ liệu độ trễ**

Đề 8  
Phương pháp thống kê dữ liệu  
Nhóm 8  
Giảng viên Vũ Quang Minh

**Ghi chú thuyết trình**

Báo cáo bài tập nhóm về so sánh hai mẫu độ trễ độc lập. Toàn bộ dữ liệu là mô phỏng theo mô hình đề bài, không phải số đo mạng thực tế. Nhóm 8 gồm Phạm Gia Minh B24DCKD057, Phương Bảo Vỹ B24DCKD105, Nguyễn Đức Thành B24DCKD085, Phan Nguyễn Trung Khánh B24DCKD041 và Phùng Quốc Khánh Nam B24DCKD059. Kết luận được phân biệt giữa mẫu phân tích chi tiết và đặc điểm thật của mô hình tạo dữ liệu.

## Slide 2 Thiết kế mô phỏng

**Bố cục:** Công thức A và B lớn ở trái, số 200 lớn ở phải. Dùng nền viễn thông dịu sáng để bảo đảm tương phản chữ.

**Nội dung trên slide**

Hai nhóm phiên truyền độc lập, mỗi nhóm 40 quan sát, đơn vị ms.

- A: X = 20 + Z
- B: Y = 16 + Z′
- Z và Z′ độc lập, phân phối mũ với trung bình 10 ms.
- Seed: 20261104.
- 200 lần sinh mẫu mới.
- Mann–Whitney và Welch hai phía, α = 0,05.
- Khoảng tin cậy 95%.

Lưu mẫu gốc, mã lệnh và kết quả để chạy lại.

**Ghi chú thuyết trình**

Chọn seed cố định trước khi chạy, không đổi seed để tìm một mẫu có ý nghĩa thống kê. SeedSequence tách luồng cho mẫu chi tiết và 200 lần mô phỏng, mỗi lần sinh mới 40 giá trị A và 40 giá trị B. Không tái sử dụng mẫu chi tiết trong bảng tỷ lệ phát hiện. Tham số 20, 16 và 10 chỉ định nghĩa mô hình tạo dữ liệu. Các trung bình, phương sai và sai số chuẩn trong phân tích được tính từ từng mẫu. Hướng dẫn chạy cùng phiên bản thư viện nằm trong README và requirements.txt.

**Nguồn phương pháp:** [numpy.org](https://numpy.org/doc/stable/reference/random/parallel.html).

## Slide 3 Thống kê mô tả và histogram

**Bố cục:** Bảng mô tả ở trái, histogram ở phải. Màu A cyan và B teal nhất quán.

**Nội dung trên slide**

Mẫu chi tiết có n = 40 mỗi nhóm. Histogram dùng cùng khoảng lớp.

| Đại lượng (ms) | A | B |
|---|---:|---:|
| Trung bình | 28,12 | 27,70 |
| Trung vị | 23,91 | 23,69 |
| Độ lệch chuẩn | 10,33 | 11,10 |
| Q1 | 22,01 | 19,12 |
| Q3 | 29,57 | 34,29 |
| IQR | 7,56 | 15,17 |

Cả hai mẫu lệch phải. Trung bình lớn hơn trung vị.

**Dữ liệu histogram**

| Khoảng lớp (ms) | Số phiên A | Số phiên B |
|---|---:|---:|
| [16, 24) | 20 | 20 |
| [24, 32) | 11 | 8 |
| [32, 40) | 3 | 7 |
| [40, 48) | 3 | 1 |
| [48, 56) | 2 | 4 |
| [56, 64) | 0 | 0 |
| [64, 72] | 1 | 0 |

Trục ngang: Độ trễ (ms). Trục dọc: Số phiên, từ 0 đến 25. Cột ghép A/B, cùng bề rộng lớp 8 ms. Tổng mỗi nhóm 40.

**Ghi chú thuyết trình**

Trung bình A 28,12 ms và B 27,70 ms gần nhau trong mẫu chi tiết này. Trung vị lần lượt 23,91 và 23,69 ms. Độ lệch chuẩn dùng mẫu số n−1. Q1 và Q3 dùng nội suy tuyến tính của NumPy, IQR bằng Q3−Q1. Histogram có bảy lớp chung bề rộng 8 ms, từ 16 đến 72 ms. Mỗi lớp đóng bên trái và mở bên phải, lớp cuối chứa cả cận phải. Hai phân phối có đuôi phải dài. IQR của B lớn hơn A trong mẫu không phủ định việc hai phân phối tạo dữ liệu có cùng dạng và độ phân tán thật.

## Slide 4 Biểu đồ hộp của hai phương án

**Bố cục:** Biểu đồ hộp lớn ở trái, diễn giải ngắn ở phải.

**Nội dung trên slide**

Hộp từ Q1 đến Q3. Vạch giữa là trung vị. Râu theo quy tắc 1,5 IQR.

- A: IQR = 7,56 ms.
- B: IQR = 15,17 ms.
- Các giá trị ngoài râu vẫn là dữ liệu hợp lệ của phân phối mũ.

Giữ toàn bộ 80 quan sát khi kiểm định.

Trục dọc: Độ trễ (ms), từ 10 đến 70. Trục ngang: hai phương án A và B. Không cắt mất các điểm ngoài râu.

**Dữ liệu chính xác để dựng biểu đồ hộp**

| Nhóm | Râu dưới | Q1 | Trung vị | Q3 | Râu trên |
|---|---:|---:|---:|---:|---:|
| A | 20.327426 | 22.012767 | 23.907064 | 29.574235 | 40.641566 |
| B | 16.527658 | 19.123197 | 23.687746 | 34.289325 | 53.661804 |

Các điểm ngoài râu (ms):

- A: 41.178137, 43.713961, 49.015069, 55.594845, 66.029757.
- B: không có.

**Ghi chú thuyết trình**

Q1 và Q3 dùng cùng quy ước nội suy tuyến tính với thống kê mô tả. Râu dưới kéo đến quan sát nhỏ nhất còn trong khoảng Q1−1,5IQR. Râu trên kéo đến quan sát lớn nhất còn trong khoảng Q3+1,5IQR. Các điểm ngoài râu được thể hiện riêng. Các điểm lớn không tự động là lỗi nhập liệu, vì mô hình mũ tạo ra những độ trễ lớn với xác suất dương. Cần giữ các điểm này khi thực hiện cả hai kiểm định. Đuôi phải dài làm trung bình và kiểm định dựa trên trung bình nhạy hơn với giá trị lớn.

## Slide 5 Mann–Whitney và cách xếp hạng

**Bố cục:** Giả thuyết, cách làm và công thức ở trái. Bảng minh họa sáu hạng ở phải.

**Nội dung trên slide**

Kiểm định Mann–Whitney hai phía cho hai mẫu độc lập.

- H₀: Hai phân phối như nhau.
- H₁: Hai phân phối khác nhau.
- Gộp 80 giá trị rồi xếp tăng dần.
- Hạng trùng nhận hạng trung bình.
- Mẫu hiện tại không có hạng trùng.

U(A) = R(A) − 40 × 41 / 2.

| Mã | Nhóm | Độ trễ (ms) | Hạng |
|---|:---:|---:|---:|
| B10 | B | 19,943 | 13 |
| B18 | B | 20,040 | 14 |
| B37 | B | 20,190 | 15 |
| A39 | A | 20,327 | 16 |
| A25 | A | 20,341 | 17 |
| A31 | A | 20,639 | 18 |

Bảng minh họa hạng 13 đến 18. Kiểm định dùng đủ 80 giá trị.

**Ghi chú thuyết trình**

Giả thuyết không là hai phân phối tổng thể giống nhau. Đối thuyết hai phía là các phân phối khác nhau theo cách kiểm định Mann–Whitney phát hiện. Khi hai phân phối cùng dạng và chỉ khác vị trí, có thể diễn giải kết quả theo dịch chuyển vị trí. Mann–Whitney không mặc nhiên kiểm định sự bằng nhau của trung bình. Gộp toàn bộ 80 giá trị, xếp hạng tăng dần, tính tổng hạng của mỗi nhóm. Nếu trùng giá trị, dùng midrank và hiệu chỉnh phương sai theo số lượng phần tử của từng nhóm trùng. Bảng chỉ minh họa sáu hạng nối tiếp. Toàn bộ bảng 80 hạng nằm trong pooled_ranks.csv.

**Nguồn phương pháp:** [docs.scipy.org](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html).

## Slide 6 Kết quả Mann–Whitney của mẫu chi tiết

**Bố cục:** P-value rất lớn bên trái, bảng thống kê ở phải. Ước lượng xác suất và kết luận ở dưới.

**Nội dung trên slide**

Xấp xỉ chuẩn, hiệu chỉnh liên tục và hiệu chỉnh hạng trùng.

**p = 0,292**

**Chưa bác bỏ H₀ ở mức 5%.**

| Thống kê | Giá trị |
|---|---:|
| Tổng hạng A / B | 1730 / 1510 |
| U(A) / U(B) | 910 / 690 |
| trị tuyệt đối z hiệu chỉnh | 1,054 |

P̂(A > B) = 910 / 1600 = 56,9%.

Đây là ước lượng từ mẫu. Mẫu chưa đủ bằng chứng về khác biệt. Chưa bác bỏ H₀ không chứng minh hai phương án tương đương.

**Ghi chú thuyết trình**

Tổng hạng A là 1730 và B là 1510. U_A bằng 1730−820 = 910, U_B bằng 1600−910 = 690. Tại H0, trung bình U bằng 800, phương sai bằng 10800 khi không có hạng trùng. Dùng hiệu chỉnh liên tục 0,5 cho p hai phía được |z| = 1,0537 và p = 0,2920. Không bác bỏ H0 vì p lớn hơn 0,05. Ước lượng xác suất một phiên A có độ trễ lớn hơn một phiên B ngẫu nhiên là U_A/(40×40) = 0,56875. Đây không phải bằng chứng đủ để xác nhận B tốt hơn ở mức 5% trong mẫu chi tiết. Giả thiết cùng dạng trong mô hình cho phép diễn giải theo vị trí, nhưng quyết định kiểm định vẫn dựa trên mẫu.

**Nguồn phương pháp:** [docs.scipy.org](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html).

## Slide 7 Welch kiểm định chênh lệch trung bình

**Bố cục:** Ước lượng chênh lệch lớn ở trái, t/df/p ở phải. Minh họa khoảng tin cậy bằng đoạn ngang và điểm ước lượng.

**Nội dung trên slide**

Welch kiểm định chênh lệch trung bình.

H₀: μA = μB.  
H₁: μA ≠ μB.

Chênh lệch trung bình ước lượng A − B = 0,426 ms.

- t = 0,178.
- df = 77,604.
- p = 0,859.

**KTC 95% [−4,349; 5,201] ms chứa 0.**

Welch xét trung bình và dùng phương sai mẫu. Mann–Whitney xét hạng. Cả hai đều chưa phát hiện khác biệt trong mẫu chi tiết này.

**Dữ liệu minh họa KTC**

Trục ngang −6 đến 6 ms, nhãn Chênh lệch trung bình A − B (ms). Đoạn ngang từ −4,348619909 đến 5,200927040, điểm trắng tại 0,426153566 và vạch tham chiếu 0. Không vẽ trục dọc mang ý nghĩa định lượng.

**Ghi chú thuyết trình**

Welch dùng sai số chuẩn căn của s_A²/40 + s_B²/40, với hai phương sai đều ước lượng từ mẫu. Không thay độ lệch chuẩn thật 10 ms của mô hình vào công thức. Sai số chuẩn là 2,3982 ms và bậc tự do Welch–Satterthwaite xấp xỉ 77,6038. P-value hai phía là 0,8594. Khoảng tin cậy 95% cho chênh lệch trung bình A−B chạy từ −4,3486 đến 5,2009 ms. Khoảng chứa 0 nên phù hợp với kết luận chưa bác bỏ. Welch không yêu cầu hai phương sai bằng nhau. Với dữ liệu lệch phải và n=40, xấp xỉ t vẫn cần thận trọng vì đuôi dài; mô phỏng lặp giúp đánh giá khả năng phát hiện trong đúng thiết kế này.

**Nguồn phương pháp:** [docs.scipy.org](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html).

## Slide 8 Tỷ lệ phát hiện qua 200 lần mô phỏng

**Bố cục:** Biểu đồ cột tỷ lệ ở trái, bảng đếm và KTC ở phải. Các cột dùng màu A/B theo tông của bộ slide, nhưng tên cột là hai kiểm định.

**Nội dung trên slide**

Mỗi lần tạo hai mẫu mới và chạy cả hai kiểm định hai phía tại α = 0,05.

| Kiểm định | Số lần phát hiện | Tỷ lệ phát hiện | KTC Wilson 95% |
|---|---:|---:|---:|
| Mann–Whitney | 153 / 200 | 76,5% | 70,2–81,8% |
| Welch | 99 / 200 | 49,5% | 42,6–56,4% |

Sai số Monte Carlo: 3,0 và 3,5 điểm phần trăm.

Ước lượng lực kiểm định trong mô hình này, không phải tỷ lệ bác bỏ sai.

**Dữ liệu biểu đồ cột:** Mann–Whitney = 0,765, Welch = 0,495. Trục dọc từ 0% đến 100%, hiển thị nhãn trên cột. Không nhập 76,5 nếu công cụ đang dùng định dạng phần trăm dựa trên 0–1.

**Ghi chú thuyết trình**

Mann–Whitney phát hiện 153 trong 200 lần, tỷ lệ 76,5%; Welch phát hiện 99 trong 200 lần, tỷ lệ 49,5%. Sai số Monte Carlo lần lượt khoảng 3,00 và 3,54 điểm phần trăm. Khoảng tin cậy Wilson 95% cho tỷ lệ phát hiện lần lượt 70,16–81,84% và 42,65–56,37%. Hai kiểm định chạy trên cùng bộ mẫu trong mỗi lần lặp để so sánh công bằng. Có 98 lần cùng phát hiện, 55 lần chỉ Mann–Whitney phát hiện, 1 lần chỉ Welch phát hiện và 46 lần cùng không phát hiện. Do mô hình thật có chênh lệch vị trí 4 ms, các tỷ lệ bác bỏ phản ánh lực kiểm định, không ước lượng sai lầm loại I. Kết quả không chứng minh Mann–Whitney luôn tốt hơn Welch trong mọi phân phối.

## Slide 9 Kiến thức nền và giới hạn kết luận

**Bố cục:** Bảng kiến thức nền ở trên. Phần giải thích thiết kế độc lập và giới hạn ở dưới.

**Nội dung trên slide**

Kết nối kiến thức chương 1–5 với kiểm định phi tham số ở chương 7.

| Kiến thức nền | Vai trò trong bài |
|---|---|
| Biến và mẫu độc lập | Độ trễ định lượng, hai nhóm phiên khác nhau |
| Biến ngẫu nhiên và phân phối | Phân phối mũ mô tả độ lệch phải |
| Thống kê mô tả | Trung bình, trung vị, SD, Q1, Q3 và IQR |
| Ước lượng và độ không chắc chắn | KTC Welch, SE Monte Carlo, KTC Wilson |

**Không ghép cặp:** Không có cùng phiên trước–sau. Ghép theo số thứ tự là tùy ý.

**Giới hạn áp dụng:** Mô phỏng n = 40, chỉ 200 lần lặp. Chưa có tải mạng, jitter hay mất gói.

**Ghi chú thuyết trình**

Kiến thức chương 1–5 cung cấp cơ sở nhận diện biến, thiết kế mẫu, phân phối xác suất, tóm tắt dữ liệu và ước lượng độ không chắc chắn. Nội dung chính của đề là kiểm định phi tham số, đối chiếu với Welch. Hai nhóm gồm những phiên khác nhau và độc lập, nên không có cặp tự nhiên như cùng phiên trước–sau. Ghép giá trị A_i với B_i theo số thứ tự tạo quan hệ tùy ý. Do đó không dùng t ghép cặp hoặc Wilcoxon hạng có dấu. Kết luận chỉ áp dụng trong mô hình tạo dữ liệu với phân phối mũ cùng scale 10, mức dịch 4 ms và cỡ mẫu 40. Chưa thể suy luận về chi phí định tuyến, năng lượng, độ mất gói, jitter, tải mạng hoặc hiệu năng thực tế.

## Slide 10 Kết luận và phân công nhóm

**Bố cục:** Kết luận ở trên, bảng nhóm ở dưới. Ưu tiên đủ tên và MSSV, không thu chữ quá nhỏ.

**Nội dung trên slide**

Nhóm 8. Giảng viên Vũ Quang Minh.

**B thấp hơn 4 ms trong mô hình tạo dữ liệu.**

Mẫu chi tiết chưa đủ bằng chứng khác biệt ở mức 5%. Mô phỏng lặp ghi nhận Mann–Whitney phát hiện thường xuyên hơn.

Phân công đề xuất 20% mỗi thành viên, nhóm xác nhận theo thực tế.

| Thành viên | MSSV | Nhiệm vụ đề xuất | Đóng góp dự kiến |
|---|---|---|---:|
| Phạm Gia Minh | B24DCKD057 | Thiết kế mô phỏng và quản lý dữ liệu gốc | 20% |
| Phương Bảo Vỹ | B24DCKD105 | Lập trình Mann–Whitney và kiểm tra bảng hạng | 20% |
| Nguyễn Đức Thành | B24DCKD085 | Phân tích Welch và khoảng tin cậy | 20% |
| Phan Nguyễn Trung Khánh | B24DCKD041 | Mô phỏng 200 lần và trực quan hóa | 20% |
| Phùng Quốc Khánh Nam | B24DCKD059 | Tổng hợp báo cáo và trình chiếu | 20% |

Nếu không đủ bề rộng cho cột Đóng góp dự kiến, giữ dòng “20% mỗi thành viên” phía trên và ba cột còn lại như bản bố cục tham chiếu. Không trình bày đóng góp đề xuất như xác nhận đã hoàn thành.

**Ghi chú thuyết trình**

Trong mô hình đề bài, B là phiên bản dịch trái 4 ms của A, vì vậy trung bình và trung vị thật đều thấp hơn 4 ms. Đây là đặc điểm của mô hình dùng để đánh giá phương pháp, không phải tham số được thay vào ước lượng mẫu. Mẫu chi tiết cố định seed chưa cho bằng chứng thống kê đủ mạnh bằng cả Mann–Whitney lẫn Welch. Mô phỏng 200 lần cho thấy Mann–Whitney phát hiện thường xuyên hơn trong thiết kế đang xét. Nếu chọn phương án chỉ theo độ trễ của mô hình này thì ưu tiên B. Để áp dụng thực tế cần dữ liệu đo độc lập, điều kiện mạng rõ ràng và ngưỡng cải thiện có ý nghĩa nghiệp vụ. Bảng phân công là đề xuất phân bổ đều 20%, nhóm cần xác nhận hoặc sửa theo công việc và đóng góp thực tế trước khi nộp.

## Lưu ý khi đưa vào Canva

Giữ đúng các dấu âm của khoảng tin cậy và phân biệt ms với phần trăm. Không biến “chưa bác bỏ” thành “hai phương án như nhau”. Không thay p-value của mẫu chi tiết bằng kết quả của 200 lần mô phỏng. Hạng trong bảng là hạng khi gộp đủ 80 giá trị, không phải hạng riêng của sáu dòng minh họa. Hệ số chuẩn hóa và độ lệch chuẩn dùng trong kiểm định đều ước lượng từ mẫu.

Các số trong ghi chú có độ chính xác cao hơn số trình bày. Việc làm tròn trên slide không thay đổi dữ liệu phân tích. Nền dùng cho nội dung cần giữ tối để chữ trắng và cyan đọc rõ.
