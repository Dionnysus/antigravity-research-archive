# 🧠 Content Brain — Notion Workflow

> Copy toàn bộ document này vào Notion. Mỗi section `## DATABASE` tạo thành một **Notion Database**. Các template bên dưới tạo thành **Database Template** tương ứng.

---

## Kiến trúc tổng thể

```
📊 Market Intelligence DB
        ↓ (relation)
📋 Content Brief DB
        ↓ (relation)
🎬 Creative Blueprint DB
        ↓ (relation)
🎙️ Production DB
        ↓ (relation)
📈 Performance DB
        ↓ (feedback loop)
📊 Market Intelligence DB
```

---

## DATABASE 1: 📊 Market Intelligence

> Mỗi dòng = 1 sản phẩm/niche đã nghiên cứu

### Properties (Cột)

| Property | Type | Options / Mô tả |
|----------|------|-----------------|
| **Sản phẩm** | Title | Tên sản phẩm |
| **Trạng thái** | Select | `🔍 Đang nghiên cứu` · `✅ Xong` · `❌ Bỏ` |
| **Niche** | Select | Tự tạo: `Gia dụng` · `Skincare` · `Tech` · `Thời trang` · ... |
| **Đối tượng** | Text | VD: "Phụ nữ 20-30 tuổi, phòng trọ nhỏ" |
| **Mức nhu cầu** | Select | `🔥 Cao` · `⚡ Trung bình` · `❄️ Thấp` |
| **Khoảng giá** | Text | VD: "300k-800k" |
| **Pain Points** | Text | Liệt kê pain points, mỗi dòng 1 cái |
| **Objections** | Text | Lý do người mua do dự |
| **Content Gaps** | Text | Câu hỏi/chủ đề chưa ai làm |
| **Đối thủ đang nói gì** | Text | Tóm tắt góc tiếp cận đối thủ |
| **High-Intent Formats** | Multi-select | `So sánh trước/sau` · `Review thực tế` · `Unboxing` · `Test phá hủy` · `Day in my life` |
| **Keywords** | Text | Từ khóa trending |
| **Insight Summary** | Text | Tóm tắt 2-3 câu dạng tự nhiên |
| **Platform** | Multi-select | `TikTok` · `YouTube Shorts` · `Reels` |
| **Ngày nghiên cứu** | Date | |
| **Link nguồn** | URL | Link Shopee, TikTok trending, etc. |
| **→ Content Briefs** | Relation | → liên kết đến DB Content Brief |

---

### TEMPLATE: Nghiên cứu sản phẩm mới

Khi tạo dòng mới trong DB Market Intelligence, dùng template này cho phần **Notes/Page content**:

---

```
## 🔍 Nghiên cứu: [Tên sản phẩm]

### Bước 1: Nhu cầu thị trường
- [ ] Check Google Trends Vietnam cho keyword
- [ ] Search TikTok: "[sản phẩm] review" → ghi lại top 5 video (views, engagement)
- [ ] Search Shopee: "[sản phẩm]" → ghi lại số lượng đã bán của top 5 sản phẩm
- [ ] Check Google autocomplete: "[sản phẩm] có tốt không", "[sản phẩm] nên mua"

**Kết luận nhu cầu**: 🔥 Cao / ⚡ Trung bình / ❄️ Thấp
**Bằng chứng**:
- 

### Bước 2: Sản phẩm đang bán
- [ ] Top 5 sản phẩm Shopee (tên + giá + đã bán)
  1. 
  2. 
  3. 
  4. 
  5. 

- [ ] Tính năng nào được quảng cáo nhiều nhất?
- [ ] Khoảng giá phổ biến?

### Bước 3: Pain Points (từ reviews 1-3⭐ trên Shopee)
- [ ] Đọc 20-30 reviews thấp nhất
- [ ] Ghi lại CHÍNH XÁC ngôn ngữ người mua dùng

| Pain Point | Tần suất | Ngôn ngữ gốc |
|-----------|----------|---------------|
| | Cao/TB/Thấp | "..." |
| | | |
| | | |

### Bước 4: Objections (lý do không mua)
- [ ] Đọc comments dưới video review
- [ ] Đọc phần Q&A trên Shopee

1. 
2. 
3. 

### Bước 5: Đối thủ đang nói gì
- [ ] Top 5 creators làm nội dung về sản phẩm này

| Creator | Platform | Angle | Hook | Views | Có affiliate? |
|---------|----------|-------|------|-------|----------------|
| | | | | | |
| | | | | | |

### Bước 6: Content Gaps
- Câu hỏi nào trong comments CHƯA ai trả lời?
  1. 
  2. 
  3. 
- Góc nhìn nào CHƯA ai thử?
  1. 
  2. 
- Video nào view cao nhưng KHÔNG ra đơn? Tại sao?
  - 

### 📝 Insight Summary
> [Viết 2-3 câu tóm tắt dạng tự nhiên]
> VD: "Phụ nữ 20-30 tuổi đang tìm máy hút bụi mini vì phòng trọ nhỏ; 
> objection lớn nhất là lực hút yếu; video so sánh trước/sau có buyer intent cao."
```

---

## DATABASE 2: 📋 Content Brief

> Mỗi dòng = 1 video idea, gắn với 1 sản phẩm và 1 funnel stage

### Properties (Cột)

| Property | Type | Options / Mô tả |
|----------|------|-----------------|
| **Tiêu đề video** | Title | Hook/tiêu đề gợi ý |
| **Trạng thái** | Select | `💡 Idea` · `📝 Brief xong` · `🎬 Đang sản xuất` · `✅ Đã đăng` · `❌ Bỏ` |
| **← Sản phẩm** | Relation | → liên kết ngược về DB Market Intelligence |
| **Funnel Stage** | Select | `🟡 Awareness` · `🟠 Problem` · `🔴 Comparison` · `🟣 Demonstration` · `🔵 Conversion` |
| **Angle** | Text | Góc tiếp cận cụ thể |
| **Hook** | Text | Câu mở đầu 1-2 giây |
| **Framework** | Select | `AIDA` · `PAS` · `BAB` · `Star-Story-Solution` · `PASTOR` |
| **Pain Point** | Text | Pain point chính video giải quyết |
| **JTBD** | Text | Job To Be Done |
| **Promise** | Text | Lời hứa với người xem |
| **Evidence** | Text | Bằng chứng cần chuẩn bị |
| **CTA** | Text | Call to action |
| **Product Position** | Text | Sản phẩm xuất hiện như thế nào |
| **Platform** | Select | `TikTok` · `YouTube Shorts` · `Reels` |
| **Ưu tiên** | Select | `🔴 P0` · `🟠 P1` · `🟡 P2` |
| **→ Blueprint** | Relation | → liên kết đến DB Creative Blueprint |
| **Ngày tạo** | Date | Created time |

---

### TEMPLATE: Content Brief theo Funnel Stage

Khi tạo brief mới, copy template phù hợp với funnel stage:

---

#### 🟡 AWARENESS — "Khiến họ nhận ra vấn đề tồn tại"

```
## Brief: [Hook]

**Framework**: AIDA (Attention → Interest → Desire → Action)
**Mục tiêu**: Người xem nhận ra một vấn đề họ chưa từng nghĩ đến

### Chiến lược
- **Attention**: Thu hút bằng gì? (hình ảnh sốc / số liệu / câu hỏi)
- **Interest**: Tại sao họ nên quan tâm?
- **Desire**: Họ muốn gì sau khi biết?
- **Action**: Micro-CTA nhẹ (follow, xem tiếp)

### Fill-in
- **Angle**: 
- **Hook (1-2 giây đầu)**: 
- **Pain Point**: 
- **JTBD**: 
- **Promise**: 
- **Evidence cần chuẩn bị**: 
- **CTA**: (nhẹ — "follow để xem phần 2")
- **Sản phẩm xuất hiện**: (KHÔNG hoặc chỉ thoáng qua)

### Ví dụ
> Sản phẩm: Máy hút bụi mini
> Hook: "3 thứ khiến phòng trọ lúc nào cũng đầy bụi"
> Angle: Bụi ẩn trong phòng trọ mà mắt thường không thấy
```

---

#### 🟠 PROBLEM — "Khuấy đảo nỗi đau"

```
## Brief: [Hook]

**Framework**: PAS (Problem → Agitate → Solution)
**Mục tiêu**: Người xem cảm thấy vấn đề đang NGHIÊM TRỌNG hơn họ tưởng

### Chiến lược
- **Problem**: Đặt tên vấn đề rõ ràng
- **Agitate**: Khuấy đảo — hậu quả nếu không xử lý?
- **Solution**: Gợi ý hướng giải quyết (chưa nói sản phẩm cụ thể)

### Fill-in
- **Angle**: 
- **Hook**: 
- **Pain Point**: 
- **JTBD**: 
- **Promise**: 
- **Evidence**: 
- **CTA**: (nhẹ — "comment nếu bạn cũng gặp vấn đề này")
- **Sản phẩm xuất hiện**: (gợi ý giải pháp, chưa bán)

### Ví dụ
> Hook: "Tại sao chổi không xử lý được bụi trên giường?"
> Agitate: Bụi mite gây dị ứng, ngứa da, hắt hơi mỗi sáng
```

---

#### 🔴 COMPARISON — "Giúp họ chọn"

```
## Brief: [Hook]

**Framework**: BAB (Before → After → Bridge)
**Mục tiêu**: Người xem thấy sự khác biệt rõ ràng

### Chiến lược
- **Before**: Trước khi dùng / sản phẩm rẻ hơn
- **After**: Sau khi dùng / sản phẩm tốt hơn
- **Bridge**: Sản phẩm là cầu nối

### Fill-in
- **Angle**: 
- **Hook**: 
- **So sánh gì vs gì**: 
- **Tiêu chí so sánh** (3-5 tiêu chí):
  1. 
  2. 
  3. 
- **Evidence**: 
- **CTA**: (trung bình — "link ở bio")
- **Sản phẩm xuất hiện**: (trung tâm — so sánh trực tiếp)

### Ví dụ
> Hook: "Máy 300k và 800k khác nhau ở đâu?"
> Tiêu chí: lực hút, pin, tiếng ồn, phụ kiện, độ bền
```

---

#### 🟣 DEMONSTRATION — "Chứng minh nó hoạt động"

```
## Brief: [Hook]

**Framework**: Star-Story-Solution
**Mục tiêu**: Người xem TIN rằng sản phẩm giải quyết được vấn đề

### Chiến lược
- **Star**: Nhân vật/tình huống có thể relate
- **Story**: Câu chuyện test/trải nghiệm thực tế
- **Solution**: Kết quả sau khi dùng sản phẩm

### Fill-in
- **Angle**: 
- **Hook**: 
- **Test scenario**: (VD: "hút nệm sau 7 ngày không vệ sinh")
- **Metrics chứng minh**: (VD: lượng bụi hút được, thời gian, pin)
- **Objection handler**: (VD: "Nhưng lực hút có yếu không?")
- **Evidence**: 
- **CTA**: (mạnh hơn — "xem giá ở link bio")
- **Sản phẩm xuất hiện**: (trung tâm — demo trực tiếp)

### Ví dụ
> Hook: "Thử hút chiếc nệm này sau 7 ngày không vệ sinh"
> Objection: "Nhưng có một vấn đề..." → giải đáp
```

---

#### 🔵 CONVERSION — "Chốt đơn"

```
## Brief: [Hook]

**Framework**: PASTOR (Problem → Amplify → Story → Transformation → Offer → Response)
**Mục tiêu**: Người xem BẤM MUA

### Chiến lược
- **Problem**: Nhắc lại vấn đề (ngắn gọn)
- **Amplify**: Hậu quả nếu tiếp tục không giải quyết
- **Story**: Trải nghiệm cá nhân
- **Transformation**: Trước/sau
- **Offer**: Sản phẩm + ưu đãi
- **Response**: CTA rõ ràng

### Fill-in
- **Angle**: 
- **Hook**: 
- **Offer**: (giá, khuyến mãi, freeship?)
- **Urgency**: (hết hạn khi nào?)
- **Social proof**: (bao nhiêu người mua, rating?)
- **Evidence**: 
- **CTA**: (mạnh — "bấm giỏ hàng ngay")
- **Sản phẩm xuất hiện**: (hero — tên, giá, link rõ ràng)

### Ví dụ
> Hook: "Nếu phòng dưới 20m², tôi sẽ chọn chiếc nào?"
> Offer: 399k, freeship, giảm thêm 50k khi mua qua link
```

---

## DATABASE 3: 🎬 Creative Blueprint

> Mỗi dòng = 1 kế hoạch quay chi tiết, gắn với 1 Content Brief

### Properties (Cột)

| Property | Type | Options / Mô tả |
|----------|------|-----------------|
| **Tên video** | Title | = Hook từ brief |
| **← Brief** | Relation | → liên kết ngược về DB Content Brief |
| **Thời lượng (giây)** | Number | 30-60 |
| **Pacing** | Select | `⚡ Fast-cut` · `🎬 Documentary` · `📖 Storytelling` · `🎧 ASMR` |
| **Số cảnh** | Number | |
| **Trạng thái** | Select | `📐 Đang plan` · `✅ Xong` |
| **→ Production** | Relation | → liên kết đến DB Production |

---

### TEMPLATE: Shot List + Scene Planning

```
## 🎬 Creative Blueprint: [Hook]

### Thông tin chung
- **Thời lượng mục tiêu**: __ giây
- **Pacing**: ⚡ Fast-cut / 🎬 Documentary / 📖 Storytelling
- **Pattern interrupt**: Mỗi __s (khuyến nghị 5-8s)

### 📐 Shot List

| # | Giây | Hình ảnh | Lời nói / Âm thanh | Camera | Caption | B-roll | Ghi chú |
|---|------|---------|---------------------|--------|---------|--------|---------|
| 1 | 0–2s | | | | | | ⚡ HOOK — quyết định xem/lướt |
| 2 | 2–7s | | | | | | Reveal / Context |
| 3 | 7–15s | | | | | | Core content |
| 4 | 15–23s | | | | | | Objection / Tension |
| 5 | 23–35s | | | | | | Test / Evidence |
| 6 | 35–45s | | | | | | Verdict |
| 7 | 45–52s | | | | | | Ai nên / không nên mua |
| 8 | 52–57s | | | | | | CTA |

### Camera Guide
- `CU` = Close-up (chi tiết sản phẩm, bụi, kết quả)
- `MS` = Medium shot (người + sản phẩm)
- `WS` = Wide shot (bối cảnh phòng)
- `OH` = Overhead (nhìn từ trên xuống)
- `POV` = Point of view (góc nhìn người dùng)
- `ZI` = Zoom in (nhấn mạnh)

### 🎵 Nhịp điệu (Rhythm)

**Pattern Interrupts** (mỗi lần thay đổi để giữ viewer):
| Giây | Loại | Mô tả |
|------|------|-------|
| ~5s | | |
| ~12s | | |
| ~20s | | |
| ~30s | | |

Loại pattern interrupt:
- 🖼️ Visual shock (hình ảnh bất ngờ)
- ❓ Question (đặt câu hỏi)
- 🔊 Sound (âm thanh bất ngờ)
- 🔄 Perspective shift (đổi góc nhìn)
- 📝 Text pop (chữ xuất hiện đột ngột)

**Tension → Payoff**:
- Tension bắt đầu giây __: "__"
- Payoff giây __: "__"

### 📝 Subtitle Emphasis (từ cần highlight)
| Giây | Từ/cụm từ | Style |
|------|-----------|-------|
| | | bold / highlight / zoom / shake |
| | | |
| | | |
```

---

## DATABASE 4: 🎙️ Production

> Mỗi dòng = 1 video đang sản xuất

### Properties (Cột)

| Property | Type | Options / Mô tả |
|----------|------|-----------------|
| **Tên video** | Title | |
| **← Blueprint** | Relation | → liên kết ngược về DB Creative Blueprint |
| **Trạng thái** | Select | `📝 Script` · `🎤 Thu voice` · `📷 Quay footage` · `✂️ Edit` · `📝 Subtitle` · `🔊 Sound` · `✅ Xong` · `📤 Đã đăng` |
| **Script** | Text | Toàn bộ script |
| **Voice** | Select | `Azure` · `ElevenLabs` · `Tự đọc` |
| **Link drive** | URL | Link footage/assets |
| **Ngày deadline** | Date | |
| **Ngày đăng** | Date | |
| **Platform** | Multi-select | `TikTok` · `YouTube Shorts` · `Reels` |
| **→ Performance** | Relation | → liên kết đến DB Performance |

---

### TEMPLATE: Production Checklist

```
## 🎙️ Production: [Tên video]

### Checklist sản xuất

#### 1. Script ✍️
- [ ] Viết script theo shot list
- [ ] Đọc thành tiếng — nghe tự nhiên không?
- [ ] Đếm từ: __ từ ÷ 3 = __ giây (khớp với thời lượng?)
- [ ] Check: Hook có đủ mạnh?
- [ ] Check: CTA có phù hợp funnel stage?

**SCRIPT:**
```
[Dán full script ở đây]
```

#### 2. Voice 🎤
- [ ] Chọn giọng: Azure / ElevenLabs / Tự đọc
- [ ] Generate voice
- [ ] Nghe lại: tốc độ OK? Ngữ điệu tự nhiên?
- [ ] Cắt silence / chỉnh timing

#### 3. Footage 📷
- [ ] Quay theo shot list
- [ ] Check: đủ B-roll?
- [ ] Check: close-up sản phẩm rõ nét?
- [ ] Check: ánh sáng OK?
- [ ] Screen recording (nếu cần)

#### 4. Edit ✂️ (CapCut)
- [ ] Import voice + footage
- [ ] Sync voice với hình
- [ ] Cắt theo shot list timing
- [ ] Thêm transitions
- [ ] Thêm zoom / pan effects
- [ ] Pattern interrupts đúng vị trí?

#### 5. Subtitle 📝
- [ ] Auto-generate subtitle
- [ ] Fix lỗi nhận dạng
- [ ] Highlight từ khóa theo Subtitle Emphasis list
- [ ] Font + màu consistent

#### 6. Sound Design 🔊
- [ ] Background music (nhẹ, không lấn voice)
- [ ] Sound effects tại pattern interrupts
- [ ] Volume balance: voice > music > SFX

#### 7. Final Check ✅
- [ ] Xem lại toàn bộ video 1 lần
- [ ] 2 giây đầu có hook không?
- [ ] Có muốn lướt không? (nếu CÓ → fix)
- [ ] CTA rõ ràng?
- [ ] Sản phẩm xuất hiện đúng lúc?
- [ ] Export đúng tỉ lệ 9:16, 1080p
```

---

## DATABASE 5: 📈 Performance

> Mỗi dòng = 1 video đã đăng, track metrics theo thời gian

### Properties (Cột)

| Property | Type | Options / Mô tả |
|----------|------|-----------------|
| **Tên video** | Title | |
| **← Production** | Relation | → liên kết ngược về DB Production |
| **Funnel Stage** | Select | (rollup từ Brief) |
| **Hook used** | Text | (rollup từ Brief) |
| **Angle used** | Text | (rollup từ Brief) |
| **Ngày đăng** | Date | |
| **Platform** | Select | `TikTok` · `Shorts` · `Reels` |
| **Impressions** | Number | |
| **Retention 2s (%)** | Number | % viewer còn xem tại 2s |
| **Retention 5s (%)** | Number | % viewer còn xem tại 5s |
| **Avg Watch Time (s)** | Number | |
| **Completion Rate (%)** | Number | |
| **Likes** | Number | |
| **Comments** | Number | |
| **Shares** | Number | |
| **Saves** | Number | |
| **Product Clicks** | Number | |
| **Add to Cart** | Number | |
| **Orders** | Number | |
| **Commission (VNĐ)** | Number | |
| **Engagement Rate (%)** | Formula | `(Likes + Comments + Shares + Saves) / Impressions * 100` |
| **Conversion Rate (%)** | Formula | `Orders / Product Clicks * 100` |
| **Revenue/View** | Formula | `Commission / Impressions` |
| **Verdict** | Select | `🔥 Winner` · `👍 OK` · `😐 Trung bình` · `❌ Flop` |
| **Learning** | Text | Bài học rút ra |

---

### TEMPLATE: Performance Review (tuần)

```
## 📈 Weekly Review: Tuần [DD/MM] – [DD/MM]

### Top Performers
| # | Video | Views | Watch Time | Orders | Tại sao thành công? |
|---|-------|-------|------------|--------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### Flops
| # | Video | Views | Watch Time | Vấn đề ở đâu? |
|---|-------|-------|------------|----------------|
| 1 | | | | |
| 2 | | | | |

### Pattern Analysis

**Hook nào hiệu quả?**
- Retention 2s cao nhất: "__" (__ %)
- Retention 2s thấp nhất: "__" (__ %)
- → Insight: 

**Funnel stage nào convert?**
- Nhiều orders nhất: __ stage
- Nhiều views nhất: __ stage
- → Insight: 

**Content type nào nên làm thêm?**
1. 
2. 

**Content type nào nên dừng?**
1. 

### Hypotheses Update

| Hypothesis | Kết quả | Status |
|-----------|---------|--------|
| | | ✅ Confirmed / ❌ Rejected / 🔄 Chưa đủ data |
| | | |

### Action Items cho tuần tới
- [ ] 
- [ ] 
- [ ] 
```

---

## DATABASE 6: 💡 Hypothesis Tracker

> Track các giả thuyết về content performance

### Properties (Cột)

| Property | Type | Options / Mô tả |
|----------|------|-----------------|
| **Giả thuyết** | Title | VD: "Video so sánh trước/sau sẽ có watch time > 15s" |
| **Metric** | Select | `2s Retention` · `5s Retention` · `Watch Time` · `Completion` · `Product Clicks` · `Orders` · `Engagement` |
| **Target** | Text | VD: "> 15s", "> 70%" |
| **Status** | Select | `🧪 Testing` · `✅ Confirmed` · `❌ Rejected` · `🔄 Inconclusive` |
| **Videos tested** | Relation | → DB Performance |
| **Actual Result** | Text | |
| **Learning** | Text | Bài học rút ra |
| **Ngày tạo** | Date | |

---

## 🔄 WORKFLOW: Quy trình từ A-Z cho 1 sản phẩm

### Sprint 1 tuần cho 1 sản phẩm

```
THỨ 2: MARKET INTELLIGENCE (2-3 giờ)
├─ Tạo dòng mới trong DB Market Intelligence
├─ Dùng template "Nghiên cứu sản phẩm mới"
├─ Hoàn thành 6 bước nghiên cứu
└─ Viết Insight Summary

THỨ 3: CONTENT STRATEGY (2-3 giờ)
├─ Từ Insight → tạo 5 dòng trong DB Content Brief
│   ├─ 1x Awareness (AIDA)
│   ├─ 1x Problem (PAS)
│   ├─ 1x Comparison (BAB)
│   ├─ 1x Demonstration (Star-Story-Solution)
│   └─ 1x Conversion (PASTOR)
├─ Mỗi brief: điền đầy đủ template theo funnel stage
└─ Chọn 2-3 briefs ưu tiên cao nhất để sản xuất trước

THỨ 4: CREATIVE PLANNING (1-2 giờ)
├─ Với mỗi brief ưu tiên → tạo Creative Blueprint
├─ Điền shot list chi tiết (giây, hình, lời, camera)
├─ Xác định pattern interrupts
├─ Xác định subtitle emphasis
└─ Viết script hoàn chỉnh

THỨ 5-6: PRODUCTION (4-6 giờ)
├─ THỨ 5 sáng: Thu voice (Azure/ElevenLabs)
├─ THỨ 5 chiều: Quay footage theo shot list
├─ THỨ 6 sáng: Edit trên CapCut
├─ THỨ 6 chiều: Subtitle + Sound design
└─ Final check toàn bộ

THỨ 7: PUBLISH + TRACK
├─ Đăng video theo lịch
├─ Tạo dòng trong DB Performance
└─ Ghi lại hypotheses cần đo

CHỦ NHẬT: REVIEW
├─ Cập nhật metrics từ tuần trước
├─ Viết Weekly Performance Review
├─ Update Hypothesis Tracker
└─ Plan sản phẩm/niche cho tuần tiếp theo
```

---

## 🎯 Dashboard Views (tạo trong Notion)

### View 1: Content Pipeline (Board)
- Group by: **Trạng thái**
- Columns: `💡 Idea` → `📝 Brief xong` → `🎬 Đang sản xuất` → `✅ Đã đăng`
- Filter: Tuần này

### View 2: Funnel Overview (Table)
- Group by: **Funnel Stage**  
- Show: Sản phẩm, Hook, Trạng thái, Platform
- Tổng quan: có đủ 5 stages cho mỗi sản phẩm không?

### View 3: Performance Leaderboard (Table)
- Sort by: **Commission** descending
- Show: Tên video, Funnel Stage, Views, Orders, Commission, Verdict
- Filter: 30 ngày gần nhất

### View 4: Hypothesis Board (Board)
- Group by: **Status**
- Columns: `🧪 Testing` → `✅ Confirmed` → `❌ Rejected`

---

## 🧠 Quick Reference: Chọn Framework theo Funnel

| Viewer đang ở đâu? | Funnel Stage | Framework | Ví dụ Hook |
|--------------------|-------------|-----------|------------|
| Chưa biết có vấn đề | 🟡 Awareness | AIDA | "3 thứ khiến phòng trọ lúc nào cũng đầy bụi" |
| Biết vấn đề, chưa tìm giải pháp | 🟠 Problem | PAS | "Tại sao chổi không xử lý được bụi trên giường?" |
| Đang so sánh các lựa chọn | 🔴 Comparison | BAB | "Máy 300k và 800k khác nhau ở đâu?" |
| Muốn thấy bằng chứng | 🟣 Demo | Star-Story-Solution | "Thử hút chiếc nệm này sau 7 ngày không vệ sinh" |
| Gần quyết định mua | 🔵 Conversion | PASTOR | "Nếu phòng dưới 20m², tôi sẽ chọn chiếc nào?" |
