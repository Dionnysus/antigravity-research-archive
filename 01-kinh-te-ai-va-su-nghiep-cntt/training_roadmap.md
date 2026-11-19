# 🏗️ Hệ Thống Bài Tập: Từ FCC Basic HTML → Web Chuẩn Công Nghiệp

> **Vai trò:** System Architect  
> **Trình độ đầu vào:** FCC Responsive Web Design — Basic HTML (65/137 steps)  
> **Mục tiêu cuối:** Tự thiết kế & triển khai Landing Page / Website chuẩn production  
> **Nguyên tắc thiết kế hệ thống:** Progressive Overload — mỗi sprint tăng độ phức tạp có kiểm soát

---

## 🗺️ Tổng quan kiến trúc lộ trình

```
[LEVEL 0] FCC Foundation (đang ở đây)
     ↓
[LEVEL 1] HTML Mastery Sprint          ← 1–2 tuần
     ↓
[LEVEL 2] CSS Core Sprint              ← 2–3 tuần
     ↓
[LEVEL 3] Layout Engineering Sprint   ← 2–3 tuần (Flexbox + Grid)
     ↓
[LEVEL 4] Responsive Design Sprint    ← 1–2 tuần
     ↓
[LEVEL 5] Component Build Sprint      ← 2–3 tuần
     ↓
[LEVEL 6] Landing Page Production     ← 2–4 tuần
     ↓
[LEVEL 7] Advanced Polish Sprint      ← ongoing
```

---

## ⚙️ LEVEL 1 — HTML Mastery Sprint
> **Mục tiêu:** Nắm vững ngữ nghĩa (semantic HTML) — nền tảng của mọi website chuẩn

### Kiến thức cần nắm
- Semantic tags: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`
- Form elements: `input`, `textarea`, `select`, `label`, `fieldset`
- Accessibility cơ bản: `alt`, `aria-label`, `role`
- HTML Boilerplate chuẩn (`meta viewport`, `lang`, `charset`, `og:tags`)

### Bài tập Sprint (làm theo thứ tự)

| # | Tên bài | Yêu cầu | Tiêu chí pass |
|---|---------|---------|---------------|
| H-01 | **Blog Post Page** | Dùng đúng semantic tags để cấu trúc 1 bài blog | Có `<article>`, heading hierarchy đúng (h1→h2→h3), không dùng `<div>` cho những gì có tag riêng |
| H-02 | **Contact Form** | Form đầy đủ: name, email, message, submit | `<label>` đúng for/id, placeholder, required attributes |
| H-03 | **Product Card List** | 3 card sản phẩm với image, title, price, button | `<figure>`, `<figcaption>`, `alt` text có nghĩa |
| H-04 | **Navigation Menu** | Nav với dropdown submenu bằng HTML thuần | `<nav>`, `<ul>/<li>`, nested list |
| H-05 | **Landing Page Skeleton** | HTML-only skeleton của 1 landing page đầy đủ | Có đủ: hero, features, testimonials, pricing, footer — đúng semantic |

### Checklist tự kiểm tra Level 1
- [ ] Validate HTML qua [validator.w3.org](https://validator.w3.org) — 0 error
- [ ] Mở DevTools → Accessibility tree → cấu trúc hợp lý
- [ ] Tắt CSS, page vẫn đọc được theo thứ tự logic

---

## ⚙️ LEVEL 2 — CSS Core Sprint
> **Mục tiêu:** Kiểm soát visual hoàn toàn — box model, typography, colors, spacing

### Kiến thức cần nắm
- Box model: `margin`, `padding`, `border`, `box-sizing: border-box`
- Selectors nâng cao: pseudo-class (`:hover`, `:focus`, `:nth-child`), pseudo-element (`::before`, `::after`)
- CSS Custom Properties (variables): `--color-primary`, `--spacing-md`
- Typography: `font-family` (Google Fonts), `line-height`, `letter-spacing`, `clamp()`
- Color: HSL color model, gradients

### Bài tập Sprint

| # | Tên bài | Yêu cầu | Tiêu chí pass |
|---|---------|---------|---------------|
| C-01 | **Design Token Sheet** | Tạo file `tokens.css` với variables cho màu, spacing, font | Có ít nhất: color palette (5 tones), spacing scale (xs→2xl), font scale |
| C-02 | **Typography Showcase** | Style các heading h1-h6, paragraph, blockquote, code | Dùng `clamp()` cho responsive font size |
| C-03 | **Button System** | 4 loại button: primary, secondary, outline, ghost | Có `:hover`, `:focus`, `:active`, `:disabled` state |
| C-04 | **Card Component** | Style card từ H-03 — shadow, border-radius, hover effect | Dùng `box-shadow` + `transform` cho hover |
| C-05 | **CSS-only Dark Mode** | Toggle dark/light bằng CSS `:has()` hoặc `[data-theme]` | Không dùng JavaScript |

### Checklist tự kiểm tra Level 2
- [ ] Không có magic numbers — dùng CSS variables
- [ ] Chạy Lighthouse → Performance ≥ 90
- [ ] Color contrast pass WCAG AA (dùng [coolors.co/contrast-checker](https://coolors.co/contrast-checker))

---

## ⚙️ LEVEL 3 — Layout Engineering Sprint
> **Mục tiêu:** Master Flexbox + CSS Grid — đây là kỹ năng phân biệt junior vs mid-level

### Kiến thức cần nắm
- Flexbox: `justify-content`, `align-items`, `flex-wrap`, `gap`, `flex-grow/shrink/basis`
- CSS Grid: `grid-template-columns`, `fr` unit, `auto-fit/auto-fill`, `minmax()`, `grid-area`
- Khi nào dùng Flex vs Grid (quy tắc 1D vs 2D)
- Positioning: `sticky`, `absolute`, `z-index` stacking context

### Bài tập Sprint

| # | Tên bài | Yêu cầu | Tiêu chí pass |
|---|---------|---------|---------------|
| L-01 | **Navbar** | Responsive navbar: logo trái, links phải | Dùng Flexbox, không dùng `float` |
| L-02 | **Holy Grail Layout** | Header + Sidebar trái + Content + Sidebar phải + Footer | Dùng CSS Grid |
| L-03 | **Auto-responsive Card Grid** | Grid cards tự co giãn không cần media query | `auto-fill` + `minmax(250px, 1fr)` |
| L-04 | **Bento Grid** | Layout dạng "bento box" — các card kích thước khác nhau | `grid-column/row: span N` |
| L-05 | **Complex Landing Section** | Hero section: text trái, hình phải, centered on mobile | Kết hợp Grid + Flexbox |

### Checklist tự kiểm tra Level 3
- [ ] Không dùng `position: absolute` để "workaround" layout
- [ ] Resize browser từ 320px → 1440px — không vỡ layout
- [ ] Dùng Firefox Grid Inspector kiểm tra visual

---

## ⚙️ LEVEL 4 — Responsive Design Sprint
> **Mục tiêu:** Mobile-first mindset — thiết kế từ nhỏ ra lớn

### Kiến thức cần nắm
- Mobile-first: viết CSS default cho mobile, dùng `min-width` để scale up
- Breakpoints chuẩn: `480px`, `768px`, `1024px`, `1280px`
- `clamp()` cho fluid typography/spacing
- Responsive images: `srcset`, `sizes`, `<picture>`
- Container queries (modern approach)

### Bài tập Sprint

| # | Tên bài | Yêu cầu | Tiêu chí pass |
|---|---------|---------|---------------|
| R-01 | **Responsive Navbar** | Mobile: hamburger menu / Desktop: horizontal | CSS-only với `:checked` trick hoặc JS tối giản |
| R-02 | **Fluid Typography System** | Headings scale mượt từ mobile → desktop | Dùng `clamp(min, preferred, max)` |
| R-03 | **Responsive Data Table** | Table đọc được trên mobile | Horizontal scroll hoặc card-transform technique |
| R-04 | **Responsive Image Gallery** | Gallery grid tự điều chỉnh | `auto-fill` + `aspect-ratio` |
| R-05 | **Full Responsive Audit** | Lấy bài L-05, làm responsive hoàn chỉnh | Pass DevTools Mobile Simulation trên 5 device sizes |

---

## ⚙️ LEVEL 5 — Component Build Sprint
> **Mục tiêu:** Xây dựng library component tái sử dụng — tư duy như frontend engineer

### Bài tập Sprint

| # | Tên bài | Mô tả |
|---|---------|-------|
| CO-01 | **Hero Section** | Full-width hero: headline, subtext, CTA button, background image/gradient |
| CO-02 | **Feature Section** | 3-column icon + text features, responsive 1-col mobile |
| CO-03 | **Testimonial Carousel** | CSS-only carousel hoặc vanilla JS minimal |
| CO-04 | **Pricing Table** | 3 plans, highlight "popular" plan, toggle monthly/yearly |
| CO-05 | **Footer** | Multi-column footer: links, social icons, newsletter form |
| CO-06 | **Modal / Dialog** | Dùng HTML `<dialog>` element — không dùng thư viện |
| CO-07 | **Sticky Navbar + Scroll Effect** | Navbar đổi style khi scroll qua hero |

---

## ⚙️ LEVEL 6 — Landing Page Production
> **Mục tiêu:** Tổng hợp tất cả — build 1 landing page hoàn chỉnh từ đầu

### Dự án cuối: "SaaS Landing Page"

**Cấu trúc bắt buộc:**
```
/project
  ├── index.html
  ├── css/
  │   ├── tokens.css       ← Design tokens
  │   ├── base.css         ← Reset + typography
  │   ├── components.css   ← Reusable components
  │   └── layout.css       ← Page layout
  ├── js/
  │   └── main.js          ← Navbar toggle, scroll effects
  └── assets/
      └── images/
```

**Sections bắt buộc:**
1. ✅ Navbar (sticky, responsive, scroll effect)
2. ✅ Hero (headline, subline, 2 CTAs, hero image/mockup)
3. ✅ Social proof (logos của khách hàng)
4. ✅ Features (3–6 features, icon + text)
5. ✅ How it works (3 bước, numbered)
6. ✅ Testimonials (3 cards)
7. ✅ Pricing (3 tiers, monthly/yearly toggle)
8. ✅ FAQ (accordion)
9. ✅ Final CTA section
10. ✅ Footer (multi-column)

**Tiêu chí production:**
- [ ] Lighthouse Performance ≥ 90
- [ ] Lighthouse Accessibility ≥ 90
- [ ] Lighthouse Best Practices ≥ 90
- [ ] Lighthouse SEO ≥ 90
- [ ] Mobile-first, pass trên tất cả kích thước màn hình
- [ ] Open Graph meta tags đầy đủ
- [ ] Không có console errors

---

## ⚙️ LEVEL 7 — Advanced Polish Sprint (Ongoing)
> Nâng trình lên senior-level

### Kỹ năng nâng cao
- **CSS Animations:** `@keyframes`, `animation`, scroll-driven animations
- **CSS Transitions:** Page transitions với View Transitions API
- **Performance:** Image optimization, lazy loading, font subsetting
- **Glassmorphism:** `backdrop-filter: blur()`, semi-transparent cards
- **Micro-interactions:** Hover states, loading states, skeleton screens
- **JavaScript:** Form validation, smooth scroll, intersection observer cho reveal animations

---

## 📏 Nguyên tắc vàng từ System Architect

> 1. **Build → Break → Rebuild**: Cố tình phá layout rồi fix — học nhanh hơn đọc docs
> 2. **Inspect, không đoán**: DevTools là bạn thân nhất, dùng mọi lúc
> 3. **Steal like an artist**: Clone UI của Stripe, Linear, Vercel — phân tích cách họ làm
> 4. **Semantic first, visual second**: Luôn viết HTML đúng trước khi thêm CSS
> 5. **Ship early**: Bài tập hoàn thành 80% còn hơn bài tập hoàn hảo 0%

---

## 📅 Gợi ý lịch học (3 tháng)

| Tuần | Level | Số bài |
|------|-------|--------|
| 1–2 | Level 1: HTML | H-01 → H-05 |
| 3–5 | Level 2: CSS | C-01 → C-05 |
| 6–8 | Level 3: Layout | L-01 → L-05 |
| 9–10 | Level 4: Responsive | R-01 → R-05 |
| 11–13 | Level 5: Components | CO-01 → CO-07 |
| 14–16 | Level 6: Landing Page | Full project |
| 17+ | Level 7: Polish | Ongoing |

---

*Cập nhật lần cuối: 2026-08-07 | Phiên bản: 1.0*
