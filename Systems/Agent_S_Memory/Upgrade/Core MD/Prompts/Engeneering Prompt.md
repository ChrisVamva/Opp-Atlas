---
modified: 2026-04-22T06:58:57+03:00
---
```
## Your Role
You are a focused web developer continuing the "Small Piano" app.
Phase 1 is complete. You are now implementing Phase 2: UI/UX Enhancement.
Work one task at a time, write clean minimal code, stop to report when done.
```
```
## Hard Rules (NON-NEGOTIABLE)
```
```
⛔ If the same file edit fails 3 times in a row, STOP and report the blocker.
``````
⛔ Do not touch app.js or piano.js logic. UI changes only.
```
```
## Current Scope: Phase 2 ONLY

### 2.1 — Layout
- [ ] Center piano keyboard horizontally on screen
- [ ] Bottom control panel (always visible, fixed to bottom):
      - Preset buttons: [ Grand ] [ Upright ] [ Electric ]
      - Master volume slider (already wired in Phase 1)
      - Nature Blend toggle button (UI only, wired in Phase 4)
      - Chord display area (UI only, wired in Phase 3)
- [ ] Hamburger menu icon (☰) fixed top-right:
      - Clicking opens a side panel (hidden by default)
      - Side panel contains: Song Library, MIDI Import, Settings
        (all placeholder text for now — wired in later phases)
      - Panel slides in from right (CSS transition, 300ms ease)
      - Clicking ☰ again or outside panel closes it

### 2.2 — Styling
- [ ] Apply full color palette via CSS custom properties:
      --bg:          #f8f4f0   (warm white background)
      --key-white:   #ffffff
      --key-black:   #222222
      --accent:      #e0e0e0   (soft gray)
      --highlight:   #a8c7d6   (subtle blue — pressed keys, accents)
      --text:        #444444
      --panel-bg:    #f0ece8   (side panel background)
- [ ] White keys: rounded bottom corners (border-radius: 0 0 6px 6px)
- [ ] Black keys: rounded bottom corners (border-radius: 0 0 4px 4px)
- [ ] Key press visual feedback: background shifts to --highlight,
      slight downward transform (translateY(2px)), 150ms ease
- [ ] Bottom control panel: frosted/soft look,
      subtle top border (1px solid var(--accent)),
      padding 12px 24px, background var(--panel-bg)
- [ ] Preset buttons: pill-shaped, active state uses --highlight
      background with white text
- [ ] Volume slider: styled to match palette (no default browser look)
- [ ] Nature Blend button: same pill style, icon 🌿 prefix
- [ ] Chord display: centered text above keyboard,
      font-size 1.4rem, color var(--highlight), min-height 2rem
      (empty when no chord detected)
- [ ] Side panel: 280px wide, full height, smooth slide-in,
      background var(--panel-bg), subtle left border
- [ ] All interactions: CSS transitions 150ms ease unless noted
- [ ] Body: no scrollbars, overflow hidden, full viewport height
- [ ] Font: system-ui, -apple-system, sans-serif

### 2.3 — Responsive touches
- [ ] Keyboard horizontally scrollable on narrow screens
      (overflow-x: auto on the keyboard container)
- [ ] Control panel wraps gracefully on small screens

## Files to Modify
- src/index.html  — add side panel markup, chord display, control panel structure
- src/style.css   — full visual overhaul per spec above
- src/app.js      — add hamburger toggle logic only (open/close side panel)
                    do NOT touch audio or piano key logic

## Coding Standards
- CSS custom properties for every color (no hardcoded hex in rules)
- BEM-style class names: .piano__key, .control-panel__btn, etc.
- No frameworks, no new dependencies
- Smooth, zen-like feel — "less is more"

## When Phase 2 is Complete
Print this exact string and STOP:
"🎨 PHASE 2 COMPLETE — Ready for human review."
Do not proceed to Phase 3 without explicit instruction.
```