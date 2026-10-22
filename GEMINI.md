# GEMINI.md — Repository Guidelines & Workspace Instructions

## 1. Clean Repository & Workspace Hygiene (Strict Requirement)

- **No Temporary Files in Workspace:** Never create or leave temporary helper scripts, text dumps, scratch files, or extracted files (such as `*.txt`, scratch `*.py`, temporary `.json`, or debug logs) in the project workspace or Git repository.
- **Use Scratch Directory:** If scratch scripts or intermediate data dumps are temporarily necessary, store them exclusively in the agent brain scratch directory (`<appDataDir>/brain/<conversation-id>/scratch/`).
- **Immediate Cleanup:** Any temporary file created during an execution step that is not part of the required project deliverables must be deleted immediately before concluding the turn.
- **Repository Integrity:** Keep the Git tracking clean. Only official course deliverables, datasets, and project documentation should be committed or present in this repository.

---

## 2. Project Information & Coursework Context

- **Course:** Advanced Machine Learning (2026/2027) — Master's Degree
- **Project:** Modeling Recovery after Lower-Limb Musculoskeletal Injury
- **Group:** Group 14 (G14)
  - `fc68043` — David Belykh
  - `fc68080` — Matilde Quitério
  - `fc68091` — Ramyad Raadi

---

## 3. Deliverables & Notebook Standards

- **Naming Convention:** All milestone deliverables must follow `MX_G14.ipynb` (e.g., `M0_G14.ipynb`, `M1_G14.ipynb`, `M2_G14.ipynb`, etc.).
- **Full Execution:** All submitted notebooks must be completely executed from top to bottom with all explicit outputs, figures, metrics, and tables embedded directly in the `.ipynb` file.
- **Academic Rigor:** All discussions, interpretations, and conclusions must refer to explicit numerical outputs, empirical frequencies, and clinical reasoning rather than generic placeholder statements.
- **Generative AI Statement:** Every deliverable notebook must include the standard group declaration acknowledging tool usage and confirming student validation.
