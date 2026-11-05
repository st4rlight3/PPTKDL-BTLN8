from pathlib import Path
import html,json
import argparse
_script_dir=Path(__file__).resolve().parent
_parser=argparse.ArgumentParser(description='Tạo nguồn HTML tĩnh 10 trang để nhập Canva')
_parser.add_argument('--repo-root',type=Path,default=_script_dir.parent)
_parser.add_argument('--output-dir',type=Path)
_args=_parser.parse_args()
R=_args.repo_root.resolve()
O=(_args.output_dir.resolve() if _args.output_dir else R/'trinh_chieu'/'nguon_canva')
O.mkdir(parents=True,exist_ok=True)
S=json.loads((R/'results/summary.json').read_text(encoding='utf8'))
N={'1': {'texts': ['01', 'HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG', 'KHOA VIỄN THÔNG 1', 'So sánh hai phương án', 'định tuyến bằng', 'dữ liệu độ trễ', 'Đề 8   Phương pháp thống kê dữ liệu', 'Nhóm 8', 'Giảng viên Vũ Quang Minh'], 'notes': ['Báo cáo bài tập nhóm về so sánh hai mẫu độ trễ độc lập. Toàn bộ dữ liệu là mô phỏng theo mô hình đề bài, không phải số đo mạng thực tế. Nhóm 8 gồm Phạm Gia Minh B24DCKD057, Phương Bảo Vỹ B24DCKD105, Nguyễn Đức Thành B24DCKD085, Phan Nguyễn Trung Khánh B24DCKD041 và Phùng Quốc Khánh Nam B24DCKD059. Kết luận được phân biệt giữa mẫu phân tích chi tiết và đặc điểm thật của mô hình tạo dữ liệu.', 'Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.', 'Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.']}, '2': {'texts': ['Thiết kế mô phỏng', 'Hai nhóm phiên truyền độc lập, mỗi nhóm 40 quan sát, đơn vị ms', '02', 'A   X = 20 + Z', 'B   Y = 16 + Z′', 'Z và Z′ độc lập, phân phối mũ', 'với trung bình 10 ms', 'Seed 20261104', 'Lưu mẫu gốc, mã lệnh và kết quả để chạy lại', '200', 'lần sinh mẫu mới', 'Mann–Whitney và Welch', 'hai phía, α = 0,05', 'Khoảng tin cậy 95%'], 'notes': ['Chọn seed cố định trước khi chạy, không đổi seed để tìm một mẫu có ý nghĩa thống kê. SeedSequence tách luồng cho mẫu chi tiết và 200 lần mô phỏng, mỗi lần sinh mới 40 giá trị A và 40 giá trị B. Không tái sử dụng mẫu chi tiết trong bảng tỷ lệ phát hiện. Tham số 20, 16 và 10 chỉ định nghĩa mô hình tạo dữ liệu. Các trung bình, phương sai và sai số chuẩn trong phân tích được tính từ từng mẫu. Hướng dẫn chạy cùng phiên bản thư viện nằm trong README và requirements.txt.', 'Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.', 'Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.', 'https://numpy.org/doc/stable/reference/random/parallel.html']}, '3': {'texts': ['Thống kê mô tả và histogram', 'Mẫu chi tiết có n = 40 mỗi nhóm, histogram dùng cùng khoảng lớp', '03', 'Đại lượng', 'A', 'B', 'Trung bình', '28,12', '27,70', 'Trung vị', '23,91', '23,69', 'Độ lệch chuẩn', '10,33', '11,10', 'Q1', '22,01', '19,12', 'Q3', '29,57', '34,29', 'IQR', '7,56', '15,17', 'Cả hai mẫu lệch phải. Trung bình lớn hơn trung vị.'], 'notes': ['Trung bình A 28,12 ms và B 27,70 ms gần nhau trong mẫu chi tiết này. Trung vị lần lượt 23,91 và 23,69 ms. Độ lệch chuẩn dùng mẫu số n−1. Q1 và Q3 dùng nội suy tuyến tính của NumPy, IQR bằng Q3−Q1. Histogram có bảy lớp chung bề rộng 8 ms, từ 16 đến 72 ms. Mỗi lớp đóng bên trái và mở bên phải, lớp cuối chứa cả cận phải. Hai phân phối có đuôi phải dài. IQR của B lớn hơn A trong mẫu không phủ định việc hai phân phối tạo dữ liệu có cùng dạng và độ phân tán thật.', 'Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.', 'Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.']}, '4': {'texts': ['Biểu đồ hộp của hai phương án', 'Hộp từ Q1 đến Q3, vạch giữa là trung vị, râu theo quy tắc 1,5 IQR', '04', 'A   IQR 7,56 ms', 'B   IQR 15,17 ms', 'Các giá trị ngoài râu', 'vẫn là dữ liệu hợp lệ', 'của phân phối mũ', 'Giữ toàn bộ 80 quan sát khi kiểm định'], 'notes': ['Q1 và Q3 dùng cùng quy ước nội suy tuyến tính với thống kê mô tả. Râu dưới kéo đến quan sát nhỏ nhất còn trong khoảng Q1−1,5IQR. Râu trên kéo đến quan sát lớn nhất còn trong khoảng Q3+1,5IQR. Các điểm ngoài râu được thể hiện riêng. Các điểm lớn không tự động là lỗi nhập liệu, vì mô hình mũ tạo ra những độ trễ lớn với xác suất dương. Cần giữ các điểm này khi thực hiện cả hai kiểm định. Đuôi phải dài làm trung bình và kiểm định dựa trên trung bình nhạy hơn với giá trị lớn.', 'Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.', 'Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.']}, '5': {'texts': ['Mann–Whitney và cách xếp hạng', 'Kiểm định hai phía cho hai mẫu độc lập', '05', 'H₀   Hai phân phối như nhau', 'H₁   Hai phân phối khác nhau', 'Gộp 80 giá trị rồi xếp tăng dần', 'Hạng trùng nhận hạng trung bình', 'Mẫu hiện tại không có hạng trùng', 'U(A) = R(A) − 40 × 41 / 2', 'Mã', 'Nhóm', 'ms', 'Hạng', 'B10', 'B', '19,943', '13', 'B18', 'B', '20,040', '14', 'B37', 'B', '20,190', '15', 'A39', 'A', '20,327', '16', 'A25', 'A', '20,341', '17', 'A31', 'A', '20,639', '18', 'Minh họa hạng 13 đến 18', 'Kiểm định dùng đủ 80 giá trị'], 'notes': ['Giả thuyết không là hai phân phối tổng thể giống nhau. Đối thuyết hai phía là các phân phối khác nhau theo cách kiểm định Mann–Whitney phát hiện. Khi hai phân phối cùng dạng và chỉ khác vị trí, có thể diễn giải kết quả theo dịch chuyển vị trí. Mann–Whitney không mặc nhiên kiểm định sự bằng nhau của trung bình. Gộp toàn bộ 80 giá trị, xếp hạng tăng dần, tính tổng hạng của mỗi nhóm. Nếu trùng giá trị, dùng midrank và hiệu chỉnh phương sai theo số lượng phần tử của từng nhóm trùng. Bảng chỉ minh họa sáu hạng nối tiếp. Toàn bộ bảng 80 hạng nằm trong pooled_ranks.csv.', 'Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.', 'Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.', 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html']}, '6': {'texts': ['Kết quả Mann–Whitney của mẫu chi tiết', 'Xấp xỉ chuẩn, hiệu chỉnh liên tục và hiệu chỉnh hạng trùng', '06', 'p = 0,292', 'Chưa bác bỏ H₀ ở mức 5%', 'Thống kê', 'Giá trị', 'Tổng hạng A / B', '1730 / 1510', 'U(A) / U(B)', '910 / 690', '|z| hiệu chỉnh', '1,054', 'P̂(A > B) = 910 / 1600 = 56,9%', 'Đây là ước lượng từ mẫu. Mẫu chưa đủ bằng chứng về khác biệt.', 'Chưa bác bỏ H₀ không chứng minh hai phương án tương đương.'], 'notes': ['Tổng hạng A là 1730 và B là 1510. U_A bằng 1730−820 = 910, U_B bằng 1600−910 = 690. Tại H0, trung bình U bằng 800, phương sai bằng 10800 khi không có hạng trùng. Dùng hiệu chỉnh liên tục 0,5 cho p hai phía được |z| = 1,0537 và p = 0,2920. Không bác bỏ H0 vì p lớn hơn 0,05. Ước lượng xác suất một phiên A có độ trễ lớn hơn một phiên B ngẫu nhiên là U_A/(40×40) = 0,56875. Đây không phải bằng chứng đủ để xác nhận B tốt hơn ở mức 5% trong mẫu chi tiết. Giả thiết cùng dạng trong mô hình cho phép diễn giải theo vị trí, nhưng quyết định kiểm định vẫn dựa trên mẫu.', 'Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.', 'Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.', 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html']}, '7': {'texts': ['Welch kiểm định chênh lệch trung bình', 'H₀  μA = μB     H₁  μA ≠ μB', '07', 'A − B = 0,426 ms', 't = 0,178', 'df = 77,604', 'p = 0,859', 'KTC 95% [−4,349 ; 5,201] ms chứa 0', 'Welch xét trung bình và dùng phương sai mẫu. Mann–Whitney xét hạng.', 'Cả hai đều chưa phát hiện khác biệt trong mẫu chi tiết này.'], 'notes': ['Welch dùng sai số chuẩn căn của s_A²/40 + s_B²/40, với hai phương sai đều ước lượng từ mẫu. Không thay độ lệch chuẩn thật 10 ms của mô hình vào công thức. Sai số chuẩn là 2,3982 ms và bậc tự do Welch–Satterthwaite xấp xỉ 77,6038. P-value hai phía là 0,8594. Khoảng tin cậy 95% cho chênh lệch trung bình A−B chạy từ −4,3486 đến 5,2009 ms. Khoảng chứa 0 nên phù hợp với kết luận chưa bác bỏ. Welch không yêu cầu hai phương sai bằng nhau. Với dữ liệu lệch phải và n=40, xấp xỉ t vẫn cần thận trọng vì đuôi dài; mô phỏng lặp giúp đánh giá khả năng phát hiện trong đúng thiết kế này.', 'Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.', 'Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.', 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html']}, '8': {'texts': ['Tỷ lệ phát hiện qua 200 lần mô phỏng', 'Mỗi lần tạo hai mẫu mới và chạy cả hai kiểm định hai phía tại α = 0,05', '08', 'Kiểm định', 'Phát hiện', 'KTC 95%', 'Mann–Whitney', '153 / 200', '70,2–81,8%', 'Welch', '99 / 200', '42,6–56,4%', 'Sai số Monte Carlo', '3,0 và 3,5 điểm phần trăm', 'Ước lượng lực kiểm định trong mô hình này, không phải tỷ lệ bác bỏ sai'], 'notes': ['Mann–Whitney phát hiện 153 trong 200 lần, tỷ lệ 76,5%; Welch phát hiện 99 trong 200 lần, tỷ lệ 49,5%. Sai số Monte Carlo lần lượt khoảng 3,00 và 3,54 điểm phần trăm. Khoảng tin cậy Wilson 95% cho tỷ lệ phát hiện lần lượt 70,16–81,84% và 42,65–56,37%. Hai kiểm định chạy trên cùng bộ mẫu trong mỗi lần lặp để so sánh công bằng. Có 98 lần cùng phát hiện, 55 lần chỉ Mann–Whitney phát hiện, 1 lần chỉ Welch phát hiện và 46 lần cùng không phát hiện. Do mô hình thật có chênh lệch vị trí 4 ms, các tỷ lệ bác bỏ phản ánh lực kiểm định, không ước lượng sai lầm loại I. Kết quả không chứng minh Mann–Whitney luôn tốt hơn Welch trong mọi phân phối.', 'Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.', 'Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.']}, '9': {'texts': ['Kiến thức nền và giới hạn kết luận', 'Kết nối kiến thức chương 1–5 với kiểm định phi tham số ở chương 7', '09', 'Kiến thức nền', 'Vai trò trong bài', 'Biến và mẫu độc lập', 'Độ trễ định lượng, hai nhóm phiên khác nhau', 'Biến ngẫu nhiên và phân phối', 'Phân phối mũ mô tả độ lệch phải', 'Thống kê mô tả', 'Trung bình, trung vị, SD, Q1, Q3 và IQR', 'Ước lượng và độ không chắc chắn', 'KTC Welch, SE Monte Carlo, KTC Wilson', 'Không ghép cặp', 'Không có cùng phiên trước–sau', 'Ghép theo số thứ tự là tùy ý', 'Giới hạn áp dụng', 'Mô phỏng n = 40, chỉ 200 lần lặp', 'Chưa có tải mạng, jitter hay mất gói'], 'notes': ['Kiến thức chương 1–5 cung cấp cơ sở nhận diện biến, thiết kế mẫu, phân phối xác suất, tóm tắt dữ liệu và ước lượng độ không chắc chắn. Nội dung chính của đề là kiểm định phi tham số, đối chiếu với Welch. Hai nhóm gồm những phiên khác nhau và độc lập, nên không có cặp tự nhiên như cùng phiên trước–sau. Ghép giá trị A_i với B_i theo số thứ tự tạo quan hệ tùy ý. Do đó không dùng t ghép cặp hoặc Wilcoxon hạng có dấu. Kết luận chỉ áp dụng trong mô hình tạo dữ liệu với phân phối mũ cùng scale 10, mức dịch 4 ms và cỡ mẫu 40. Chưa thể suy luận về chi phí định tuyến, năng lượng, độ mất gói, jitter, tải mạng hoặc hiệu năng thực tế.', 'Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.', 'Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.']}, '10': {'texts': ['Kết luận và phân công nhóm', 'Nhóm 8   Giảng viên Vũ Quang Minh', '10', 'B thấp hơn 4 ms trong mô hình tạo dữ liệu', 'Mẫu chi tiết chưa đủ bằng chứng khác biệt ở mức 5%.', 'Mô phỏng lặp ghi nhận Mann–Whitney phát hiện thường xuyên hơn.', 'Phân công đề xuất 20% mỗi thành viên, nhóm xác nhận theo thực tế', 'Thành viên', 'MSSV', 'Nhiệm vụ đề xuất', 'Phạm Gia Minh', 'B24DCKD057', 'Thiết kế mô phỏng, quản lý dữ liệu gốc', 'Phương Bảo Vỹ', 'B24DCKD105', 'Lập trình Mann–Whitney và kiểm tra hạng', 'Nguyễn Đức Thành', 'B24DCKD085', 'Welch và khoảng tin cậy', 'Phan Nguyễn Trung Khánh', 'B24DCKD041', 'Mô phỏng 200 lần và trực quan hóa', 'Phùng Quốc Khánh Nam', 'B24DCKD059', 'Tổng hợp báo cáo và trình chiếu'], 'notes': ['Trong mô hình đề bài, B là phiên bản dịch trái 4 ms của A, vì vậy trung bình và trung vị thật đều thấp hơn 4 ms. Đây là đặc điểm của mô hình dùng để đánh giá phương pháp, không phải tham số được thay vào ước lượng mẫu. Mẫu chi tiết cố định seed chưa cho bằng chứng thống kê đủ mạnh bằng cả Mann–Whitney lẫn Welch. Mô phỏng 200 lần cho thấy Mann–Whitney phát hiện thường xuyên hơn trong thiết kế đang xét. Nếu chọn phương án chỉ theo độ trễ của mô hình này thì ưu tiên B. Để áp dụng thực tế cần dữ liệu đo độc lập, điều kiện mạng rõ ràng và ngưỡng cải thiện có ý nghĩa nghiệp vụ. Bảng phân công là đề xuất phân bổ đều 20%, nhóm cần xác nhận hoặc sửa theo công việc và đóng góp thực tế trước khi nộp.', 'Nguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.', 'Dữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.']}}
INK='#172326';PAPER='#F4F3EE';BLUE='#1946D2';ORANGE='#D75D2A';MUTED='#58615F';RULE='#B4BCB8'
CSS='''*{box-sizing:border-box}html,body{margin:0;padding:0}html{background:#DDDFD8}body{font-family:Arial,sans-serif;color:#172326}.page{position:relative;width:1600px;height:900px;background:#F4F3EE;overflow:hidden;margin:0 auto 30px}.t{position:absolute;margin:0;white-space:pre-line;font-family:Arial,sans-serif;font-weight:400;line-height:1.25;font-variant-numeric:lining-nums tabular-nums}.serif{font-family:\"Times New Roman\",serif;font-weight:400;line-height:1.06;letter-spacing:0}.shape{position:absolute}.meta{letter-spacing:1.6px;font-size:19px;font-weight:700}.page.blue{background:#1946D2;color:#F4F3EE}.page.ink{background:#172326;color:#F4F3EE}@media print{html,body{background:none}.page{margin:0;break-after:page}}'''
def t(text,x,y,w,h,size=30,color=INK,serif=False,weight=400,align='left',line=1.25,extra=''):
 cls='t'+(' serif' if serif else '')
 return f'<div class="{cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;font-size:{size}px;color:{color};font-weight:{weight};text-align:{align};line-height:{line};{extra}">{html.escape(str(text))}</div>'
def rect(x,y,w,h,color):return f'<div class="shape" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color}"></div>'
def rule(y,color=RULE,x=80,w=1440,h=1):return rect(x,y,w,h,color)
def page(i,label,content,kind=''):
 notes='\n\n'.join(N[str(i)]['notes'])
 return f'<section class="page {kind}" data-document-role="page" data-label="{html.escape(str(i).zfill(2)+" "+label,quote=True)}" data-speaker-notes="{html.escape(notes,quote=True)}">{content}</section>'
def header(label,color=INK):
 return t('PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU',80,49,1000,28,19,color,weight=700,extra='letter-spacing:1.6px')+t(label,1160,49,360,28,19,color,align='right')+rule(100,color)
def footer(i,source='Dữ liệu mô phỏng. Seed 20261104.',color=MUTED):return rule(820,RULE)+t(source,80,843,1350,27,19,color)+t(f'{i:02}',1440,836,80,40,28,color,align='right')
P=[]
p=header('ĐỀ 8  /  NHÓM 8')
p+=t('So sánh hai\nphương án định tuyến',80,169,1400,266,106,serif=True,line=1.05)
p+=t('Dữ liệu độ trễ mô phỏng',85,477,1000,52,38,MUTED)
p+=t('Mann–Whitney\nvà kiểm định t Welch',85,587,800,100,34,line=1.3)
p+=t('A',1040,548,180,40,25,BLUE,weight=700)+t('40',1032,581,230,117,106,BLUE,weight=700,line=1)
p+=t('B',1300,548,180,40,25,ORANGE,weight=700)+t('40',1292,581,230,117,106,ORANGE,weight=700,line=1)
p+=t('phiên truyền độc lập',1038,708,470,40,27,MUTED)
p+=rule(773)+t('Học viện Công nghệ Bưu chính Viễn thông\nKhoa Viễn thông 1',80,800,920,64,22,MUTED,line=1.4)+t('Giảng viên Vũ Quang Minh',1040,818,480,42,24,align='right')
P.append(page(1,'So sánh hai phương án định tuyến',p))
p=header('THIẾT KẾ MÔ PHỎNG')+t('Hai mẫu độc lập',80,145,1440,100,82,serif=True)
p+=t('Mỗi quan sát là một phiên truyền. Đơn vị độ trễ là ms.',84,262,1400,46,32,MUTED)
p+=rect(80,355,660,4,BLUE)+rect(860,355,660,4,ORANGE)
p+=t('PHƯƠNG ÁN A',80,384,660,34,22,BLUE,weight=700,extra='letter-spacing:1.4px')+t('PHƯƠNG ÁN B',860,384,660,34,22,ORANGE,weight=700,extra='letter-spacing:1.4px')
p+=t('X = 20 + Z',80,444,660,90,64)+t('Y = 16 + Z′',860,444,660,90,64)
p+=t('40 phiên',84,557,660,45,34,weight=700)+t('40 phiên',864,557,660,45,34,weight=700)
p+=t('Z và Z′ độc lập, cùng phân phối mũ với trung bình 10 ms.',84,642,1420,46,32,MUTED)
p+=rule(722)+t('Seed 20261104',80,750,520,42,28,weight=700)+t('200 lần sinh mẫu mới',600,750,480,42,28,weight=700)+t('α = 0,05     KTC 95%',1120,750,400,42,28,align='right')
p+=footer(2)
P.append(page(2,'Hai mẫu độc lập',p))
def save(pages):
 doc='<!doctype html><html lang="vi" data-type="product"><head><meta charset="utf-8"><meta name="page-type" content="product"><meta name="site-kind" content="tech"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Đề 8 Nhóm 8 — So sánh độ trễ</title><style>'+CSS+'</style></head><body>'+''.join(pages)+'</body></html>'
 (O/'deck-canva.html').write_text(doc,encoding='utf8')
 # The import document always contains ten pages.
 return doc

# The remaining eight pages use the same artboard and type system.
import csv,math,zipfile
raw=list(csv.DictReader((R/'data/sample_detail.csv').open(encoding='utf-8-sig')))
ranks=list(csv.DictReader((R/'data/pooled_ranks.csv').open(encoding='utf-8-sig')))
A,B=S['descriptive'];D=S['detail_tests']
a=[float(x['latency_ms']) for x in raw if x['group']=='A'];b=[float(x['latency_ms']) for x in raw if x['group']=='B']
def f(v,k=2):return f'{v:.{k}f}'.replace('.',',')
def dot(x,y,r,col):return f'<div class="shape" style="left:{x-r}px;top:{y-r}px;width:{r*2}px;height:{r*2}px;border-radius:50%;background:{col}"></div>'
def hline(x1,x2,y,col=RULE,width=1):return rect(min(x1,x2),y-width/2,abs(x2-x1),width,col)
def vline(x,y1,y2,col=RULE,width=1):return rect(x-width/2,min(y1,y2),width,abs(y2-y1),col)
def outline(x,y,w,h,col,width=3):return rect(x,y,w,width,col)+rect(x,y+h-width,w,width,col)+rect(x,y,width,h,col)+rect(x+w-width,y,width,h,col)
def label(text,x,y,w,h=32,size=22,col=INK,weight=400,align='center'):
 return t(text,x,y,w,h,size,col,weight=weight,align=align)
# 3 Descriptive statistics and observed frequency distribution.
p=header('MẪU PHÂN TÍCH CHI TIẾT')+t('Trung bình mẫu gần nhau',80,145,1440,105,82,serif=True)
p+=t('Cả hai mẫu lệch phải. Mỗi phương án có 40 quan sát.',84,266,1436,45,31,MUTED)
p+=t('THỐNG KÊ  (ms)',80,342,400,32,20,MUTED,weight=700,extra='letter-spacing:1.2px')+t('A',390,342,100,40,26,BLUE,weight=700,align='right')+t('B',570,342,100,40,26,ORANGE,weight=700,align='right')+hline(80,670,396)
for i,(name,key) in enumerate([('Trung bình','mean_ms'),('Trung vị','median_ms'),('Độ lệch chuẩn','sd_ms'),('Q1','q1_ms'),('Q3','q3_ms'),('IQR','iqr_ms')]):
 yy=424+i*58;p+=t(name,80,yy,300,42,27)+t(f(A[key]),380,yy-2,110,46,31,BLUE,weight=700,align='right')+t(f(B[key]),550,yy-2,120,46,31,ORANGE,weight=700,align='right')
 if i<5:p+=hline(80,670,yy+45,'#D8DCD5')
left,right,top,bottom=790,1500,383,718
Y=lambda v:bottom-v/25*(bottom-top)
p+=t('TẦN SỐ',730,342,300,32,20,MUTED,weight=700,extra='letter-spacing:1.2px')+t('Độ trễ (ms)',1230,342,270,32,22,MUTED,align='right')
for v in range(0,26,5):p+=hline(left,right,Y(v),'#D8DCD5')+label(str(v),733,Y(v)-14,45,28,20,MUTED,align='right')
p+=vline(left,top,bottom)+hline(left,right,bottom)
edges=[16,24,32,40,48,56,64,72]
counts=lambda vals:[sum(lo<=v<(edges[i+1]) or (i==6 and v==72) for v in vals) for i,lo in enumerate(edges[:-1])]
ca,cb=counts(a),counts(b);bw=(right-left)/7
for i in range(7):
 cx=left+(i+.5)*bw
 for j,(co,col) in enumerate([(ca,BLUE),(cb,ORANGE)]):
  if co[i]:p+=rect(cx-35+j*35,Y(co[i]),32,bottom-Y(co[i]),col)
 p+=label(f'{edges[i]}–{edges[i+1]}',cx-bw/2,738,bw,32,20,MUTED)
p+=footer(3,'Độ lệch chuẩn mẫu dùng n−1. Q1 và Q3 theo nội suy tuyến tính.')
P.append(page(3,'Trung bình mẫu gần nhau',p))
# 4 Wide boxplots and observed dispersion.
p=header('PHÂN PHỐI ĐỘ TRỄ')+t('Độ phân tán trong mẫu',80,145,1440,108,82,serif=True)
p+=t('Giữ các giá trị ngoài râu khi kiểm định. Chúng thuộc mô hình mũ.',84,267,1410,44,31,MUTED)
left,right,top,bottom=170,1070,365,737;Y=lambda v:bottom-(v-10)/60*(bottom-top)
p+=t('Độ trễ (ms)',80,334,400,30,22,MUTED)
for v in range(10,71,10):p+=hline(left,right,Y(v),'#D8DCD5')+label(str(v),104,Y(v)-13,50,28,20,MUTED,align='right')
p+=vline(left,top,bottom)+hline(left,right,bottom)
for vals,d,x,col in [(a,A,445,BLUE),(b,B,805,ORANGE)]:
 lo=d['q1_ms']-1.5*d['iqr_ms'];hi=d['q3_ms']+1.5*d['iqr_ms'];inside=[v for v in vals if lo<=v<=hi];low,high=min(inside),max(inside)
 p+=vline(x,Y(low),Y(d['q1_ms']),col,3)+vline(x,Y(d['q3_ms']),Y(high),col,3)+hline(x-26,x+26,Y(low),col,3)+hline(x-26,x+26,Y(high),col,3)
 p+=outline(x-53,Y(d['q3_ms']),106,Y(d['q1_ms'])-Y(d['q3_ms']),col,3)+hline(x-53,x+53,Y(d['median_ms']),INK,4)
 for v in vals:
  if v<lo or v>hi:p+=dot(x,Y(v),5,col)
 p+=label(d['group'],x-55,756,110,38,28,col,700)
p+=t('IQR',1180,365,340,35,22,MUTED,weight=700,extra='letter-spacing:1.4px')+t('7,56',1170,412,350,102,82,BLUE,weight=700,line=1)+t('A  /  ms',1180,521,340,34,24,MUTED)
p+=t('15,17',1170,609,350,102,82,ORANGE,weight=700,line=1)+t('B  /  ms',1180,718,340,34,24,MUTED)
p+=footer(4,'Hộp: Q1 đến Q3. Vạch giữa: trung vị. Râu: quy tắc 1,5 IQR.')
P.append(page(4,'Độ phân tán trong mẫu',p))
# 5 Rank strip with exactly 80 ordered observations.
p=header('MANN–WHITNEY')+t('Xếp hạng 80 quan sát',80,145,1440,105,82,serif=True)
p+=t('Gộp hai mẫu, sắp tăng dần. Hạng trùng nhận hạng trung bình.',84,266,1420,45,31,MUTED)
for i,r in enumerate(ranks):p+=rect(80+i*18,350,16,38,BLUE if r['group']=='A' else ORANGE)
for rank in [1,20,40,60,80]:p+=label(str(rank),80+(rank-.5)*18-30,405,60,30,20,MUTED)
p+=t('H₀  Cùng phân phối\nH₁  Phân phối khác nhau',80,492,680,105,33,line=1.45)
p+=t('U(A) = R(A) − 40 × 41 / 2',80,651,750,61,39,weight=700)
p+=t('R(A) = 1730     R(B) = 1510',80,742,720,39,27,MUTED)
xs=[900,1065,1190,1390];ws=[140,100,170,130]
for x,w,te in zip(xs,ws,['Mã','Nhóm','ms','Hạng']):p+=label(te,x,484,w,32,22,MUTED,700,align='left' if x==900 else 'right')
p+=hline(900,1520,528)
for i,r in enumerate(ranks[12:18]):
 yy=547+i*39
 for j,val in enumerate([r['observation_id'],r['group'],f(float(r['latency_ms']),3),r['rank']]):p+=label(val,xs[j],yy,ws[j],34,25,INK,align='left' if j==0 else 'right')
p+=footer(5,'Dải màu: A cobalt, B orange. Mẫu không có hạng trùng. Kiểm định dùng đủ 80 giá trị.')
P.append(page(5,'Xếp hạng 80 quan sát',p))
# 6 One cobalt conclusion page.
p=header('KẾT QUẢ MANN–WHITNEY',PAPER)+t('Mẫu chưa đủ bằng chứng\nvề khác biệt',80,148,1440,217,84,PAPER,serif=True,line=1.1)
p+=t('0,292',76,443,800,173,152,PAPER,weight=700,line=1)+t('p-value hai phía',84,636,760,42,29,'#DEE5FA')
p+=t('U(A) = 910\nU(B) = 690',1040,450,480,100,34,PAPER,line=1.5)+t('P̂(A > B) = 56,9%',1040,635,480,46,30,PAPER)
p+=t('Ở mức ý nghĩa 5%. Chưa bác bỏ H₀ không chứng minh hai phương án tương đương.',84,741,1436,51,29,PAPER)
p+=footer(6,'Xấp xỉ chuẩn. Hiệu chỉnh liên tục. Kiểm định hai phía.','#DEE5FA')
P.append(page(6,'Mẫu chưa đủ bằng chứng về khác biệt',p,'blue'))
# 7 A single, dominant confidence interval.
p=header('KIỂM ĐỊNH t WELCH')+t('Chênh lệch trung bình',80,145,1440,105,82,serif=True)
p+=t('Khoảng tin cậy 95% chứa 0.',84,266,1436,45,31,MUTED)
p+=t('0,426',76,342,760,150,130,INK,weight=700,line=1)+t('ms',532,427,160,50,37,MUTED)
p+=t('t = 0,178\ndf = 77,604\np = 0,859',1150,350,370,139,31,MUTED,line=1.5)
p+=t('KTC 95%  [−4,349 ; 5,201] ms',84,525,1436,46,31,weight=700)
X=lambda v:160+(v+6)/12*1260
for tick in range(-6,7,2):
 p+=vline(X(tick),618,722,'#D8DCD5')+label(str(tick).replace('-','−'),X(tick)-40,739,80,33,22,MUTED)
p+=hline(160,1420,722)+vline(X(0),602,716,INK,2)
p+=hline(X(D['mean_difference_ci95_low_ms']),X(D['mean_difference_ci95_high_ms']),650,BLUE,7)
p+=vline(X(D['mean_difference_ci95_low_ms']),630,670,BLUE,3)+vline(X(D['mean_difference_ci95_high_ms']),630,670,BLUE,3)+dot(X(D['mean_difference_a_minus_b_ms']),650,11,INK)
p+=footer(7,'Chênh lệch A − B (ms). Welch xét trung bình, dùng phương sai ước lượng từ mẫu.')
P.append(page(7,'Chênh lệch trung bình',p))
# 8 Monte Carlo comparison with long proportional bars.
p=header('MÔ PHỎNG LẶP')+t('Khả năng phát hiện\nqua 200 lần lặp',80,142,1440,190,80,serif=True,line=1.08)
p+=t('Lực kiểm định trong mô hình đề bài. Mỗi lần sinh hai mẫu mới.',84,346,1436,43,29,MUTED)
for yy,name,count,rate,col,ci in [(457,'Mann–Whitney',153,.765,BLUE,'KTC Wilson 95%  70,2–81,8%'),(668,'Welch',99,.495,ORANGE,'KTC Wilson 95%  42,6–56,4%')]:
 p+=t(name,80,yy-54,1000,43,30,weight=700)+rect(80,yy,1100,54,'#DFE3DC')+rect(80,yy,1100*rate,54,col)
 p+=t(f'{count} / 200',1010,yy+9,170,38,27,INK,align='right')+t(f(rate*100,1)+'%',1250,yy-22,270,101,76,col,weight=700,line=1)
 p+=t(ci,80,yy+74,1080,35,24,MUTED)
p+=footer(8,'α = 0,05. Sai số Monte Carlo: 3,0 và 3,5 điểm phần trăm. Không phải tỷ lệ bác bỏ sai.')
P.append(page(8,'Khả năng phát hiện qua 200 lần lặp',p))
# 9 Independent design, foundations and limits.
p=header('ĐIỀU KIỆN VÀ GIỚI HẠN')+t('Mẫu độc lập,\ngiới hạn rõ ràng',80,143,900,187,80,serif=True,line=1.08)
p+=t('Ghép Aᵢ với Bᵢ theo thứ tự\nsẽ tạo cặp tùy ý.',1020,181,500,130,35,line=1.4)
p+=rule(394)+t('KIẾN THỨC CHƯƠNG 1–5',80,428,900,34,21,MUTED,weight=700,extra='letter-spacing:1.2px')
rows=[('Biến và mẫu','Độ trễ định lượng, hai nhóm khác nhau.'),('Phân phối','Mũ và độ lệch phải của dữ liệu.'),('Mô tả','Trung bình, trung vị, SD và IQR.'),('Ước lượng','KTC Welch và sai số mô phỏng.')]
for i,(le,ri) in enumerate(rows):
 yy=494+i*72;p+=t(le,80,yy,300,42,28,weight=700)+t(ri,390,yy+2,580,42,26,MUTED)
 if i<3:p+=hline(80,970,yy+53,'#D8DCD5')
p+=t('Chỉ cho mô hình này',1070,481,450,52,32,weight=700)+t('Phân phối mũ cùng độ phân tán.\n\nChưa xét tải mạng, jitter, mất gói.\n\nKhông suy luận chi phí hoặc năng lượng.',1070,553,450,235,27,MUTED,line=1.35)
p+=footer(9,'Dữ liệu độc lập. Không dùng kiểm định ghép cặp. n = 40 mỗi nhóm, 200 lần lặp.')
P.append(page(9,'Mẫu độc lập và giới hạn rõ ràng',p))
# 10 Restrained dark closing page, full verified identities.
p=header('KẾT LUẬN  /  NHÓM 8',PAPER)+t('Kết luận trong\nphạm vi mô hình',80,138,1050,181,76,PAPER,serif=True,line=1.08)
p+=t('4 ms',1120,151,400,132,112,PAPER,weight=700,line=1)+t('B thấp hơn trong mô hình',1124,299,396,39,26,'#C6D0CB')
p+=t('Ưu tiên B nếu chỉ xét độ trễ của mô hình.\nMẫu chi tiết chưa đủ bằng chứng ở mức 5%.',84,357,1436,93,30,PAPER,line=1.4)
p+=t('Phân công đề xuất 20% mỗi thành viên. Nhóm xác nhận theo thực tế.',84,470,1436,36,24,'#C6D0CB')
xs=[80,620,940];ws=[520,270,580]
for x,w,tx in zip(xs,ws,['THÀNH VIÊN','MSSV','NHIỆM VỤ ĐỀ XUẤT']):p+=t(tx,x,529,w,32,20,'#C6D0CB',weight=700,extra='letter-spacing:1.1px')
p+=hline(80,1520,573,'#61716A')
team=[('Phạm Gia Minh','B24DCKD057','Thiết kế và dữ liệu'),('Phương Bảo Vỹ','B24DCKD105','Mann–Whitney và bảng hạng'),('Nguyễn Đức Thành','B24DCKD085','Welch và khoảng tin cậy'),('Phan Nguyễn Trung Khánh','B24DCKD041','Mô phỏng và trực quan hóa'),('Phùng Quốc Khánh Nam','B24DCKD059','Báo cáo và trình chiếu')]
for i,row in enumerate(team):
 yy=589+i*43
 for x,w,tx in zip(xs,ws,row):p+=t(tx,x,yy,w,38,26,PAPER)
p+=footer(10,'Dữ liệu mô phỏng. Phân công là đề xuất cần xác nhận.','#C6D0CB')
P.append(page(10,'Kết luận và phân công nhóm',p,'ink'))

save(P)
# Retain the builder for the remaining pages.
print('Created all 10 editorial artboards')

import re
p=O/'deck-canva.html'
s=p.read_text(encoding='utf8')
s=re.sub(r' data-(?:document-role|label|speaker-notes)="[^"]*"','',s)
s=s.replace('</style>','''body{background:#DDE0DA}.page{display:none;position:absolute;left:0;top:0;margin:0;transform-origin:top left}.page.active{display:block}#stage{position:relative;margin:24px auto}.toolbar{height:58px;padding:0 24px;display:flex;align-items:center;justify-content:space-between;font:16px Arial,sans-serif;border-bottom:1px solid #BAC2BB}.toolbar button{font:16px Arial,sans-serif;padding:9px 14px;min-height:44px;min-width:68px;border:1px solid #172326;background:#F4F3EE;color:#172326;cursor:pointer}.toolbar button:hover{background:#E8EBE2}.toolbar button:focus-visible{outline:3px solid #1946D2;outline-offset:3px}.toolbar button:disabled{opacity:.4;cursor:default}@media(max-width:480px){.toolbar{padding:0 12px;gap:8px}.toolbar strong{font-size:14px}.toolbar button{min-width:60px;padding:8px 10px}}@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}</style>''')
s=s.replace('<body>','<body><nav class="toolbar" aria-label="Điều khiển trình chiếu"><strong>Đề 8 · Nhóm 8</strong><span><button id="prev" type="button">Trước</button> <span id="page-status" aria-live="polite"></span> <button id="next" type="button">Tiếp</button></span></nav><main id="stage">')
s=s.replace('</body>','''</main><script>
const pages=[...document.querySelectorAll('.page')];let current=0;
function fit(){const scale=Math.max(.1,Math.min((innerWidth-48)/1600,(innerHeight-110)/900,1));const stage=document.getElementById('stage');stage.style.width=1600*scale+'px';stage.style.height=900*scale+'px';pages.forEach(p=>p.style.transform='scale('+scale+')');}
function show(n){current=Math.max(0,Math.min(pages.length-1,n));pages.forEach((p,i)=>p.classList.toggle('active',i===current));document.getElementById('page-status').textContent=' '+(current+1)+' / '+pages.length+' ';document.getElementById('prev').disabled=current===0;document.getElementById('next').disabled=current===pages.length-1;fit();}
document.getElementById('prev').onclick=()=>show(current-1);document.getElementById('next').onclick=()=>show(current+1);addEventListener('keydown',e=>{if(e.key==='ArrowRight')show(current+1);if(e.key==='ArrowLeft')show(current-1);});addEventListener('resize',fit);show(0);
</script></body>''')
(O/'preview.html').write_text(s,encoding='utf8')
print('Preview created')

from zipfile import ZipFile,ZIP_DEFLATED
with ZipFile(O/'deck-canva-assets.zip','w',ZIP_DEFLATED) as package:
 package.write(O/'deck-canva.html','index.html')
print('Canva HTML source:',O/'deck-canva.html')
print('Canva ZIP:',O/'deck-canva-assets.zip')
