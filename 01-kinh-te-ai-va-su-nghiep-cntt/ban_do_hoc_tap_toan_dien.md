# 🧭 Bản Đồ Học Tập Toàn Diện
### Tư duy + Framework + Ngôn ngữ lập trình — Từ sinh viên IT → Product Builder

---

## Tổng Quan: 3 Trụ Cột Bạn Cần Xây

```
╔══════════════════════════════════════════════════════════════════╗
║                    BẠN MUỐN TRỞ THÀNH                          ║
║              "Người tạo ra giá trị bằng công nghệ"             ║
║                                                                  ║
║  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐     ║
║  │  🧠 TRỤ 1    │  │  💻 TRỤ 2    │  │  📈 TRỤ 3          │     ║
║  │              │  │              │  │                   │     ║
║  │  NỀN TẢNG   │  │  TECH STACK  │  │  BUSINESS &       │     ║
║  │  TƯ DUY     │  │  & NGÔN NGỮ  │  │  PRODUCT          │     ║
║  │              │  │  LẬP TRÌNH   │  │  FRAMEWORK        │     ║
║  │              │  │              │  │                   │     ║
║  │ • Cách suy   │  │ • HTML/CSS   │  │ • Tìm vấn đề     │     ║
║  │   nghĩ       │  │ • JavaScript │  │ • Validate ý      │     ║
║  │ • Ra quyết   │  │ • TypeScript │  │   tưởng           │     ║
║  │   định       │  │ • React      │  │ • Xây MVP         │     ║
║  │ • Giải quyết │  │ • Next.js    │  │ • Tìm khách hàng  │     ║
║  │   vấn đề     │  │ • Node.js    │  │ • Định giá        │     ║
║  │ • Tư duy     │  │ • PostgreSQL │  │ • Tăng trưởng     │     ║
║  │   hệ thống   │  │ • Git        │  │                   │     ║
║  └──────────────┘  └──────────────┘  └───────────────────┘     ║
║                                                                  ║
║  Hầu hết SV IT     SV IT học ở       Hầu như KHÔNG ai           ║
║  THIẾU cái này     trường cái này    dạy cái này ở trường       ║
╚══════════════════════════════════════════════════════════════════╝
```

> [!IMPORTANT]
> **Sự thật:** Trường đại học dạy bạn Trụ 2 (code). Nhưng để leo lên chuỗi giá trị, bạn cần **cả 3 trụ**. Trụ 1 (tư duy) quyết định bạn giải quyết đúng vấn đề. Trụ 3 (business) quyết định bạn kiếm được tiền từ giải pháp. Thiếu 1 trong 3 → mắc kẹt.

---

# 🧠 TRỤ 1: Nền Tảng Tư Duy & Mental Models

## Mental Model là gì?
Mental Model là **khung suy nghĩ** giúp bạn ra quyết định tốt hơn. Giống như lập trình có design pattern, cuộc sống và kinh doanh có mental model. Người giỏi không phải vì họ thông minh hơn — họ có **bộ công cụ suy nghĩ** tốt hơn.

---

### Model 1: 🔬 First Principles Thinking (Tư duy nguyên lý đầu tiên)

**Là gì?** Phân tích vấn đề về những sự thật cơ bản nhất, rồi xây lại từ đó — thay vì sao chép cách người khác đã làm.

```
TƯ DUY THÔNG THƯỜNG (suy nghĩ bằng phép tương tự):
"Tất cả mọi người làm landing page dùng WordPress"
→ "Vậy mình cũng dùng WordPress"

TƯ DUY FIRST PRINCIPLES:
"Khách hàng CẦN GÌ thực sự?"
→ "Họ cần 1 trang load nhanh, chuyển đổi cao, dễ sửa"
→ "WordPress có đáp ứng? Quá nặng, quá nhiều plugin"
→ "Giải pháp tốt hơn: static site + headless CMS"
→ Kết quả: nhanh hơn 5x, bảo mật hơn, khách hài lòng hơn
```

**Cách luyện tập hàng ngày:**
```
Mỗi khi gặp vấn đề, hỏi 5 lần "TẠI SAO":

Vấn đề: "Landing page của khách conversion thấp"
1. Tại sao? → Ít người click CTA
2. Tại sao? → CTA không nổi bật
3. Tại sao? → Bị lẫn với background
4. Tại sao? → Không có contrast trong design system
5. Tại sao? → Không ai kiểm tra accessibility contrast

→ Gốc rễ: Thiếu checklist contrast ratio
→ Giải pháp: Thêm bước kiểm tra WCAG vào quy trình
```

---

### Model 2: 🔄 Tư Duy Đảo Ngược (Inversion)

**Là gì?** Thay vì hỏi *"Làm sao để thành công?"*, hỏi *"Làm sao để chắc chắn THẤT BẠI?"* — rồi tránh những điều đó.

```
THƯỜNG: "Làm sao để SaaS của mình thành công?"
→ Quá mơ hồ, không biết bắt đầu từ đâu

ĐẢO NGƯỢC: "Làm sao để SaaS của mình CHẮC CHẮN thất bại?"
→ ✗ Xây tính năng không ai cần
→ ✗ Không nói chuyện với khách hàng trước khi code
→ ✗ Cố làm hoàn hảo trước khi launch
→ ✗ Giá quá rẻ, không đủ margin
→ ✗ Không tracking metrics

→ Bây giờ, ĐẢM BẢO bạn KHÔNG làm những điều trên
→ Xác suất thành công tăng đáng kể!
```

**Áp dụng cho freelance ngay:**
```
"Làm sao để mất khách hàng landing page?"
→ ✗ Giao trễ deadline
→ ✗ Không responsive mobile
→ ✗ Code xong biến mất
→ ✗ Không hỏi kỹ yêu cầu

→ Tránh 4 điều này = bạn đã tốt hơn 80% freelancer khác
```

---

### Model 3: 🎯 ICE Scoring (Ưu tiên hóa)

**Là gì?** Framework để quyết định *làm gì trước* khi có quá nhiều việc. Chấm điểm mỗi task theo 3 tiêu chí:

| Tiêu chí | Ý nghĩa | Thang điểm |
|---|---|---|
| **I**mpact (Tác động) | Task này mang lại giá trị lớn cỡ nào? | 1–10 |
| **C**onfidence (Tự tin) | Bạn tin chắc nó sẽ hiệu quả? | 1–10 |
| **E**ase (Dễ dàng) | Mất bao nhiêu công sức? | 1–10 |

**ICE Score = (I + C + E) / 3** → Làm task có score cao nhất trước

```
Ví dụ: Bạn có 4 việc muốn làm tuần này

| Việc                          | I  | C  | E  | Score |
|-------------------------------|----|----|----| ------|
| Học React                     | 9  | 8  | 5  | 7.3   | ← Làm 2
| Cải thiện portfolio           | 7  | 9  | 8  | 8.0   | ← Làm 1 ✅
| Học Docker                    | 5  | 4  | 3  | 4.0   | ← Chưa cần
| Đăng bài lên group tìm khách | 8  | 6  | 9  | 7.7   | ← Làm 3

→ Tuần này: Portfolio → React → Đăng bài → (Docker để sau)
```

---

### Model 4: 🔁 Build → Measure → Learn (Vòng lặp Lean)

**Là gì?** Framework cốt lõi từ **The Lean Startup** — xây nhanh, đo lường, học hỏi, lặp lại.

```
       ┌──────────┐
       │   IDEA   │  ← Giả thuyết: "Spa nhỏ cần app đặt lịch"
       └────┬─────┘
            │
            ▼
       ┌──────────┐
       │  BUILD   │  ← Xây MVP đơn giản nhất (1–2 tuần)
       │  (Xây)   │     Chỉ 1 tính năng cốt lõi
       └────┬─────┘
            │
            ▼
       ┌──────────┐
       │ MEASURE  │  ← Cho 5 spa dùng thử, đo:
       │  (Đo)    │     Có dùng không? Trả tiền không?
       └────┬─────┘
            │
            ▼
       ┌──────────┐
       │  LEARN   │  ← Họ thích gì? Ghét gì? Cần thêm gì?
       │ (Học)    │
       └────┬─────┘
            │
            └──── Quay lại BUILD với insight mới
```

**Quy tắc quan trọng:**
- MVP **không phải** sản phẩm kém chất lượng → là sản phẩm **tối thiểu đủ để TEST giả thuyết**
- Nếu không ai dùng MVP → đổi hướng nhanh (pivot), đừng cố code thêm tính năng
- **1 tuần code + 1 tuần đo > 3 tháng code + 0 ngày đo**

---

### Model 5: 🌐 Tư Duy Hệ Thống (Systems Thinking)

**Là gì?** Nhìn mọi thứ như một **hệ thống có liên kết**, không phải các phần riêng lẻ.

```
TƯ DUY THƯỜNG:
"Mình cần code landing page → giao cho khách → nhận tiền"
(Nhìn từng task riêng lẻ)

TƯ DUY HỆ THỐNG:
┌─────────────────────────────────────────────────┐
│                HỆ THỐNG KIẾM TIỀN               │
│                                                  │
│  Marketing ──→ Lead ──→ Tư vấn ──→ Hợp đồng    │
│      ↑                                    │      │
│      │         Code ──→ Bàn giao          │      │
│      │                      │             │      │
│      │                      ▼             │      │
│      │               Follow-up            │      │
│      │                      │             │      │
│      │                      ▼             │      │
│      └──── Giới thiệu ◄── Hài lòng ◄────┘      │
│                                                  │
│  Mỗi phần ảnh hưởng phần khác.                  │
│  Tối ưu 1 phần → cải thiện toàn bộ              │
└─────────────────────────────────────────────────┘
```

**Ứng dụng:** Khi landing page conversion thấp, đừng chỉ sửa button color. Hãy kiểm tra: traffic có đúng đối tượng không? Copy có match với ads không? Form có quá dài không? Trang có load nhanh trên mobile không? — Tất cả là 1 hệ thống.

---

### Model 6: 🚪 Type 1 vs Type 2 Decisions (Jeff Bezos)

**Là gì?** Phân loại quyết định thành 2 loại để biết khi nào cần suy nghĩ kỹ, khi nào cần hành động nhanh.

| | Type 1 (Cửa 1 chiều) | Type 2 (Cửa 2 chiều) |
|---|---|---|
| **Đặc điểm** | Không thể quay lại | Có thể quay lại, sửa được |
| **Ví dụ** | Chọn ngành học, ký hợp đồng 1 năm, chọn tech stack chính | Chọn color palette, thử 1 kênh marketing, giá dịch vụ |
| **Cách xử lý** | Suy nghĩ kỹ, nghiên cứu, hỏi ý kiến | **Làm nhanh!** Thử → sai → sửa |

> [!CAUTION]
> **Sai lầm lớn nhất của sinh viên:** Đối xử mọi quyết định như Type 1 → phân tích quá lâu → không hành động → bỏ lỡ cơ hội. 90% quyết định hàng ngày là Type 2 — **hãy làm nhanh và sửa sau**.

---

# 💻 TRỤ 2: Tech Stack & Ngôn Ngữ Lập Trình

## Triết lý chọn tech stack

```
❌ SAI: "Mình phải học HẾT mọi ngôn ngữ/framework"
✅ ĐÚNG: "Mình cần 1 stack ĐỦ để xây bất kỳ sản phẩm nào"

Nguyên tắc chọn stack:
1. Ít ngôn ngữ nhất có thể (giảm context switching)
2. Cộng đồng lớn (dễ tìm giải pháp, AI tools hỗ trợ tốt)
3. Full-stack bằng 1 ngôn ngữ (frontend + backend cùng 1 thứ)
4. Miễn phí hoặc free tier đủ dùng
```

## 🏗️ The "One-Language" Stack — JavaScript/TypeScript

### Tại sao JavaScript/TypeScript?

```
1 NGÔN NGỮ → TOÀN BỘ SẢN PHẨM

  ┌─────────────────────────────────────────────┐
  │              TypeScript / JavaScript          │
  │                                               │
  │  Frontend ──── React / Next.js                │
  │  Backend ───── Next.js API Routes / Node.js   │
  │  Database ──── Supabase (qua JS client)       │
  │  Mobile ────── React Native (sau này)         │
  │  Desktop ───── Electron (sau này)             │
  │  AI/ML ─────── TensorFlow.js / API calls      │
  │  Scripting ─── Node.js scripts                │
  │                                               │
  │  → Học 1 ngôn ngữ, xây TOÀN BỘ               │
  └─────────────────────────────────────────────┘
```

| Câu hỏi hay gặp | Trả lời |
|---|---|
| "Python thì sao?" | Python tuyệt cho AI/ML/Data, nhưng frontend phải dùng JS. Học Python **sau** khi vững JS, khi cần làm AI features |
| "Java/C# thì sao?" | Tốt cho enterprise, nhưng chậm để prototype. Không phù hợp cho solo founder/freelancer |
| "PHP thì sao?" | WordPress ecosystem lớn, nhưng xu hướng 2026 đang dịch chuyển. Biết thì tốt, nhưng không nên đầu tư sâu |
| "Có cần học C/C++?" | Ở trường thì học. Cho freelance/SaaS → KHÔNG cần |

---

## Lộ Trình Học 4 Phase

### Phase 1: Nền Tảng Web (Tháng 1–3) — BẮT BUỘC

> Bạn đang ở đây với landing page. Mục tiêu: làm vững nền.

```
TUẦN 1–4: HTML & CSS Chuyên Sâu
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ HTML5 semantic: <header>, <main>, <section>, <article>, <nav>
□ CSS Layout: Flexbox (bắt buộc) + Grid (bắt buộc)
□ Responsive: Media queries, mobile-first approach
□ CSS Variables (custom properties)
□ Animation: @keyframes, transition, transform
□ Accessibility cơ bản: ARIA labels, contrast ratio

📚 Tài nguyên:
  • freeCodeCamp → Responsive Web Design (MIỄN PHÍ, có chứng chỉ)
  • Kevin Powell YouTube → CSS God-level tutorials
  • web.dev/learn/css → Của Google, rất chuẩn

🎯 Bài tập: Tạo 3 landing page KHÔNG dùng framework CSS nào
```

```
TUẦN 5–8: JavaScript Chuyên Sâu
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Cơ bản: variables, functions, arrays, objects, loops
□ ES6+: arrow functions, destructuring, spread/rest, modules
□ DOM Manipulation: querySelector, addEventListener, createElement
□ Async: Promises, async/await, fetch API
□ Error Handling: try/catch
□ Local Storage & Session Storage

📚 Tài nguyên:
  • javascript.info → Sách giáo khoa JS tốt nhất (MIỄN PHÍ)
  • The Odin Project → JavaScript Path (MIỄN PHÍ)
  • Eloquent JavaScript → Sách online miễn phí

🎯 Bài tập: Tạo 1 ứng dụng To-do có filter, search, localStorage
```

```
TUẦN 9–12: Git & Công Cụ
━━━━━━━━━━━━━━━━━━━━━━━━
□ Git cơ bản: init, add, commit, push, pull, branch, merge
□ GitHub: Tạo repo, PR, Issues
□ VS Code: Extensions, shortcuts, debugging
□ Terminal/Command Line cơ bản
□ npm: install, scripts, package.json

📚 Tài nguyên:
  • GitHub Skills → learn.github.com (MIỄN PHÍ, interactive)
  • "Oh My Git!" → Game học Git (MIỄN PHÍ)

🎯 Bài tập: Push tất cả projects lên GitHub, viết README đẹp
```

---

### Phase 2: Framework Frontend (Tháng 4–6)

> Chuyển từ "code HTML tĩnh" sang "xây ứng dụng động"

```
TUẦN 13–16: React Fundamentals
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ JSX, Components, Props
□ State Management: useState, useEffect
□ Lists & Conditional Rendering
□ Forms & Controlled Components
□ useContext (chia sẻ state)
□ useRef, useMemo (performance)
□ Component composition patterns

📚 Tài nguyên:
  • react.dev → Official docs (TỰ HỌC TỐT NHẤT)
  • Scrimba → Learn React (MIỄN PHÍ, interactive)

🎯 Bài tập: Xây 1 ứng dụng thời tiết (fetch API + UI đẹp)
```

```
TUẦN 17–20: TypeScript + Next.js
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ TypeScript cơ bản: types, interfaces, generics
□ Next.js: Pages, Routing, Layouts
□ Server Components vs Client Components
□ Server Actions (thay thế API routes đơn giản)
□ Image Optimization, Font Optimization
□ SEO: Metadata API
□ Middleware cơ bản

📚 Tài nguyên:
  • nextjs.org/learn → Official tutorial (MIỄN PHÍ, rất tốt)
  • TypeScript Handbook → typescriptlang.org (MIỄN PHÍ)
  • Matt Pocock YouTube → TypeScript tips

🎯 Bài tập: Rebuild portfolio bằng Next.js, deploy lên Vercel
```

```
TUẦN 21–24: Styling & UI
━━━━━━━━━━━━━━━━━━━━━━━━
□ Tailwind CSS: utility-first, responsive, dark mode
□ shadcn/ui: component library (copy-paste, customizable)
□ Framer Motion: animations
□ Figma cơ bản: đọc design, export assets

📚 Tài nguyên:
  • tailwindcss.com/docs → Official docs
  • ui.shadcn.com → Component docs
  • Figma YouTube tutorials

🎯 Bài tập: Xây 1 landing page template cao cấp bán trên Gumroad
```

---

### Phase 3: Full-Stack & Database (Tháng 7–10)

> Đây là lúc bạn từ "frontend dev" → "product builder"

```
TUẦN 25–30: Supabase + PostgreSQL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Supabase setup & dashboard
□ PostgreSQL cơ bản: CREATE TABLE, SELECT, INSERT, UPDATE, DELETE
□ Relations: 1-to-many, many-to-many, foreign keys
□ Row Level Security (RLS) — bảo mật data
□ Supabase Auth: email, OAuth (Google, GitHub)
□ Supabase Storage: upload/quản lý files
□ Real-time subscriptions (live updates)

📚 Tài nguyên:
  • supabase.com/docs → Official docs (RẤT TỐT)
  • SQLBolt.com → Học SQL interactive (MIỄN PHÍ)
  • "Build a SaaS with Supabase" YouTube tutorials

🎯 Bài tập: Xây app ghi chú (auth + CRUD + real-time)
```

```
TUẦN 31–34: API & Integration
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ RESTful API concepts: GET, POST, PUT, DELETE
□ Next.js Route Handlers (API routes)
□ Middleware: authentication, rate limiting
□ Tích hợp 3rd-party APIs:
  • Stripe / VNPay (thanh toán)
  • Resend / Nodemailer (email)
  • OpenAI API (AI features)

📚 Tài nguyên:
  • stripe.com/docs → Stripe integration guide
  • developer.vnpay.vn → VNPay docs

🎯 Bài tập: Thêm Stripe checkout vào 1 ứng dụng
```

```
TUẦN 35–40: Node.js Backend (khi cần logic phức tạp)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Node.js runtime: modules, file system, streams
□ Express.js: routing, middleware, error handling
□ Validation: Zod hoặc Joi
□ Background jobs: cron, queues
□ WebSockets (real-time communication)

📚 Tài nguyên:
  • The Odin Project → NodeJS Path (MIỄN PHÍ)
  • Node.js official docs

🎯 Bài tập: Xây 1 REST API hoàn chỉnh cho blog system
```

---

### Phase 4: Deploy & Scale (Tháng 11–12)

> Ship sản phẩm ra thế giới thật

```
TUẦN 41–44: Deployment & DevOps
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Vercel: deploy Next.js (zero-config)
□ Custom domains & DNS
□ Environment variables & secrets
□ GitHub Actions: CI/CD cơ bản (auto deploy)
□ Error monitoring: Sentry (free tier)
□ Analytics: Vercel Analytics, GA4

📚 Tài nguyên:
  • vercel.com/docs → Official docs
  • GitHub Actions → docs.github.com

🎯 Bài tập: Deploy 1 SaaS MVP hoàn chỉnh, có custom domain
```

```
TUẦN 45–48: Tối ưu & Production
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Caching strategies
□ Rate limiting & security basics
□ Performance monitoring
□ SEO cho SaaS
□ Email transactional (welcome, reset password)
□ Legal: Privacy Policy, Terms of Service

🎯 Bài tập: SẢN PHẨM ĐẦU TIÊN CỦA BẠN LIVE! 🚀
```

---

## 🗂️ Bảng Tổng Hợp Tech Stack

```
┌─────────────────────────────────────────────────────────────┐
│                 THE PRODUCT BUILDER STACK                     │
│               (Tất cả bạn cần để xây SaaS)                  │
├────────────┬────────────────────────────────────────────────┤
│ Ngôn ngữ   │ TypeScript (JavaScript có types)              │
├────────────┼────────────────────────────────────────────────┤
│ Frontend   │ React → Next.js (App Router)                  │
├────────────┼────────────────────────────────────────────────┤
│ Styling    │ Tailwind CSS + shadcn/ui                      │
├────────────┼────────────────────────────────────────────────┤
│ Animation  │ Framer Motion                                 │
├────────────┼────────────────────────────────────────────────┤
│ Backend    │ Next.js API Routes + Server Actions            │
├────────────┼────────────────────────────────────────────────┤
│ Database   │ Supabase (PostgreSQL)                         │
├────────────┼────────────────────────────────────────────────┤
│ Auth       │ Supabase Auth                                 │
├────────────┼────────────────────────────────────────────────┤
│ Storage    │ Supabase Storage                              │
├────────────┼────────────────────────────────────────────────┤
│ Payments   │ Stripe (quốc tế) / VNPay (Việt Nam)          │
├────────────┼────────────────────────────────────────────────┤
│ Email      │ Resend                                        │
├────────────┼────────────────────────────────────────────────┤
│ Deploy     │ Vercel                                        │
├────────────┼────────────────────────────────────────────────┤
│ Version    │ Git + GitHub                                  │
├────────────┼────────────────────────────────────────────────┤
│ AI Tools   │ Cursor + GitHub Copilot + Claude              │
├────────────┼────────────────────────────────────────────────┤
│ Monitoring │ Sentry + Vercel Analytics                     │
├────────────┼────────────────────────────────────────────────┤
│ Chi phí    │ $0–30/tháng (hầu hết free tier)              │
└────────────┴────────────────────────────────────────────────┘
```

---

# 📈 TRỤ 3: Business & Product Frameworks

## Framework 1: The Mom Test (Tìm ý tưởng đúng)

**Quy tắc:** ĐỪNG BAO GIỜ hỏi *"Bạn có thích ý tưởng này không?"* — mọi người sẽ nói dối để làm bạn vui.

```
❌ CÂU HỎI TỆ                    ✅ CÂU HỎI TỐT
─────────────────────             ─────────────────────
"Bạn có dùng app đặt              "Lần cuối bạn quản lý
lịch cho spa không?"               lịch hẹn NTN? Kể cho
→ Họ sẽ nói "Có" cho vui           mình nghe cụ thể?"

"Bạn có trả 300k/tháng            "Tháng vừa rồi bạn đã
cho app này không?"                trả tiền cho tool nào
→ Lời hứa ≠ hành động              để quản lý spa?"

"Ý tưởng này hay không?"           "Bạn đang giải quyết
→ Ai cũng nói hay                  vấn đề X bằng cách
                                    nào? Điều gì khó nhất?"
```

**3 quy tắc vàng:**
1. Nói về **cuộc sống/công việc CỦA HỌ**, không phải ý tưởng của bạn
2. Hỏi về **quá khứ cụ thể**, không phải tương lai giả định
3. **Ít nói, nhiều nghe** — bạn đang thu thập data, không phải pitch

---

## Framework 2: Lean Canvas (Lên kế hoạch 1 trang)

Thay vì business plan 50 trang, dùng Lean Canvas — **1 trang A4 duy nhất**:

```
┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐
│  2. VẤN ĐỀ  │  4. GIẢI    │  3. GIÁ TRỊ │  9. LỢI THẾ │  1. PHÂN    │
│             │  PHÁP       │  ĐỘC NHẤT   │  CẠNH TRANH │  KHÚC KH    │
│ 3 vấn đề    │ 3 tính năng │ 1 câu mô tả │ Điều đối thủ│ Ai là khách │
│ lớn nhất    │ chính       │ tại sao      │ không thể   │ đầu tiên?   │
│             │             │ chọn bạn     │ copy được   │             │
├─────────────┤             ├─────────────┤             ├─────────────┤
│  8. CHỈ SỐ  │             │  5. KÊNH     │             │             │
│  THEN CHỐT  │             │ Khách tìm   │             │             │
│ Đo gì?      │             │ thấy bạn    │             │             │
│             │             │ bằng cách   │             │             │
│             │             │ nào?        │             │             │
├─────────────┴─────────────┴─────────────┴─────────────┴─────────────┤
│  7. CƠ CẤU CHI PHÍ                 │  6. DÒNG DOANH THU              │
│  Hosting, tools, thời gian          │  Giá bao nhiêu? Ai trả? NTN?   │
└─────────────────────────────────────┴─────────────────────────────────┘
```

---

## Framework 3: Jobs-to-be-Done (JTBD)

**Là gì?** Khách không mua sản phẩm — họ "thuê" sản phẩm để **hoàn thành 1 công việc**.

```
Ví dụ:
Khách KHÔNG mua "landing page"
Khách "thuê" landing page để "có thêm khách hàng mới từ Facebook Ads"

→ Khi hiểu "job" thật sự, bạn có thể:
  1. Tính giá theo giá trị (không phải theo giờ code)
  2. Đề xuất giải pháp tốt hơn (có khi không cần landing page!)
  3. Upsell dịch vụ khác (CRO, analytics, bảo trì)
```

**Công thức JTBD:**
```
"Khi [tình huống], tôi muốn [hành động], để tôi có thể [kết quả]"

Ví dụ:
"Khi tôi chạy ads Facebook cho spa,
 tôi muốn có 1 trang chuyên nghiệp để hướng traffic vào,
 để tôi có thể thu được SĐT khách quan tâm và gọi tư vấn"

→ Job = Thu SĐT khách quan tâm
→ Không phải Job = "Có website đẹp"
```

---

## Framework 4: Value-Based Pricing (Tính giá theo giá trị)

```
THAY VÌ:
"Em mất 20 giờ × 150k/giờ = 3 triệu"
→ Khách luôn muốn giảm giờ = giảm tiền bạn

HÃY:
"Landing page này giúp anh có thêm ~20 khách/tháng
× 500k/khách = 10 triệu doanh thu thêm/tháng.
Đầu tư 5 triệu 1 lần, hoàn vốn trong 2 tuần."
→ Khách thấy ROI rõ ràng = sẵn sàng trả
```

**Công thức:**
```
Giá dịch vụ = 10–20% × Giá trị bạn mang lại trong 1 năm

Ví dụ:
Landing page giúp khách thêm 10 lead/tháng × 12 tháng = 120 lead
Mỗi lead chuyển đổi 20% → 24 khách mới/năm
Mỗi khách trị giá 2 triệu → 48 triệu giá trị/năm
Giá hợp lý: 48tr × 15% = ~7 triệu
```

---

## Framework 5: Flywheel (Bánh đà tăng trưởng)

```
         ┌──── Sản phẩm tốt ◄────┐
         │                         │
         ▼                         │
   Khách hài lòng            Có tiền tái
         │                    đầu tư
         ▼                         │
   Giới thiệu người         Doanh thu
   mới (word-of-mouth)       tăng
         │                         │
         ▼                         │
   Thêm khách hàng ──────────────┘

Mỗi vòng quay → bánh đà NHANH HƠN
Năm 1: Bạn phải đẩy mạnh (tốn sức)
Năm 2: Bắt đầu tự quay
Năm 3+: Tự tăng tốc (compound growth)
```

---

# 📚 Thư Viện Sách — Đọc Theo Thứ Tự

### Đọc NGAY (trong 3 tháng tới)

| # | Sách | Tác giả | Dạy gì | Trang |
|---|---|---|---|---|
| 1 | **The Mom Test** | Rob Fitzpatrick | Cách hỏi khách để tìm ý tưởng thật | ~130 |
| 2 | **Getting Real** | 37signals | Xây sản phẩm gọn nhẹ, ship nhanh | ~190 |
| 3 | **The Lean Startup** | Eric Ries | Build-Measure-Learn loop | ~300 |

### Đọc trong 6 tháng tiếp

| # | Sách | Tác giả | Dạy gì |
|---|---|---|---|
| 4 | **$100M Offers** | Alex Hormozi | Tạo offer không thể từ chối |
| 5 | **Zero to One** | Peter Thiel | Tư duy tạo thứ chưa tồn tại |
| 6 | **Inspired** | Marty Cagan | Product management chuẩn mực |
| 7 | **The Pragmatic Programmer** | Hunt & Thomas | Triết lý craft phần mềm |

### Đọc khi đã có sản phẩm

| # | Sách | Tác giả | Dạy gì |
|---|---|---|---|
| 8 | **Continuous Discovery Habits** | Teresa Torres | Tích hợp user feedback liên tục |
| 9 | **Designing Data-Intensive Apps** | Martin Kleppmann | Kiến trúc hệ thống scale |
| 10 | **The Design of Everyday Things** | Don Norman | UX/Design thinking |
| 11 | **Competing in the Age of AI** | Iansiti & Lakhani | Xây business AI-native |
| 12 | **The Hard Thing About Hard Things** | Ben Horowitz | Thực tế khởi nghiệp |

---

# 🗓️ Bản Đồ Tổng Hợp 24 Tháng

```
         TƯ DUY              TECH                BUSINESS
         ──────              ────                ────────

Tháng    First Principles    HTML/CSS/JS         Bắt đầu
1–3      + Inversion         + Git               freelance
         + ICE Scoring                           landing page

Tháng    Systems Thinking    React               The Mom Test
4–6      + Type 1 vs 2      + Next.js            + ghi chú
         Decisions           + TypeScript         insight từ KH

Tháng    Build-Measure-      Supabase            Lean Canvas
7–10     Learn               + PostgreSQL         cho 1 ý tưởng
         (bắt đầu áp dụng)  + Auth + API         + validate

Tháng    Áp dụng tất cả     Deploy               Xây MVP
11–12    mental models       + CI/CD              đầu tiên
         vào sản phẩm thật  + Monitoring          + thu phí

Tháng    Iterate &           Tối ưu              Product-Market
13–18    improve             performance          Fit + Growth
         judgment            + scale

Tháng    Strategic           Thuê/AI             Scale hoặc
19–24    thinking            cho code routine     Pivot sản phẩm
         + leadership        + system design      + marketing
```

---

> [!TIP]
> **Bạn không cần nhớ hết.** Bookmark tài liệu này, quay lại mỗi tháng 1 lần để check tiến độ. Quan trọng nhất: **BẮT ĐẦU NGAY HÔM NAY** với việc nhỏ nhất — mở javascript.info, đọc 1 chương, code 1 bài tập. Mỗi ngày 1% tốt hơn, sau 1 năm bạn sẽ gấp 37 lần hiện tại.

> [!NOTE]
> **Tài nguyên tiếng Việt:** Nếu tiếng Anh còn khó, bắt đầu với freeCodeCamp (có bản tiếng Việt một phần), YouTube channel "Coders Tokyo", "F8 Official", "Evondev". Nhưng hãy **cố gắng chuyển sang tài nguyên tiếng Anh càng sớm càng tốt** — 90% kiến thức chất lượng cao bằng tiếng Anh.
