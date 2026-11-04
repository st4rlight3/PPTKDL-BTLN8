import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Presentation,PresentationFile,FileBlob} from '@oai/artifact-tool';

// Build a Vietnamese ten-slide presentation from the reproducible analysis.
const scriptDir=path.dirname(fileURLToPath(import.meta.url));
const workspaceDir=path.resolve(scriptDir,'..');
const buildDir=path.join(workspaceDir,'trinh_chieu');
function applyPresentationChartFont(chart,{fontFamily}){
 const styles=[chart.legend?.textStyle,chart.dataLabels?.textStyle,chart.xAxis?.textStyle,chart.yAxis?.textStyle];
 for(const axis of [chart.xAxis,chart.yAxis]) if(axis?.title?.textStyle) styles.push(axis.title.textStyle);
 for(const style of styles) if(style) style.typeface=fontFamily;
}
const S=JSON.parse(await fs.readFile(path.join(workspaceDir,'results/summary.json'),'utf8'));
const D=S.detail_tests,[A,B]=S.descriptive;
const csv=async file=>{const text=(await fs.readFile(file,'utf8')).replace(/^\uFEFF/,'').trim();const [head,...lines]=text.split(/\r?\n/);const cols=head.split(',');return lines.map(line=>Object.fromEntries(line.split(',').map((v,i)=>[cols[i],v])));};
const raw=await csv(path.join(workspaceDir,'data/sample_detail.csv'));
const ranks=await csv(path.join(workspaceDir,'data/pooled_ranks.csv'));
const a=raw.filter(r=>r.group==='A').map(r=>+r.latency_ms),b=raw.filter(r=>r.group==='B').map(r=>+r.latency_ms);
const C={navy:'#06152B',white:'#F6FAFF',muted:'#B9CFE3',cyan:'#59D8F0',teal:'#27D5B2',grid:'#2D435B'};
const fmt=(n,k=2)=>Number(n).toFixed(k).replace('.',',');
const bg=await fs.readFile(path.join(buildDir,'network_background.png'));
const bgArray=bg.buffer.slice(bg.byteOffset,bg.byteOffset+bg.byteLength);
const quiet=await fs.readFile(path.join(buildDir,'network_background_quiet.png'));
const quietArray=quiet.buffer.slice(quiet.byteOffset,quiet.byteOffset+quiet.byteLength);
const p=Presentation.create({slideSize:{width:1280,height:720}});
p.theme.defaultFont='Arial';
let count=0;
function txt(s,text,x,y,w,h,size=28,color=C.white,bold=false){const z=s.shapes.add({geometry:'textbox',name:`text-${count++}`,position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});z.text=text;z.text.style={fontSize:size,typeface:'Arial',color,bold,wrap:'square',autoFit:'none',insets:0,verticalAlignment:'top'};return z;}
function slide(title,subtitle=''){const s=p.slides.add();s.background.fill=C.navy;s.images.add({blob:p.slides.items.length===1?bgArray:quietArray,contentType:'image/png',alt:'Nền viễn thông trừu tượng xanh navy',fit:'cover',position:{left:0,top:0,width:1280,height:720}});txt(s,title,64,40,1148,82,42,C.white,true);if(subtitle)txt(s,subtitle,66,126,1130,54,23,C.muted);txt(s,String(p.slides.items.length).padStart(2,'0'),1198,670,42,30,18,C.muted);return s;}
function table(s,values,x,y,w,h,widths,size=23){const z=s.tables.add({rows:values.length,columns:values[0].length,left:x,top:y,width:w,height:h,values,columnWidths:widths});z.borders.assign({fill:'#37516A',width:1,style:'solid'});for(let r=0;r<values.length;r++)for(let c=0;c<values[0].length;c++){const cell=z.getCell(r,c);cell.fill=r===0?'#123650':r%2?'#092039':'#0A2941';cell.text.style={fontSize:size,typeface:'Arial',color:r===0?C.cyan:C.white,bold:r===0,verticalAlignment:'middle',alignment:c===0?'left':'center',insets:{top:8,bottom:8,left:10,right:10},wrap:'square'};}return z;}
function chart(s,type,config){
 // Chart coordinates use six decimals for portable Excel chart workbooks.
 // Full precision analysis values remain in the delivered CSV and JSON files.
 const portable={...config,series:config.series.map(series=>({...series,...(series.values?{values:series.values.map(v=>v===null?null:Number(v.toFixed(6)))}:{}),...(series.xValues?{xValues:series.xValues.map(v=>v===null?null:Number(v.toFixed(6)))}:{})}))};
 const z=s.charts.add(type,{chartFill:C.navy,chartLine:{fill:'none',width:0},plotAreaFill:C.navy,plotAreaLine:{fill:'none',width:0},...portable});applyPresentationChartFont(z,{fontFamily:'Arial'});return z;
}
const ax=(title)=>({title:{text:title,textStyle:{fontSize:21,fill:C.white}},textStyle:{fontSize:20,fill:C.white},line:{fill:'#8AA6BC',width:1},majorGridlines:{fill:C.grid,width:1}});
const note=(s,text,links=[])=>{s.speakerNotes.text=text+'\n\nNguồn bài toán: Bộ đề bài tập nhóm Phương pháp thống kê dữ liệu sinh viên, đề 8 trang 9, yêu cầu chung trang 1 và sản phẩm nộp trang 12.\nDữ liệu và kết quả: analysis.py, seed 20261104, sample_detail.csv, summary.json.\n'+links.join('\n');};

// 1 Cover
{
 const s=slide('');
 txt(s,'HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG',66,48,1080,40,25,C.muted,true);
 txt(s,'KHOA VIỄN THÔNG 1',66,91,900,34,25,C.muted);
 txt(s,'So sánh hai phương án\nđịnh tuyến bằng\ndữ liệu độ trễ',66,182,1080,256,62,C.white,true);
 txt(s,'Đề 8   Phương pháp thống kê dữ liệu',68,461,970,42,30,C.cyan);
 txt(s,'Nhóm 8\nGiảng viên Vũ Quang Minh',68,533,1040,90,28,C.white);
 note(s,'Báo cáo bài tập nhóm về so sánh hai mẫu độ trễ độc lập. Toàn bộ dữ liệu là mô phỏng theo mô hình đề bài, không phải số đo mạng thực tế. Nhóm 8 gồm Phạm Gia Minh B24DCKD057, Phương Bảo Vỹ B24DCKD105, Nguyễn Đức Thành B24DCKD085, Phan Nguyễn Trung Khánh B24DCKD041 và Phùng Quốc Khánh Nam B24DCKD059. Kết luận được phân biệt giữa mẫu phân tích chi tiết và đặc điểm thật của mô hình tạo dữ liệu.');
}
// 2 Design
{
 const s=slide('Thiết kế mô phỏng','Hai nhóm phiên truyền độc lập, mỗi nhóm 40 quan sát, đơn vị ms');
 txt(s,'A   X = 20 + Z',68,203,720,62,42,C.cyan,true);
 txt(s,'B   Y = 16 + Z′',68,287,720,62,42,C.teal,true);
 txt(s,'Z và Z′ độc lập, phân phối mũ\nvới trung bình 10 ms',70,381,730,96,30,C.white);
 txt(s,'Seed 20261104',70,534,550,46,32,C.cyan,true);
 txt(s,'Lưu mẫu gốc, mã lệnh và kết quả để chạy lại',70,589,900,42,25,C.muted);
 txt(s,'200',920,209,260,113,86,C.white,true);
 txt(s,'lần sinh mẫu mới',850,327,360,48,28,C.white);
 txt(s,'Mann–Whitney và Welch\nhai phía, α = 0,05\nKhoảng tin cậy 95%',850,412,370,137,28,C.muted);
 note(s,'Chọn seed cố định trước khi chạy, không đổi seed để tìm một mẫu có ý nghĩa thống kê. SeedSequence tách luồng cho mẫu chi tiết và 200 lần mô phỏng, mỗi lần sinh mới 40 giá trị A và 40 giá trị B. Không tái sử dụng mẫu chi tiết trong bảng tỷ lệ phát hiện. Tham số 20, 16 và 10 chỉ định nghĩa mô hình tạo dữ liệu. Các trung bình, phương sai và sai số chuẩn trong phân tích được tính từ từng mẫu. Hướng dẫn chạy cùng phiên bản thư viện nằm trong README và requirements.txt.', ['https://numpy.org/doc/stable/reference/random/parallel.html']);
}
// 3 Descriptive and histogram
{
 const s=slide('Thống kê mô tả và histogram','Mẫu chi tiết có n = 40 mỗi nhóm, histogram dùng cùng khoảng lớp');
 table(s,[['Đại lượng','A','B'],['Trung bình',fmt(A.mean_ms),fmt(B.mean_ms)],['Trung vị',fmt(A.median_ms),fmt(B.median_ms)],['Độ lệch chuẩn',fmt(A.sd_ms),fmt(B.sd_ms)],['Q1',fmt(A.q1_ms),fmt(B.q1_ms)],['Q3',fmt(A.q3_ms),fmt(B.q3_ms)],['IQR',fmt(A.iqr_ms),fmt(B.iqr_ms)]],66,212,460,340,[240,110,110],23);
 const edges=[16,24,32,40,48,56,64,72];const bins=values=>edges.slice(0,-1).map((lo,i)=>values.filter(v=>v>=lo&&(i===edges.length-2?v<=edges[i+1]:v<edges[i+1])).length);
 chart(s,'bar',{position:{left:570,top:200,width:650,height:385},categories:edges.slice(0,-1).map((v,i)=>`${v}–${edges[i+1]}`),series:[{name:'A',values:bins(a),fill:C.cyan},{name:'B',values:bins(b),fill:C.teal}],barOptions:{direction:'column',grouping:'clustered',gapWidth:18},hasLegend:true,legend:{position:'top',textStyle:{fontSize:22,fill:C.white}},xAxis:{...ax('Độ trễ (ms)'),majorGridlines:null,textStyle:{fontSize:17,fill:C.white}},yAxis:{...ax('Số phiên'),min:0,max:25,majorUnit:5}});
 txt(s,'Cả hai mẫu lệch phải. Trung bình lớn hơn trung vị.',68,593,1090,44,27,C.white);
 note(s,'Trung bình A 28,12 ms và B 27,70 ms gần nhau trong mẫu chi tiết này. Trung vị lần lượt 23,91 và 23,69 ms. Độ lệch chuẩn dùng mẫu số n−1. Q1 và Q3 dùng nội suy tuyến tính của NumPy, IQR bằng Q3−Q1. Histogram có bảy lớp chung bề rộng 8 ms, từ 16 đến 72 ms. Mỗi lớp đóng bên trái và mở bên phải, lớp cuối chứa cả cận phải. Hai phân phối có đuôi phải dài. IQR của B lớn hơn A trong mẫu không phủ định việc hai phân phối tạo dữ liệu có cùng dạng và độ phân tán thật.');
}
// 4 Native scatter box representation
{
 const s=slide('Biểu đồ hộp của hai phương án','Hộp từ Q1 đến Q3, vạch giữa là trung vị, râu theo quy tắc 1,5 IQR');
 const series=[];
 function addSeries(name,xs,ys,color,width=3,markers=false){series.push({name,xValues:xs,values:ys,line:{fill:markers?'none':color,width:markers?0:width},marker:markers?{symbol:'circle',size:7,fill:color}:{symbol:'none'}});}
 function box(vals,d,x,color){const lo=d.q1_ms-1.5*d.iqr_ms,hi=d.q3_ms+1.5*d.iqr_ms;const inside=vals.filter(v=>v>=lo&&v<=hi);const low=Math.min(...inside),high=Math.max(...inside);addSeries(d.group+' hộp',[x-.21,x+.21,x+.21,x-.21,x-.21],[d.q1_ms,d.q1_ms,d.q3_ms,d.q3_ms,d.q1_ms],color);addSeries(d.group+' trung vị',[x-.21,x+.21],[d.median_ms,d.median_ms],C.white,4);addSeries(d.group+' râu dưới',[x,x],[low,d.q1_ms],color);addSeries(d.group+' râu trên',[x,x],[d.q3_ms,high],color);addSeries(d.group+' mút dưới',[x-.10,x+.10],[low,low],color);addSeries(d.group+' mút trên',[x-.10,x+.10],[high,high],color);const out=vals.filter(v=>v<lo||v>hi);if(out.length)addSeries(d.group+' ngoài râu',out.map(()=>x),out,color,0,true);}
 box(a,A,1,C.cyan);box(b,B,2,C.teal);
 chart(s,'scatter',{position:{left:65,top:198,width:720,height:415},series,scatterOptions:{style:'lineWithMarkers'},hasLegend:false,xAxis:{...ax('1 = A                 2 = B'),min:0,max:3,majorUnit:1,majorGridlines:null},yAxis:{...ax('Độ trễ (ms)'),min:10,max:70,majorUnit:10}});
 txt(s,'A   IQR 7,56 ms\nB   IQR 15,17 ms',831,231,362,100,30,C.cyan,true);
 txt(s,'Các giá trị ngoài râu\nvẫn là dữ liệu hợp lệ\ncủa phân phối mũ',831,384,356,132,29,C.white);
 txt(s,'Giữ toàn bộ 80 quan sát khi kiểm định',68,619,1100,38,26,C.muted);
 note(s,'Q1 và Q3 dùng cùng quy ước nội suy tuyến tính với thống kê mô tả. Râu dưới kéo đến quan sát nhỏ nhất còn trong khoảng Q1−1,5IQR. Râu trên kéo đến quan sát lớn nhất còn trong khoảng Q3+1,5IQR. Các điểm ngoài râu được thể hiện riêng. Các điểm lớn không tự động là lỗi nhập liệu, vì mô hình mũ tạo ra những độ trễ lớn với xác suất dương. Cần giữ các điểm này khi thực hiện cả hai kiểm định. Đuôi phải dài làm trung bình và kiểm định dựa trên trung bình nhạy hơn với giá trị lớn.');
}
// 5 Rank method
{
 const s=slide('Mann–Whitney và cách xếp hạng','Kiểm định hai phía cho hai mẫu độc lập');
 txt(s,'H₀   Hai phân phối như nhau\nH₁   Hai phân phối khác nhau',68,211,615,110,30,C.white,true);
 txt(s,'Gộp 80 giá trị rồi xếp tăng dần\nHạng trùng nhận hạng trung bình\nMẫu hiện tại không có hạng trùng',68,361,594,150,28,C.muted);
 txt(s,'U(A) = R(A) − 40 × 41 / 2',68,552,670,52,31,C.cyan,true);
 const rows=ranks.slice(12,18).map(r=>[r.observation_id,r.group,fmt(r.latency_ms,3),r.rank]);
 table(s,[['Mã','Nhóm','ms','Hạng'],...rows],715,211,500,337,[105,100,160,135],23);
 txt(s,'Minh họa hạng 13 đến 18\nKiểm định dùng đủ 80 giá trị',716,574,500,75,25,C.white);
 note(s,'Giả thuyết không là hai phân phối tổng thể giống nhau. Đối thuyết hai phía là các phân phối khác nhau theo cách kiểm định Mann–Whitney phát hiện. Khi hai phân phối cùng dạng và chỉ khác vị trí, có thể diễn giải kết quả theo dịch chuyển vị trí. Mann–Whitney không mặc nhiên kiểm định sự bằng nhau của trung bình. Gộp toàn bộ 80 giá trị, xếp hạng tăng dần, tính tổng hạng của mỗi nhóm. Nếu trùng giá trị, dùng midrank và hiệu chỉnh phương sai theo số lượng phần tử của từng nhóm trùng. Bảng chỉ minh họa sáu hạng nối tiếp. Toàn bộ bảng 80 hạng nằm trong pooled_ranks.csv.', ['https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html']);
}
// 6 Mann Whitney result
{
 const s=slide('Kết quả Mann–Whitney của mẫu chi tiết','Xấp xỉ chuẩn, hiệu chỉnh liên tục và hiệu chỉnh hạng trùng');
 txt(s,'p = 0,292',68,217,690,101,72,C.cyan,true);
 txt(s,'Chưa bác bỏ H₀ ở mức 5%',70,340,840,64,38,C.white,true);
 table(s,[['Thống kê','Giá trị'],['Tổng hạng A / B','1730 / 1510'],['U(A) / U(B)','910 / 690'],['|z| hiệu chỉnh','1,054']],806,211,412,235,[252,160],24);
 txt(s,'P̂(A > B) = 910 / 1600 = 56,9%',70,465,1090,58,35,C.white);
 txt(s,'Đây là ước lượng từ mẫu. Mẫu chưa đủ bằng chứng về khác biệt.\nChưa bác bỏ H₀ không chứng minh hai phương án tương đương.',70,563,1110,92,27,C.muted);
 note(s,'Tổng hạng A là 1730 và B là 1510. U_A bằng 1730−820 = 910, U_B bằng 1600−910 = 690. Tại H0, trung bình U bằng 800, phương sai bằng 10800 khi không có hạng trùng. Dùng hiệu chỉnh liên tục 0,5 cho p hai phía được |z| = 1,0537 và p = 0,2920. Không bác bỏ H0 vì p lớn hơn 0,05. Ước lượng xác suất một phiên A có độ trễ lớn hơn một phiên B ngẫu nhiên là U_A/(40×40) = 0,56875. Đây không phải bằng chứng đủ để xác nhận B tốt hơn ở mức 5% trong mẫu chi tiết. Giả thiết cùng dạng trong mô hình cho phép diễn giải theo vị trí, nhưng quyết định kiểm định vẫn dựa trên mẫu.', ['https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html']);
}
// 7 Welch
{
 const s=slide('Welch kiểm định chênh lệch trung bình','H₀  μA = μB     H₁  μA ≠ μB');
 txt(s,'A − B = 0,426 ms',68,199,720,67,48,C.teal,true);
 txt(s,'t = 0,178\ndf = 77,604\np = 0,859',919,219,297,146,31,C.white);
 chart(s,'scatter',{position:{left:70,top:292,width:770,height:220},series:[{name:'KTC 95%',xValues:[D.mean_difference_ci95_low_ms,D.mean_difference_ci95_high_ms],values:[1,1],line:{fill:C.teal,width:5},marker:{symbol:'none'}},{name:'Ước lượng',xValues:[D.mean_difference_a_minus_b_ms],values:[1],line:{fill:'none',width:0},marker:{symbol:'circle',size:11,fill:C.white}},{name:'Mốc 0',xValues:[0,0],values:[.7,1.3],line:{fill:C.muted,width:2},marker:{symbol:'none'}}],scatterOptions:{style:'lineWithMarkers'},hasLegend:false,xAxis:{...ax('Chênh lệch trung bình A − B (ms)'),min:-6,max:6,majorUnit:2},yAxis:{visible:false,min:0.5,max:1.5,majorGridlines:null}});
 txt(s,'KTC 95% [−4,349 ; 5,201] ms chứa 0',70,533,1120,50,34,C.white,true);
 txt(s,'Welch xét trung bình và dùng phương sai mẫu. Mann–Whitney xét hạng.\nCả hai đều chưa phát hiện khác biệt trong mẫu chi tiết này.',70,598,1114,65,25,C.muted);
 note(s,'Welch dùng sai số chuẩn căn của s_A²/40 + s_B²/40, với hai phương sai đều ước lượng từ mẫu. Không thay độ lệch chuẩn thật 10 ms của mô hình vào công thức. Sai số chuẩn là 2,3982 ms và bậc tự do Welch–Satterthwaite xấp xỉ 77,6038. P-value hai phía là 0,8594. Khoảng tin cậy 95% cho chênh lệch trung bình A−B chạy từ −4,3486 đến 5,2009 ms. Khoảng chứa 0 nên phù hợp với kết luận chưa bác bỏ. Welch không yêu cầu hai phương sai bằng nhau. Với dữ liệu lệch phải và n=40, xấp xỉ t vẫn cần thận trọng vì đuôi dài; mô phỏng lặp giúp đánh giá khả năng phát hiện trong đúng thiết kế này.', ['https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html']);
}
// 8 Monte Carlo
{
 const s=slide('Tỷ lệ phát hiện qua 200 lần mô phỏng','Mỗi lần tạo hai mẫu mới và chạy cả hai kiểm định hai phía tại α = 0,05');
 chart(s,'bar',{position:{left:69,top:199,width:620,height:397},categories:['Mann–Whitney','Welch'],series:[{name:'Tỷ lệ phát hiện',values:S.simulation_summary.map(r=>r.detection_rate),fill:C.cyan,points:[{idx:0,fill:C.cyan},{idx:1,fill:C.teal}]}],barOptions:{direction:'column',grouping:'clustered',gapWidth:95},hasLegend:false,xAxis:{...ax(''),majorGridlines:null},yAxis:{...ax('Tỷ lệ bác bỏ H₀'),min:0,max:1,majorUnit:.25,numberFormatCode:'0%'},dataLabels:{showValue:true,position:'outEnd',numberFormatCode:'0.0%',textStyle:{fontSize:27,fill:C.white,bold:true}}});
 table(s,[['Kiểm định','Phát hiện','KTC 95%'],['Mann–Whitney','153 / 200','70,2–81,8%'],['Welch','99 / 200','42,6–56,4%']],727,218,490,217,[205,125,160],24);
 txt(s,'Sai số Monte Carlo\n3,0 và 3,5 điểm phần trăm',731,475,473,95,28,C.white);
 txt(s,'Ước lượng lực kiểm định trong mô hình này, không phải tỷ lệ bác bỏ sai',70,618,1140,40,26,C.muted);
 note(s,'Mann–Whitney phát hiện 153 trong 200 lần, tỷ lệ 76,5%; Welch phát hiện 99 trong 200 lần, tỷ lệ 49,5%. Sai số Monte Carlo lần lượt khoảng 3,00 và 3,54 điểm phần trăm. Khoảng tin cậy Wilson 95% cho tỷ lệ phát hiện lần lượt 70,16–81,84% và 42,65–56,37%. Hai kiểm định chạy trên cùng bộ mẫu trong mỗi lần lặp để so sánh công bằng. Có 98 lần cùng phát hiện, 55 lần chỉ Mann–Whitney phát hiện, 1 lần chỉ Welch phát hiện và 46 lần cùng không phát hiện. Do mô hình thật có chênh lệch vị trí 4 ms, các tỷ lệ bác bỏ phản ánh lực kiểm định, không ước lượng sai lầm loại I. Kết quả không chứng minh Mann–Whitney luôn tốt hơn Welch trong mọi phân phối.');
}
// 9 Foundations and limits
{
 const s=slide('Kiến thức nền và giới hạn kết luận','Kết nối kiến thức chương 1–5 với kiểm định phi tham số ở chương 7');
 table(s,[['Kiến thức nền','Vai trò trong bài'],['Biến và mẫu độc lập','Độ trễ định lượng, hai nhóm phiên khác nhau'],['Biến ngẫu nhiên và phân phối','Phân phối mũ mô tả độ lệch phải'],['Thống kê mô tả','Trung bình, trung vị, SD, Q1, Q3 và IQR'],['Ước lượng và độ không chắc chắn','KTC Welch, SE Monte Carlo, KTC Wilson']],66,208,1148,291,[410,738],25);
 txt(s,'Không ghép cặp',69,540,525,48,32,C.cyan,true);
 txt(s,'Không có cùng phiên trước–sau\nGhép theo số thứ tự là tùy ý',69,591,563,70,26,C.white);
 txt(s,'Giới hạn áp dụng',705,540,501,48,32,C.teal,true);
 txt(s,'Mô phỏng n = 40, chỉ 200 lần lặp\nChưa có tải mạng, jitter hay mất gói',705,591,501,70,26,C.white);
 note(s,'Kiến thức chương 1–5 cung cấp cơ sở nhận diện biến, thiết kế mẫu, phân phối xác suất, tóm tắt dữ liệu và ước lượng độ không chắc chắn. Nội dung chính của đề là kiểm định phi tham số, đối chiếu với Welch. Hai nhóm gồm những phiên khác nhau và độc lập, nên không có cặp tự nhiên như cùng phiên trước–sau. Ghép giá trị A_i với B_i theo số thứ tự tạo quan hệ tùy ý. Do đó không dùng t ghép cặp hoặc Wilcoxon hạng có dấu. Kết luận chỉ áp dụng trong mô hình tạo dữ liệu với phân phối mũ cùng scale 10, mức dịch 4 ms và cỡ mẫu 40. Chưa thể suy luận về chi phí định tuyến, năng lượng, độ mất gói, jitter, tải mạng hoặc hiệu năng thực tế.');
}
// 10 Conclusion and proposed responsibilities
{
 const s=slide('Kết luận và phân công nhóm','Nhóm 8   Giảng viên Vũ Quang Minh');
 txt(s,'B thấp hơn 4 ms trong mô hình tạo dữ liệu',68,193,1135,53,36,C.cyan,true);
 txt(s,'Mẫu chi tiết chưa đủ bằng chứng khác biệt ở mức 5%.\nMô phỏng lặp ghi nhận Mann–Whitney phát hiện thường xuyên hơn.',68,258,1140,74,27,C.white);
 txt(s,'Phân công đề xuất 20% mỗi thành viên, nhóm xác nhận theo thực tế',68,350,1140,33,24,C.muted);
 table(s,[['Thành viên','MSSV','Nhiệm vụ đề xuất'],['Phạm Gia Minh','B24DCKD057','Thiết kế mô phỏng, quản lý dữ liệu gốc'],['Phương Bảo Vỹ','B24DCKD105','Lập trình Mann–Whitney và kiểm tra hạng'],['Nguyễn Đức Thành','B24DCKD085','Welch và khoảng tin cậy'],['Phan Nguyễn Trung Khánh','B24DCKD041','Mô phỏng 200 lần và trực quan hóa'],['Phùng Quốc Khánh Nam','B24DCKD059','Tổng hợp báo cáo và trình chiếu']],68,390,1147,253,[390,235,522],22);
 note(s,'Trong mô hình đề bài, B là phiên bản dịch trái 4 ms của A, vì vậy trung bình và trung vị thật đều thấp hơn 4 ms. Đây là đặc điểm của mô hình dùng để đánh giá phương pháp, không phải tham số được thay vào ước lượng mẫu. Mẫu chi tiết cố định seed chưa cho bằng chứng thống kê đủ mạnh bằng cả Mann–Whitney lẫn Welch. Mô phỏng 200 lần cho thấy Mann–Whitney phát hiện thường xuyên hơn trong thiết kế đang xét. Nếu chọn phương án chỉ theo độ trễ của mô hình này thì ưu tiên B. Để áp dụng thực tế cần dữ liệu đo độc lập, điều kiện mạng rõ ràng và ngưỡng cải thiện có ý nghĩa nghiệp vụ. Bảng phân công là đề xuất phân bổ đều 20%, nhóm cần xác nhận hoặc sửa theo công việc và đóng góp thực tế trước khi nộp.');
}

await fs.mkdir(buildDir,{recursive:true});
const outputPath=path.join(buildDir,'Bai_trinh_chieu_De_8_Nhom_8.pptx');
await(await PresentationFile.exportPptx(p)).save(outputPath);
console.log(outputPath);
