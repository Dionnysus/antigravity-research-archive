# CoreVision — Build Walkthrough

## ✅ What Was Built

CoreVision MVP — a **format-agnostic FEA stress analyzer** that uses **Gemini 2.5 Pro** to parse any Finite Element Analysis output file and visualize the top 5 critical stress nodes in an interactive **3D scene**.

---

## 📁 Project Structure

```
C:\Users\groul\.gemini\antigravity\scratch\
├── app/
│   ├── layout.tsx              ← Root layout (SEO, Google Fonts, dark theme)
│   ├── page.tsx                ← Main page (split-screen: sidebar + 3D viewer)
│   ├── globals.css             ← Premium dark theme with gradient mesh BG
│   └── api/
│       ├── analyze/route.ts    ← POST: upload file → Gemini → parse → save
│       └── sessions/route.ts   ← GET/DELETE: session history CRUD
├── components/
│   ├── FileUploader.tsx        ← Drag-and-drop with validation + animations
│   ├── StressViewer3D.tsx      ← Three.js interactive 3D stress visualization
│   ├── ResultsPanel.tsx        ← Ranked node list with bars + AI explanations
│   └── SessionHistory.tsx      ← Past analysis history with load/delete
├── lib/
│   ├── gemini.ts               ← Gemini 2.5 Pro client + FEA system prompt
│   ├── supabase.ts             ← Lazy-init Supabase client (server + client)
│   └── types.ts                ← TypeScript interfaces
├── public/
│   └── sample-fea.txt          ← Sample ANSYS-format FEA file for demo
├── supabase/
│   └── schema.sql              ← Database migration SQL
├── Dockerfile                  ← Multi-stage build for Cloud Run (port 8080)
├── .dockerignore
├── .env.example
├── next.config.ts              ← Standalone output + Three.js transpile
├── README.md                   ← Setup & deployment guide
└── package.json
```

---

## 🔧 Key Technical Decisions

| Decision | Rationale |
|---|---|
| **Gemini 2.5 Pro** (not Flash) | Long context window needed for large FEA files; stronger reasoning for format detection |
| **`next/dynamic` for Three.js** | Three.js is SSR-incompatible; dynamic import with `ssr: false` prevents hydration errors |
| **Lazy Supabase init** | Module-level `createClient()` crashes during `next build` when env vars aren't set |
| **`output: "standalone"`** | Required for Docker multi-stage build — produces minimal `server.js` bundle |
| **Imperative Three.js lines** | R3F's declarative `<bufferAttribute>` has TypeScript issues; `primitive` approach is cleaner |

---

## 🧪 Validation

| Check | Result |
|---|---|
| `npx tsc --noEmit` | ✅ Pass — 0 errors |
| `npm run build` | ✅ Pass — static pages generated |
| Route `/` | ✅ Static — prerendered |
| Route `/api/analyze` | ✅ Dynamic — server-rendered |
| Route `/api/sessions` | ✅ Dynamic — server-rendered |

---

## 🚀 Next Steps To Go Live

### 1. Setup Supabase (5 minutes)
1. Create project at [supabase.com](https://supabase.com)
2. Go to **SQL Editor** → paste contents of [`supabase/schema.sql`](file:///C:/Users/groul/.gemini/antigravity/scratch/supabase/schema.sql)
3. Copy keys from **Settings → API**

### 2. Get Gemini API Key (2 minutes)
1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Create key

### 3. Create `.env.local` (1 minute)
```bash
cp .env.example .env.local
# Fill in your 3 keys
```

### 4. Run Locally
```bash
npm run dev
# Open http://localhost:3000
# Upload public/sample-fea.txt to test
```

### 5. Deploy to Cloud Run
```bash
gcloud run deploy corevision \
  --source . \
  --region asia-southeast1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY=xxx,NEXT_PUBLIC_SUPABASE_URL=xxx,NEXT_PUBLIC_SUPABASE_ANON_KEY=xxx,SUPABASE_SERVICE_ROLE_KEY=xxx
```

---

## 🎨 UI Features

- **Dark glassmorphism theme** with gradient mesh background
- **Animated file uploader** with drag-and-drop and format badges
- **3D stress visualization** with pulsing glow effects, orbit controls, axis labels
- **Stress intensity heatmap** (amber → red color scale)
- **AI-generated explanations** for each critical node
- **Export to JSON** for downstream integration
- **Session history** with load/delete from Supabase
