// @ts-check
"use strict";

// Custom markdownlint rule: one sentence per line (semantic line breaks), ADR-021.
// Shared by the CLI (markdownlint-cli2) and the VSCode extension via `customRules`.
//
// It flags two shapes inside a paragraph:
//   (a) two sentences on one line — a sentence boundary mid-line;
//   (b) a sentence broken across lines — a non-final paragraph line that does not
//       end a sentence (Markdown joins the lines when rendering, so this is legal
//       Markdown but violates the house convention).
//
// Heuristic, with an abbreviation allow-list to keep false positives low; tune the
// lists against this repo's prose rather than chasing perfection.

const CLOSERS = "\"')\\]”’»"; // quotes/brackets allowed to trail a sentence end
const SENTENCE_END = new RegExp("[.!?][" + CLOSERS + "]*$");
const INTERNAL_BOUNDARY = new RegExp("[.!?][" + CLOSERS + "]*\\s+(?=[A-Z(“\"'«])");

// Words that end in "." but do not end a sentence.
const ABBR = "e\\.g|i\\.e|cf|vs|etc|al|ibid|no|nos|dr|mr|mrs|ms|st|fig|eq|ch|pp|vol|approx|ph\\.d|u\\.s|a\\.k\\.a";
const ENDS_ABBR = new RegExp("(?:^|\\s|\\()(?:" + ABBR + ")\\.$", "i");
const ENDS_INITIAL = /(?:^|\s)[A-Z]\.$/;      // "… by J." (an initial)
const ENDS_DECIMAL = /\d\.$/;                  // a bare number ending in "." e.g. "3."

function endsSentence(line) {
  return SENTENCE_END.test(line) &&
    !ENDS_ABBR.test(line) && !ENDS_INITIAL.test(line);
}

module.exports = {
  names: ["sentence-per-line", "MD100"],
  description: "One sentence per line (semantic line breaks, ADR-021)",
  tags: ["sentences", "line_length"],
  parser: "markdownit",
  function: (params, onError) => {
    const lines = params.lines;
    const tokens =
      (params.parsers && params.parsers.markdownit && params.parsers.markdownit.tokens) ||
      params.tokens ||
      [];
    for (const token of tokens) {
      if (token.type !== "paragraph_open" || !token.map) {
        continue;
      }
      const [start, end] = token.map; // [start, end) 0-based, end exclusive
      for (let i = start; i < end; i++) {
        const raw = lines[i];
        if (raw === undefined) {
          continue;
        }
        const line = raw.replace(/\s+$/, "");
        if (!line) {
          continue;
        }
        // (a) two sentences on one line.
        const m = INTERNAL_BOUNDARY.exec(line);
        if (m) {
          const before = line.slice(0, m.index + 1);
          if (!ENDS_ABBR.test(before) && !ENDS_INITIAL.test(before) && !ENDS_DECIMAL.test(before)) {
            onError({
              lineNumber: i + 1,
              detail: "Two sentences on one line — break at the sentence boundary.",
              range: [m.index + 1, 1]
            });
          }
        }
        // (b) a sentence broken across lines: a non-final line that does not end a
        // sentence. A trailing ":" introduces a list/quote and is exempt.
        const isLast = i === end - 1;
        if (!isLast && !endsSentence(line) && !line.endsWith(":")) {
          onError({
            lineNumber: i + 1,
            detail: "Line does not end a sentence — no line break before the sentence ends.",
            range: [line.length, 1]
          });
        }
      }
    }
  }
};
