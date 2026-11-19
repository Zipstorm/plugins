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

## A PDF built in code

Where no HTML can be printed, build the PDF with ReportLab Platypus so text wraps
and pages flow: Letter, 0.6in margins, Times-Bold for headlines and big figures,
Helvetica elsewhere (text those cannot draw, such as Chinese, needs a registered
font with its glyphs; scripts that need shaping or right-to-left order, such as
Arabic, Hebrew and Hindi, get neither here, so print those from HTML), the tokens above as hex. These keep it from breaking:

- No content text at fixed coordinates. The only canvas drawing is a one-line
  footer (source, date, page number); anything longer ends the story.
- The band, cards and callouts are one-cell `Table`s (`colWidths=[doc.width]`
  for the band) with `BACKGROUND`, growing with their text; never a fixed-height
  rectangle filled with text; content longer than a page is split into several
  such tables. `--band` carries only white or `--peach` text;
  every other surface is `--card`, `--paper` or `--tint` with `--ink` or `--sub`.
- Every table cell is a `Paragraph`, `colWidths` sum to `doc.width`, and each
  column fits its header word. Links and company lists sit in a `Paragraph`.
- A pill is sized from its text (`stringWidth(text, font, 8) + 12`), or is plain
  small uppercase `--sub` text with no box.
- A big figure and its label are separate `Paragraph`s, in a column at least as
  wide as the label; no word breaks across lines. Each style's `leading` is at
  least 1.2 × its `fontSize`, so the figure never touches the text above or below.
- Charts no wider than `doc.width`, labels left of bars, the axis limit past the
  largest value so every bar ends inside its track; a bar's length is its value
  over that limit times the track, with no minimum width, and bars meant to be
  compared share one limit and one track width; a chart with negative values
  (net talent flow) draws from a zero baseline on one signed scale; heading,
  chart and caption in one `KeepTogether`.
- Type: headline 22pt, section 13pt, body 10/14pt, tables 9pt, captions 8pt;
  nothing under 8pt. Keep the page count asked for: cut the weakest section,
  never shrink type.
- Before handing over, render each page to an image and look: nothing clipped,
  spilling out of a box, past the margin or on a background near its own colour.
  Fix and rebuild if anything is.

## Never

Status uses words in neutral pills, not colour. No side rails, gradients, glows,
shadows, navy/orange dashboard palette or logo image. Wordmark: text “SeekOut,”
with “Out” in `--plum`.
