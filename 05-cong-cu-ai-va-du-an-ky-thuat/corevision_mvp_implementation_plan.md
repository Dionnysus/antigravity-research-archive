# CoreVision — FEA Log Parser & 3D Stress Visualizer
## AI Riser Vietnam 2026 | #BuildwithGoogleAI

**Tagline:** Upload bất kỳ file log FEA nào → Nhận ngay Top 5 điểm ứng suất tới hạn trên bản đồ 3D.

---

## Problem Statement

Kỹ sư kết cấu và sinh viên phải đọc thủ công các file ASCII/CSV khổng lồ từ phần mềm mô phỏng (ANSYS, ABAQUS, SAP2000) để tìm các điểm đứt gãy tới hạn — mỗi phần mềm xuất ra một format khác nhau, không có tool nào đọc được tất cả.

## Solution (1-1-1)

- **1 vấn đề:** Parse FEA log bất kỳ format nào
- **1 tính năng AI:** Gemini 2.5 Pro trích xuất Top 5 Max Stress Nodes
- **1 luồng người dùng:** Upload → Analyze → View 3D

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Next.js 14 (App Router) |
| AI Core | Google Gemini 2.5 Pro (AI Studio API) |
| Database | Supabase (PostgreSQL + Storage) |
| 3D Render | Three.js + React Three Fiber |
| Styling | Tailwind CSS + shadcn/ui |
| Deployment | Docker → Google Cloud Run |
| Dev Tool | Antigravity IDE |

---

## Architecture

```
User
  ↓ Upload FEA file (any format)
Next.js Frontend
  ↓ POST /api/analyze
API Route (Next.js)
  ├── Store file → Supabase Storage
  ├── Send file content → Gemini 2.5 Pro
  │     "Extract Top 5 max stress nodes, return JSON"
  ├── Parse JSON response
  ├── Save session → Supabase DB
  └── Return structured data
Three.js Viewer
  ↓ Render 3D scatter plot with stress heatmap
```

---

## Database Schema (Supabase)

### Table: `analysis_sessions`
- `id` uuid PK
- `file_name` text
- `file_format` text (auto-detected by Gemini)
- `stress_unit` text (MPa, kPa, etc.)
- `threshold_value` float (user-defined or AI-detected)
- `created_at` timestamp
- `status` text (pending / done / error)

### Table: `stress_nodes`
- `id` uuid PK
- `session_id` uuid FK → analysis_sessions
- `node_id` text
- `x` float
- `y` float
- `z` float
- `stress_value` float
- `rank` int (1-5)
- `description` text (AI-generated explanation)

---

## Gemini Prompt Strategy

**System Prompt:**
```
You are a structural engineering AI assistant specializing in Finite Element Analysis (FEA) post-processing.
Your task is to parse FEA output files of ANY format and extract critical stress data.

RULES:
1. Return ONLY valid JSON. No explanations outside JSON.
2. Auto-detect the file format (ANSYS .rst text, ABAQUS .dat, SAP2000, custom ASCII matrix).
3. Find the TOP 5 nodes with highest Von Mises stress (or equivalent stress metric).
4. If coordinates are missing, estimate from node numbering patterns.
5. Always include a human-readable "reason" for why each node is critical.

OUTPUT FORMAT:
{
  "format_detected": "ANSYS RST text export",
  "stress_unit": "MPa",
  "threshold_applied": 25.0,
  "nodes": [
    {
      "node_id": "N4521",
      "x": 12.5,
      "y": 8.3,
      "z": 0.0,
      "stress_value": 47.2,
      "rank": 1,
      "reason": "Corner node at beam-column junction, stress concentration due to geometric discontinuity"
    }
  ]
}
```

---

## File Structure

```
corevision/
├── app/
│   ├── layout.tsx
│   ├── page.tsx                    # Main upload + viewer page
│   ├── globals.css
│   └── api/
│       ├── analyze/
│       │   └── route.ts            # Gemini integration
│       └── sessions/
│           └── route.ts            # CRUD for Supabase
├── components/
│   ├── FileUploader.tsx            # Drag & drop upload
│   ├── StressViewer3D.tsx          # Three.js 3D visualization
│   ├── ResultsPanel.tsx            # Ranked nodes list
│   └── SessionHistory.tsx          # Past analyses
├── lib/
│   ├── gemini.ts                   # Gemini API client
│   ├── supabase.ts                 # Supabase client
│   └── types.ts                    # TypeScript interfaces
├── public/
│   └── sample-fea.txt              # Sample FEA file for demo
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── package.json
```

---

## Verification Plan

### Automated
- `npm run build` — TypeScript compile check
- `docker build` — Container build validation

### Manual
1. Upload sample ANSYS-format FEA file → verify JSON response
2. Upload custom ASCII matrix → verify format-agnostic parsing
3. Verify 3D nodes render at correct coordinates
4. Test Supabase session save/retrieve
5. Deploy to Cloud Run, verify public URL accessible

---

## Execution Timeline

| Phase | Task | Est. Time |
|---|---|---|
| 1 | Project scaffold + dependencies | 30 min |
| 2 | Supabase schema + env setup | 20 min |
| 3 | Gemini API integration + prompt | 45 min |
| 4 | Upload API route | 30 min |
| 5 | Three.js 3D viewer component | 60 min |
| 6 | Main page UI + file uploader | 45 min |
| 7 | Results panel + session history | 30 min |
| 8 | Docker + deployment config | 20 min |
| 9 | Sample data + end-to-end test | 30 min |
| **Total** | | **~5.5 hours** |
