# SeekOut brand

Use for files without a supplied customer brand: documents, PDF/HTML, slides,
spreadsheets and charts.

## Palette

Warm paper, ink text, aubergine headline band; colour carries measurement meaning.

| Token | Value | Use |
| --- | --- | --- |
| `--paper` | `#faf8f6` | Background |
| `--card` | `#fff` | Cards/table body |
| `--ink` | `#1d1721` | Text/primary bars |
| `--sub` | `#69636f` | Captions/labels |
| `--faint` | `#9a94a0` | Minor labels |
| `--line` | `#e7e1da` | Row rules |
| `--rule` | `#d6cfc7` | Strong/dashed rules |
| `--band` | `#291242` | Headline band, white text |
| `--plum` | `#5e4db2` | Headline key figure, markers, links |
| `--brand` | `#781fb3` | Sparse brand accent |
| `--peach` | `#fec195` | Answer/hero figure on band |
| `--ember` | `#e98f4f` | Answer/as-written market bar on paper |
| `--lav` | `#b8acf6` | Measured context on band |
| `--mist` | `#d4cbe0` | Measured context on paper |
| `--track` | `#ece7e1` | Unfilled bar |
| `--tint` | `#f3f0ec` | Notes/callouts |
| `--tint-line` | `#e4ddd5` | Note border |
| `--chip` | `#efebe6` | Neutral pills |

## Type

Newsreader 400–500 for finding headlines/large figures; Inter 400–600 elsewhere.
Small uppercase `--sub` labels; tabular figures, right-aligned in tables.
Use Georgia/Arial respectively where docx/xlsx/pptx cannot embed fonts.

## Layout

1. Text wordmark left; kind/version/date right.
2. Role/company/market eyebrow, finding headline, short `--sub` introduction and req.
3. `--band` headline strip: `--peach` hero figure, up to three white supporting figures.
4. Findings sections: small plum-square/number kicker, source type (measured,
   inference or req), Newsreader heading. Hairline rows under an ink rule, no boxes.
5. Limits in `--tint`/`--tint-line` callouts; source ledger and small footer.

Include only supported content. HTML uses these CSS variables; print its PDF
from that HTML to preserve the design.

## Never

Status uses words in neutral pills, not colour. No side rails, gradients, glows,
shadows, navy/orange dashboard palette or logo image. Wordmark: text “SeekOut,”
with “Out” in `--plum`.
