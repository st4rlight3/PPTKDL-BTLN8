"""Tạo báo cáo Word từ các CSV/JSON đã tính. Chạy từ bất kỳ thư mục nào."""
from pathlib import Path
import json, csv
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
S = json.loads((ROOT/'results/summary.json').read_text(encoding='utf-8'))
T = S['detail_tests']; A,B = S['descriptive']; MC=S['simulation_summary']
MEMBERS = [('Phạm Gia Minh','B24DCKD057'),('Phương Bảo Vỹ','B24DCKD105'),
 ('Nguyễn Đức Thành','B24DCKD085'),('Nguyễn Mạnh Duy','B24DCKD024'),
 ('Phùng Quốc Khánh Nam','B24DCKD059')]
TASKS = ['Thiết kế mô phỏng và quản lý dữ liệu gốc',
 'Lập trình Mann–Whitney và kiểm tra bảng hạng',
 'Phân tích Welch và khoảng tin cậy',
 'Mô phỏng 200 lần và trực quan hóa',
 'Tổng hợp báo cáo và trình chiếu']
def f(x,d=3): return f'{x:.{d}f}'.replace('.',',')
def pc(x,d=1): return f(100*x,d)+'%'
doc=Document(); sec=doc.sections[0]
sec.page_width=Inches(8.5);sec.page_height=Inches(11)
sec.top_margin=Inches(.77);sec.bottom_margin=Inches(.72)
sec.left_margin=Inches(.88);sec.right_margin=Inches(.78)
sec.header_distance=Inches(.3);sec.footer_distance=Inches(.3)
for sn in ['Normal','Title','Subtitle','Heading 1','Heading 2','Caption']:
 st=doc.styles[sn];st.font.name='Times New Roman';st.font.color.rgb=RGBColor(0,0,0)
 st._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),'Times New Roman')
normal=doc.styles['Normal'];normal.font.size=Pt(12)
normal.paragraph_format.line_spacing=1.14
normal.paragraph_format.space_after=Pt(7)
for sn,size in [('Title',24),('Heading 1',17),('Heading 2',13),('Caption',10)]:
 doc.styles[sn].font.size=Pt(size)
doc.styles['Heading 1'].paragraph_format.space_after=Pt(12)
doc.styles['Heading 2'].paragraph_format.space_before=Pt(9)
doc.styles['Heading 2'].paragraph_format.space_after=Pt(5)
doc.styles['Caption'].font.italic=True
header=sec.header.paragraphs[0];header.text='PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU                                      NHÓM 8'
header.runs[0].font.size=Pt(9)
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
footer.add_run('Đề 8  |  Dữ liệu mô phỏng  |  ')
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)
for r in footer.runs:r.font.size=Pt(9)
doc.core_properties.title='So sánh hai phương án định tuyến bằng dữ liệu độ trễ'
doc.core_properties.author='Nhóm 8'
doc.core_properties.subject='Bài tập lớn Phương pháp thống kê dữ liệu'

def p(text='',bold=False,align=None,size=None):
 x=doc.add_paragraph();r=x.add_run(text);r.bold=bold
 if align is not None:x.alignment=align
 if size:r.font.size=Pt(size)
 return x
def h(text):doc.add_heading(text,1)
def h2(text):doc.add_heading(text,2)
def page():doc.add_page_break()
def table(headers,rows,widths=None,size=10.5):
 t=doc.add_table(rows=1, cols=len(headers));t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
 for i,v in enumerate(headers):t.rows[0].cells[i].text=str(v)
 for row in rows:
  for i,v in enumerate(row):
   if i==0:cells=t.add_row().cells
   cells[i].text=str(v)
 for ri,row in enumerate(t.rows):
  for ci,c in enumerate(row.cells):
   c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
   if widths:c.width=Inches(widths[ci])
   pr=c._tc.get_or_add_tcPr();mar=OxmlElement('w:tcMar')
   for edge,val in [('top','75'),('left','90'),('bottom','75'),('right','90')]:
    z=OxmlElement('w:'+edge);z.set(qn('w:w'),val);z.set(qn('w:type'),'dxa');mar.append(z)
   pr.append(mar)
   borders=OxmlElement('w:tcBorders')
   for edge in ['top','left','bottom','right']:
    z=OxmlElement('w:'+edge);z.set(qn('w:val'),'single');z.set(qn('w:sz'),'4');z.set(qn('w:color'),'D9D9D9');borders.append(z)
   pr.append(borders)
   sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'17324D' if ri==0 else ('F0F4F7' if ri%2==0 else 'FFFFFF'));pr.append(sh)
   for x in c.paragraphs:
    x.paragraph_format.space_after=Pt(0);x.paragraph_format.line_spacing=1.06
    x.alignment=WD_ALIGN_PARAGRAPH.LEFT if ci==0 else WD_ALIGN_PARAGRAPH.CENTER
    for r in x.runs:
     r.font.size=Pt(size)
     if ri==0:r.bold=True;r.font.color.rgb=RGBColor(255,255,255)
  trpr=row._tr.get_or_add_trPr();ns=OxmlElement('w:cantSplit');trpr.append(ns)
 repeat=OxmlElement('w:tblHeader');t.rows[0]._tr.get_or_add_trPr().append(repeat)
 p('').paragraph_format.space_after=Pt(0)
 return t
def fig(name,caption,width=6.5):
 x=doc.add_paragraph();x.alignment=WD_ALIGN_PARAGRAPH.CENTER
 x.paragraph_format.space_after=Pt(3);x.add_run().add_picture(str(ROOT/'figures'/name),width=Inches(width))
 x=doc.add_paragraph(caption,style='Caption');x.alignment=WD_ALIGN_PARAGRAPH.CENTER
def mr(txt):
 x=OxmlElement('m:r');t=OxmlElement('m:t');t.text=txt;x.append(t);return x
def frac(num,den):
 x=OxmlElement('m:f')
 for tag,value in [('num',num),('den',den)]:
  e=OxmlElement('m:'+tag);e.append(mr(value));x.append(e)
 return x
def eq(*nodes):
 x=doc.add_paragraph();x.alignment=WD_ALIGN_PARAGRAPH.CENTER
 x.paragraph_format.space_after=Pt(8)
 m=OxmlElement('m:oMath')
 for n in nodes:m.append(mr(n) if isinstance(n,str) else n)
 x._p.append(m);return x

# Trang 1
p('HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG',True,WD_ALIGN_PARAGRAPH.CENTER,13)
p('KHOA VIỄN THÔNG 1',True,WD_ALIGN_PARAGRAPH.CENTER,13)
p('\nBÁO CÁO BÀI TẬP LỚN',True,WD_ALIGN_PARAGRAPH.CENTER,16)
p('PHƯƠNG PHÁP THỐNG KÊ DỮ LIỆU',True,WD_ALIGN_PARAGRAPH.CENTER,15)
x=doc.add_paragraph('So sánh hai phương án định tuyến bằng dữ liệu độ trễ',style='Title');x.alignment=WD_ALIGN_PARAGRAPH.CENTER
p('Đề 8     Nhóm 8',True,WD_ALIGN_PARAGRAPH.CENTER,15)
p('Giảng viên hướng dẫn  Vũ Quang Minh',False,WD_ALIGN_PARAGRAPH.CENTER,13)
p('Thành viên thực hiện',True,WD_ALIGN_PARAGRAPH.CENTER)
table(['Họ và tên','Mã sinh viên'],MEMBERS,[3.9,2.7],11.5)
p('Dữ liệu sử dụng hoàn toàn là dữ liệu mô phỏng bằng máy tính.',False,WD_ALIGN_PARAGRAPH.CENTER,11)
p('Seed 20261104     Mức ý nghĩa 5%     Mức tin cậy 95%',False,WD_ALIGN_PARAGRAPH.CENTER,11)
p('Tháng 11 năm 2026',False,WD_ALIGN_PARAGRAPH.CENTER,11)

# Trang 2
page();h('1 Bài toán và thiết kế mô phỏng')
p('Bài toán đặt ra là so sánh độ trễ của hai phương án định tuyến trên hai nhóm phiên truyền độc lập. Độ trễ nhỏ hơn có lợi cho thời gian phản hồi. Báo cáo dùng Mann–Whitney hai phía làm phân tích chính và Welch hai phía để đối chiếu kết luận về trung bình. Nội dung bám đề 8, các yêu cầu chung và danh mục sản phẩm của tài liệu giao bài [1].')
p('Kết quả chính: ở mẫu chi tiết đã lưu, cả hai kiểm định chưa cho đủ bằng chứng khác biệt tại mức 5%. Trong 200 mẫu mới, tỷ lệ phát hiện của Mann–Whitney là 76,5%, của Welch là 49,5%. Mô hình sinh dữ liệu quy định B có phân phối dịch trái 4 ms; thông tin này dùng để đánh giá phương pháp, tách biệt với suy luận từ mẫu.')
h2('1.1 Mô hình và đơn vị quan sát')
eq('X = 20 + Z,       Y = 16 + Z′,       Z, Z′ ∼ Exp(scale = 10 ms)')
table(['Nội dung','Quy định'],[
 ('Đơn vị quan sát','Một phiên truyền độc lập'),('Biến nhóm','A hoặc B'),
 ('Biến đáp ứng','Độ trễ, đơn vị ms'),('Cỡ mẫu chi tiết','40 phiên A và 40 phiên B'),
 ('Quan hệ giữa hai mẫu','Độc lập, không ghép cặp'),('Số lần mô phỏng mới','200, mỗi lần 40 A và 40 B')],[2.5,4.1],11)
p('Tham số scale = 10 là kỳ vọng của biến mũ, tương ứng tốc độ λ = 0,1/ms. Mỗi lần sinh tạo 80 biến ngẫu nhiên độc lập. Số thứ tự phiên A01 và B01 chỉ là mã nhận diện, không biểu thị chung điều kiện thử nghiệm.')
h2('1.2 Quy trình và khả năng tái lập')
p('Ấn định seed 20261104 trước khi phân tích. NumPy SeedSequence tạo hai nhánh: (0) cho mẫu chi tiết và (1) cho mô phỏng. Nhánh (1) tiếp tục sinh 200 nhánh con (1,0) đến (1,199). Mẫu chi tiết không nằm trong 200 lần lặp. Mỗi lần dùng cùng hai mẫu mới để chạy cả hai kiểm định [4].')
p('Không đổi seed để tìm kết quả có ý nghĩa. Không thay số liệu bằng trung bình, phương sai hay chênh lệch thật của mô hình. Các độ trễ lớn hợp lệ được giữ nguyên.')

# Trang 3
page();h('2 Cơ sở xác suất và thống kê')
h2('2.1 Kiến thức chương 1 đến chương 5 đã sử dụng')
p('Bài sử dụng các nhóm kiến thức nền ở chương 1–5 để hình thành và giải thích các kiểm định phi tham số ở chương 7. Vì tài liệu giao bài không kèm mục lục giáo trình, bảng sau nêu nội dung kiến thức, không tự gán tên riêng cho từng chương.')
table(['Kiến thức nền','Vai trò trong bài'],[
 ('Biến ngẫu nhiên và phân phối xác suất','Mô hình mũ mô tả độ trễ lệch phải; dịch hằng số tạo hai phương án.'),
 ('Kỳ vọng và phương sai','Phân biệt trung bình với trung vị; giải thích biến động độ trễ.'),
 ('Mẫu và tính độc lập','Xác định n = 40 mỗi nhóm và loại thiết kế ghép cặp.'),
 ('Thống kê mô tả','Trung bình, trung vị, SD và IQR cho thấy vị trí, độ phân tán và độ lệch.'),
 ('Ước lượng và phân phối mẫu','Dùng s² từ mẫu, sai số chuẩn và KTC 95% cho chênh lệch trung bình.'),
 ('Suy luận thống kê','Mức ý nghĩa 5%, p-value và lực kiểm định được phân biệt rõ.')],[2.35,4.25],11)
h2('2.2 Đại lượng thật chỉ dùng để đánh giá')
p('Với Z có phân phối mũ kỳ vọng 10 ms, hàm phân phối là F(z) = 1 − exp(−z/10) khi z ≥ 0 và bằng 0 khi z < 0. Phân vị mức q là −10 ln(1 − q). Do đó:')
table(['Đại lượng mô hình','A','B'],[
 ('Trung bình thật (ms)','30','26'),('Trung vị thật (ms)','26,9315','22,9315'),
 ('SD thật (ms)','10','10'),('IQR thật (ms)','10,9861','10,9861')],[3.4,1.6,1.6],11)
p('Hai phân phối có cùng dạng và cùng độ phân tán, chỉ dịch vị trí 4 ms. Đối với hai phiên độc lập, xác suất B có độ trễ thấp hơn A là 1 − 0,5 exp(−0,4) ≈ 66,484%. Điều này không bảo đảm mọi phiên B đều nhanh hơn A.')
p('Các con số trong bảng này được suy ra từ cơ chế tạo dữ liệu. Các bảng mô tả, kiểm định và khoảng tin cậy ở những trang tiếp theo đều tính từ các quan sát đã sinh, dùng phương sai mẫu với mẫu số n − 1.')

# Trang 4
page();h('3 Thống kê mô tả của mẫu chi tiết')
table(['Chỉ tiêu (ms nếu có)','Phương án A','Phương án B'],[
 ('Số phiên',40,40),('Trung bình',f(A['mean_ms']),f(B['mean_ms'])),
 ('Trung vị',f(A['median_ms']),f(B['median_ms'])),('Độ lệch chuẩn mẫu',f(A['sd_ms']),f(B['sd_ms'])),
 ('Tứ phân vị Q1',f(A['q1_ms']),f(B['q1_ms'])),('Tứ phân vị Q3',f(A['q3_ms']),f(B['q3_ms'])),
 ('IQR = Q3 − Q1',f(A['iqr_ms']),f(B['iqr_ms'])),
 ('Nhỏ nhất',f(A['min_ms']),f(B['min_ms'])),('Lớn nhất',f(A['max_ms']),f(B['max_ms']))],[3.2,1.7,1.7],10.7)
fig('histogram.png','Hình 1 Histogram hai mẫu dùng chung các mốc chia lớp',6.5)
p('Trung bình lớn hơn trung vị ở cả hai nhóm, phù hợp với dữ liệu lệch phải. Mẫu A có vài phiên rất chậm kéo trung bình lên. Dùng cùng mốc chia lớp giúp so sánh công bằng hình dạng và vị trí. Mức chồng lấn giữa hai mẫu lớn nên đồ thị chưa đủ để khẳng định khác biệt.')
p('SD dùng ddof = 1. Q1 và Q3 dùng nội suy tuyến tính của NumPy; IQR được tính từ hai phân vị này. Giá trị đầy đủ được giữ trong CSV, báo cáo chỉ làm tròn khi trình bày.',size=10.5)

# Trang 5
page();h('4 Biểu đồ hộp và tính độc lập')
fig('boxplot.png','Hình 2 Hộp biểu diễn Q1 đến Q3 và đường trung vị',6.5)
p('Trung vị A là 23,907 ms và B là 23,688 ms, chỉ lệch 0,219 ms trong mẫu này. IQR của B khoảng 15,166 ms, lớn hơn IQR của A 7,561 ms. Đây là biến động do lấy mẫu; không nên kết luận hai phân phối tổng thể có phương sai khác chỉ từ hai hộp.')
p('Râu hộp dừng ở quan sát xa nhất còn trong khoảng [Q1 − 1,5IQR; Q3 + 1,5IQR]. Các điểm ngoài râu là giá trị xa theo quy tắc đồ thị. Chúng vẫn là quan sát hợp lệ của phân phối mũ; nhóm không xóa chúng để làm p-value nhỏ hơn.')
h2('4.1 Vì sao không dùng kiểm định ghép cặp')
p('Hai phương án được thử trên hai nhóm phiên độc lập. Không có cùng một phiên được đo trước và sau, cũng không có thiết kế ghép theo một đơn vị chung. Vì vậy, không tồn tại sai khác cặp tự nhiên Dᵢ để làm cơ sở cho kiểm định t ghép cặp hoặc Wilcoxon hạng có dấu.')
p('Ghép A01 với B01 chỉ vì cùng số thứ tự sẽ tạo cặp tùy tiện. Cách làm đó không phản ánh thiết kế và có thể khiến sai số chuẩn hoặc diễn giải sai khác cặp thiếu căn cứ. Mann–Whitney và Welch đều sử dụng cấu trúc hai mẫu độc lập của bài.')
h2('4.2 Điều kiện suy luận')
p('Các quan sát có thang đo định lượng, có thể so sánh thứ tự và độc lập trong từng nhóm cũng như giữa hai nhóm. Mann–Whitney không yêu cầu dữ liệu gốc phân phối chuẩn. Việc diễn giải khác biệt vị trí dựa vào giả thiết hai phân phối cùng dạng; giả thiết này được bảo đảm bởi cơ chế mô phỏng, không được khẳng định chỉ từ histogram [2].')

# Trang 6
page();h('5 Kiểm định Mann–Whitney hai phía')
h2('5.1 Giả thuyết và cách tính')
p('H₀: F_A(t) = F_B(t) với mọi t, hai phân phối độ trễ giống nhau. H₁: hai phân phối khác nhau. Chọn kiểm định hai phía với α = 0,05 trước khi xem dữ liệu. Trong họ mô hình dịch chuyển cùng dạng của đề, H₀ tương ứng không có dịch chuyển vị trí [2].')
p('Gộp 80 quan sát, sắp tăng dần và gán hạng 1 đến 80. Nếu một giá trị lặp tⱼ lần, tất cả các quan sát đó nhận hạng trung bình của các vị trí chúng chiếm. Dữ liệu đầy đủ dùng để xếp hạng trước khi làm tròn.')
eq('U_A = R_A − ',frac('n_A(n_A + 1)','2'),',       U_B = n_A n_B − U_A')
p('R_A là tổng hạng của A. U_A đếm số cặp mà A lớn hơn B, cộng nửa số cặp bằng nhau. SciPy trả thống kê U tương ứng với mẫu A được truyền vào đầu tiên. U nhỏ nhất chỉ là cách trình bày bổ sung, không đổi p-value hai phía.')
eq('E₀(U_A) = ',frac('n_A n_B','2'),' = 800')
eq('Var₀(U_A) = ',frac('n_A n_B','12'),' [N + 1 − ',frac('Σⱼ(tⱼ³ − tⱼ)','N(N − 1)'),']')
p('N = 80. Tổng hiệu chỉnh bằng 0 khi không có hạng trùng. Với cỡ mẫu 40 mỗi nhóm, nhóm dùng xấp xỉ chuẩn có hiệu chỉnh liên tục 0,5 và hiệu chỉnh trùng hạng, không dùng cách tính exact mặc định tùy phiên bản.')
eq('z = ',frac('|U_A − 800| − 0,5','σ_U'),',       p = min(1; 2[1 − Φ(z)])')
h2('5.2 Kết quả mẫu chi tiết')
p('R_A = 1730, R_B = 1510 và tổng hai hạng bằng 3240 = 80×81/2. Suy ra U_A = 910, U_B = 690, tổng bằng 1600. Không có giá trị trùng ở độ chính xác gốc. Phương sai dưới H₀ là 10800, σ_U = 103,923 và z = 1,053664.')
p('p = 0,292037 > 0,05 nên chưa bác bỏ H₀. Mẫu này chưa cho đủ bằng chứng hai phân phối khác nhau. Kết quả không chứng minh hai phương án tương đương và cũng không xác nhận H₀ đúng.')

# Trang 7
page();h('6 Minh họa xếp hạng và mức ảnh hưởng')
p('Bảng 1 trích các vị trí quanh nơi hai nhóm bắt đầu xen kẽ trong mẫu gộp. Bảng pooled_ranks.csv kèm bài có đủ 80 quan sát, giá trị chưa làm tròn và hạng. Các thống kê kiểm định dùng toàn bộ 80 quan sát, không dùng riêng phần minh họa.')
ranks=list(csv.DictReader((ROOT/'data/pooled_ranks.csv').open(encoding='utf-8-sig')))
selected=ranks[10:22]
table(['Thứ tự','Mã phiên','Nhóm','Độ trễ (ms)','Hạng'],[
 (r['sorted_order'],r['observation_id'],r['group'],f(float(r['latency_ms']),6),f(float(r['rank']),1)) for r in selected],[.75,1.2,.7,2.3,1.65],10.7)
p('Ví dụ riêng về hạng trùng: nếu ba giá trị tăng dần là 21, 21, 23 ms thì hai giá trị 21 nhận hạng (1 + 2)/2 = 1,5 và 23 nhận hạng 3. Ví dụ này chỉ giải thích quy tắc, không được thêm vào dữ liệu mô phỏng.')
h2('6.1 Xác suất so sánh hai phiên độc lập')
eq('θ̂ = ',frac('U_A','n_A n_B'),' = ',frac('910','1600'),' = 0,56875')
p('Ước lượng θ̂ = 56,875% là tỷ lệ các cặp chéo mà A có độ trễ cao hơn B, cộng nửa tỷ lệ bằng nhau. Nó mô tả xu hướng B nhanh hơn A trên hai phiên lấy độc lập. Đây không phải tỷ lệ phiên B nhanh hơn chính phiên A cùng số thứ tự, vì dữ liệu không ghép cặp.')
p('Hệ số tương quan hạng nhị phân r = 2θ̂ − 1 = 0,1375 theo chiều A trễ hơn B. Mức ảnh hưởng ước lượng nhỏ trong mẫu chi tiết phù hợp với kết quả chưa có ý nghĩa thống kê. Các ước lượng này không được thay bằng xác suất thật 66,484% của cơ chế sinh dữ liệu.')
h2('6.2 Phạm vi diễn giải Mann–Whitney')
p('Mann–Whitney sử dụng thứ tự, không trực tiếp kiểm định hiệu trung bình. Khi dạng phân phối khác nhau, kết quả có thể phản ánh khác biệt về hình dạng hoặc độ phân tán. Trong đề này, cùng dạng và chỉ dịch vị trí cho phép liên hệ kết quả với dịch chuyển vị trí, bao gồm dịch chuyển trung vị [2].')

# Trang 8
page();h('7 Kiểm định Welch và khoảng tin cậy')
p('Đối với Welch, H₀: μ_A = μ_B và H₁: μ_A ≠ μ_B. Đại lượng mục tiêu là chênh lệch trung bình tổng thể Δ = μ_A − μ_B. Nhóm gọi ttest_ind với equal_var=False và alternative="two-sided" [3].')
eq('SE = √(s_A²/n_A + s_B²/n_B),       t = ',frac('X̄ − Ȳ','SE'))
eq('ν = ',frac('(s_A²/n_A + s_B²/n_B)²','(s_A²/n_A)²/(n_A−1) + (s_B²/n_B)²/(n_B−1)'))
eq('KTC 95% cho Δ = (X̄ − Ȳ) ± t₀,₉₇₅;ν × SE')
table(['Kết quả từ mẫu','Giá trị'],[
 ('Chênh lệch trung bình A − B (ms)',f(T['mean_difference_a_minus_b_ms'],6)),
 ('Sai số chuẩn (ms)',f(T['welch_standard_error_ms'],6)),
 ('Thống kê t',f(T['t_welch'],6)),('Bậc tự do xấp xỉ',f(T['df_welch'],6)),
 ('p-value hai phía',f(T['p_welch'],6)),
 ('KTC 95% của Δ (ms)',f"[{f(T['mean_difference_ci95_low_ms'],6)}; {f(T['mean_difference_ci95_high_ms'],6)}]")],[3.55,3.05],11)
p('p = 0,859422 > 0,05 nên chưa bác bỏ H₀ về trung bình. KTC chứa 0 và khá rộng. Mẫu tương thích cả với A nhanh hơn B lẫn B nhanh hơn A trong phạm vi khoảng ước lượng; chưa đủ cơ sở chọn phương án dựa riêng vào chênh lệch trung bình mẫu 0,426 ms.')
h2('7.1 Điều kiện và so sánh hai phép kiểm định')
p('Welch không yêu cầu hai phương sai bằng nhau. Dữ liệu mũ không chuẩn và lệch phải, nên suy luận t ở đây dựa vào xấp xỉ phân phối của trung bình mẫu với n = 40 mỗi nhóm. Độ lệch và các phiên trễ lớn có thể làm xấp xỉ kém hơn; không khẳng định đây là kiểm định t chính xác hữu hạn mẫu cho phân phối mũ.')
table(['Phương pháp','Đại lượng được xét','Kết luận mẫu'],[
 ('Mann–Whitney','Phân phối; vị trí khi cùng dạng','Chưa bác bỏ H₀'),
 ('Welch','Trung bình tổng thể','Chưa bác bỏ H₀')],[1.4,3.5,1.7],10.7)
p('Sự thống nhất về quyết định không có nghĩa hai phương pháp kiểm định cùng một đại lượng. p-value lớn hơn cũng không phải thước đo chất lượng phương án định tuyến.')

# Trang 9
page();h('8 Mô phỏng lặp 200 lần')
p('Mỗi lần r sinh mới 40 phiên A và 40 phiên B theo đúng mô hình. Tính hai p-value trên cùng dữ liệu của lần r, rồi ghi I(p < 0,05). Tỷ lệ phát hiện là tổng số lần bác bỏ chia 200. Vì mô hình thật có dịch chuyển 4 ms, tỷ lệ này ước lượng lực kiểm định tại đúng kịch bản đã cho, không phải tỷ lệ sai lầm loại I.')
table(['Phương pháp','Phát hiện','Tỷ lệ','SE Monte Carlo','Wilson 95%'],[
 (m['test'],f"{m['detected']}/200",pc(m['detection_rate']),pc(m['monte_carlo_se'],2),
  f"[{pc(m['wilson_ci95_low'],2)}; {pc(m['wilson_ci95_high'],2)}]") for m in MC],[1.4,1.05,.8,1.4,1.95],10.3)
fig('monte_carlo_detection.png','Hình 3 Tỷ lệ phát hiện và khoảng Wilson 95%',6.25)
p('Sai số Monte Carlo ước lượng bằng √[p̂(1 − p̂)/200]. Với 200 lần, sai số chuẩn tối đa khoảng 3,54 điểm phần trăm. Khoảng Wilson phản ánh bất định do số lần mô phỏng hữu hạn, không phải KTC cho độ trễ và không thay thế KTC Welch của mẫu chi tiết.')
p('Trong cùng 200 lần: cả hai phát hiện 98 lần, chỉ Mann–Whitney 55 lần, chỉ Welch 1 lần, cả hai không phát hiện 46 lần. Tỷ lệ phát hiện chênh 27 điểm phần trăm trong thí nghiệm này; hai tỷ lệ dùng cùng các lần lặp nên có quan hệ với nhau.')
p('Mann–Whitney phát hiện thường xuyên hơn ở kịch bản mũ dịch chuyển này. Kết quả không chứng minh phương pháp này luôn tốt hơn Welch ở mọi phân phối, cỡ mẫu hoặc mục tiêu suy luận.')

# Trang 10
page();h('9 Kết luận và giới hạn áp dụng')
h2('9.1 Kết luận theo dữ liệu và theo mô hình')
p('Từ mẫu chi tiết: A có trung bình 28,125 ms, B có trung bình 27,699 ms. Mann–Whitney p = 0,292037 và Welch p = 0,859422 đều lớn hơn 0,05. Do đó, nhóm chưa có đủ bằng chứng về khác biệt từ riêng mẫu này. Không diễn giải “chưa bác bỏ” thành “hai phương án bằng nhau” hoặc “đã chứng minh tương đương”.')
p('Từ cơ chế mô hình đã biết: B có phân phối độ trễ thấp hơn A đúng 4 ms theo dịch chuyển vị trí. Trung bình thật B là 26 ms so với 30 ms của A, giảm khoảng 13,33% so với A. Đây là tính chất được gán trong mô hình, không phải mức giảm được ước lượng chắc chắn từ mẫu chi tiết.')
p('Từ 200 lần lặp: Mann–Whitney phát hiện khác biệt trong 76,5% số lần, Welch trong 49,5%. Vì lực kiểm định chưa đạt 100%, một mẫu chưa phát hiện khác biệt vẫn có thể xuất hiện dù mô hình thật khác nhau. Các kết quả lặp giúp giải thích mẫu chi tiết, không thay p-value của mẫu bằng tỷ lệ phát hiện.')
h2('9.2 Ý nghĩa thực tế và lựa chọn phương pháp')
p('Nếu mục tiêu là đánh giá xu hướng độ trễ giữa các phân phối cùng dạng, Mann–Whitney phù hợp với dữ liệu lệch và cho khả năng phát hiện tốt hơn trong kịch bản này. Nếu mục tiêu nghiệp vụ là thời gian trễ trung bình, Welch trả lời trực tiếp câu hỏi về trung bình và cho KTC của chênh lệch. Cần chọn đại lượng mục tiêu trước khi xem kết quả.')
p('Trong phạm vi mô hình đã cho, B là phương án có độ trễ thấp hơn. Để quyết định triển khai thực tế, cần xác định trước mức cải thiện tối thiểu có ích hoặc ngưỡng dịch vụ, rồi kiểm tra bằng số đo thật. Không suy luận thêm về chi phí, mất gói hoặc năng lượng khi bài chưa cung cấp dữ liệu.')
h2('9.3 Hạn chế')
p('Dữ liệu hoàn toàn mô phỏng, chỉ xét hai phân phối mũ cùng scale 10 ms và n = 40. Thực tế có thể có tự tương quan, nghẽn mạng, các mức tải khác nhau hoặc khác dạng phân phối. Các điều kiện đó có thể làm thay đổi hiệu quả kiểm định và giới hạn diễn giải dịch chuyển vị trí.')
p('Mann–Whitney dùng xấp xỉ chuẩn, Welch dùng xấp xỉ t cho dữ liệu lệch. Chỉ 200 lần lặp tạo sai số Monte Carlo đáng kể. Bài chưa mô phỏng dưới H₀ nên không dùng thí nghiệm này để khẳng định mức sai lầm loại I thực nghiệm bằng 5%. Không có kiểm định tương đương hoặc đánh giá triển khai trên mạng thật.')

# Trang 11
page();h('10 Công cụ và hướng dẫn tái lập')
p('Môi trường đã chạy: Python '+S['versions']['python']+', NumPy '+S['versions']['numpy']+', pandas '+S['versions']['pandas']+', SciPy '+S['versions']['scipy']+', Matplotlib '+S['versions']['matplotlib']+'. Seed mặc định 20261104, α = 0,05. requirements.txt chốt các phiên bản thư viện. README.md trình bày lệnh chạy trên Windows và Linux/macOS.')
p('Từ thư mục gốc repo, tạo môi trường ảo, cài requirements.txt, rồi chạy lệnh sau. Các đường dẫn dưới đây là tương đối so với repo, dùng được trên máy khác.',size=11)
p('python scripts/analysis.py --seed 20261104 --out-dir .',bold=True,size=11)
p('Mã tạo dữ liệu, tính mô tả, gộp hạng, kiểm định, chạy 200 lần lặp, xuất bảng và vẽ lại biểu đồ. Dùng thư mục đầu ra khác nếu muốn giữ nguyên bộ số liệu đã nộp. Các phép kiểm tra trong mã đối chiếu U từ hạng với đếm cặp và đối chiếu Welch tính tay với SciPy.')
table(['Tệp hoặc thư mục','Nội dung sử dụng'],[
 ('data/sample_detail.csv','80 quan sát gốc của mẫu chi tiết'),
 ('data/pooled_ranks.csv','Bảng gộp đủ 80 hạng'),
 ('data/simulation_200_raw.csv','16.000 quan sát của 200 lần mới'),
 ('results/simulation_200.csv','Thống kê và quyết định từng lần'),
 ('results/descriptive.csv và detail_tests.csv','Mô tả và hai kiểm định của mẫu chi tiết'),
 ('results/summary.json','Seed, phiên bản, luồng sinh và tổng hợp'),
 ('figures/ và scripts/','Biểu đồ và mã phân tích'),
 ('bao_cao/ và trinh_chieu/','Báo cáo và bài trình chiếu')],[3.15,3.45],10.3)
h2('10.1 Đối chiếu yêu cầu chung')
p('Nhóm có 5 thành viên. Kế hoạch thực hiện đề xuất trong 3 tuần: tuần 1 thiết kế và tạo dữ liệu, tuần 2 kiểm định và mô phỏng lặp, tuần 3 rà soát báo cáo và thuyết trình. Kế hoạch này không phải nhật ký công việc đã hoàn thành của từng thành viên.')
p('Công cụ và bước xử lý được công bố. Dữ liệu luôn được nhận diện là mô phỏng. Seed, dữ liệu, mã và kết quả đều được lưu. Mọi kiểm định dùng 5%, mọi KTC dùng 95%. Ước lượng của mẫu tính từ mẫu; tham số thật chỉ dùng đánh giá. Cách chọn phương pháp, điều kiện và ý nghĩa thực tế đã nêu ở các mục 4–9.')
p('Đã chạy lại phân tích độc lập với cùng seed: cả 7 CSV số liệu có SHA-256 trùng khớp. Tệp results/sha256_data.json cho phép đối chiếu dữ liệu và kết quả khi chạy lại.',size=10.5)

# Trang 12
page();h('11 Phân công và tài liệu tham khảo')
h2('11.1 Bảng phân công và đóng góp dự kiến')
p('Bảng dưới là đề xuất phân công để nhóm hoàn thiện và xác nhận. Tỷ lệ 20% mỗi người là mức đóng góp dự kiến, không khẳng định đó là đóng góp thực tế đã được ghi nhận. Nhóm cần cập nhật theo công việc và minh chứng trước khi nộp.')
table(['Thành viên và MSSV','Nhiệm vụ đề xuất','Tỷ lệ dự kiến'],[
 (name+'\n'+sid,TASKS[i],'20%') for i,(name,sid) in enumerate(MEMBERS)],[2.45,3.05,1.1],10.7)
p('Tất cả thành viên cùng đọc lại kết luận, kiểm tra dữ liệu/mã và chuẩn bị trả lời câu hỏi. Bảng phân công riêng trong repo có thêm ô để ghi tỷ lệ và minh chứng đóng góp thực tế sau khi nhóm xác nhận.',size=11)
h2('11.2 Tài liệu tham khảo')
refs=[
 '[1] Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu, tài liệu giao bài do người học cung cấp. Trang 1: yêu cầu chung; trang 9: đề 8; trang 12: sản phẩm nộp và đánh giá.',
 '[2] SciPy. scipy.stats.mannwhitneyu. Giả thuyết, mẫu độc lập, xấp xỉ chuẩn và hiệu chỉnh hạng trùng. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html',
 '[3] SciPy. scipy.stats.ttest_ind. Kiểm định trung bình hai mẫu độc lập, lựa chọn equal_var=False và khoảng tin cậy. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html',
 '[4] NumPy. Parallel random number generation. SeedSequence.spawn và các luồng giả ngẫu nhiên tái lập. https://numpy.org/doc/stable/reference/random/parallel.html']
for text in refs:p(text,size=10)
p('Các tài liệu trực tuyến được đối chiếu ngày 04/11/2026. Phiên bản thư viện thực sự đã chạy được ghi ở mục 10 và tệp summary.json.',size=10)
out=ROOT/'bao_cao/Bao_cao_De_8_Nhom_8.docx';out.parent.mkdir(parents=True,exist_ok=True)
doc.save(out)
contrib=ROOT/'phan_cong.csv'
with contrib.open('w',encoding='utf-8-sig',newline='') as fp:
 w=csv.writer(fp);w.writerow(['ho_ten','mssv','nhiem_vu_de_xuat','ty_le_du_kien','ty_le_thuc_te_can_xac_nhan','minh_chung_thuc_te_can_bo_sung'])
 for i,(name,sid) in enumerate(MEMBERS):w.writerow([name,sid,TASKS[i],0.2,'',''])
print(out)
