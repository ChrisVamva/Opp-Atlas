# Migration Map

## Source vault: Opp Atlas

- `00-Index` → `00-Index` and `01-Operating-Model`
- `01-Project-State` → `01-Operating-Model` and `06-Decisions-and-Portfolio`
- `02-Opportunity-Atlas` → `02-Opportunity-World`
- `03-Research` → `04-Evidence-and-Research`
- `04-Experiments` → `05-Validation-and-Experiments`
- `05-Systems-and-Architecture` → `01-Operating-Model` and `07-Data-Layer`
- `06-Prompts-and-Agents` → operating protocols; keep separate from entity data
- `07-Commander-Deck` → `01-Operating-Model`, `03-Person-Atlas`, and `06-Decisions-and-Portfolio`
- `08-Reference` → `08-Templates`

## Source vault: Database strategy

- Working Environment Intelligence Database → `07-Data-Layer`
- Research Evidence Ledger → `04-Evidence-and-Research`
- Opportunity Atlas Analytics → `02-Opportunity-World` plus `07-Data-Layer`
- Continuity and Recovery → `06-Decisions-and-Portfolio`
- Tool Graph Discovery → future `07-Data-Layer` extension

## Migration rule

Copy and classify source notes; do not bulk-copy ambiguity into the canonical database. Preserve originals in the source vaults and record provenance on migrated notes.
