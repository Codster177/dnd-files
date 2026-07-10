# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not code** — it is an Obsidian vault of worldbuilding and campaign notes for a homebrew
tabletop RPG (a "Kids on Shrooms"-style system) set in a modern world where magic is real but secret.
There are no build, lint, or test commands. "Working in this repository" means reading, editing, and
creating Markdown notes while preserving the vault's conventions. Changes are saved as plain `.md`
files and committed with git like any other content.

This vault ("Kids on Shrooms") is one campaign among sibling vaults under the same parent repo
(e.g. a separate "Hellspire" vault); keep edits scoped to this vault unless asked otherwise.

## Organization model

- **No YAML frontmatter, no `#tags`, no callouts.** Notes begin directly with prose or a `##` header.
  A leading/standalone `---` is a horizontal-rule divider, never metadata.
- Classification is done entirely through **folder hierarchy + `[[wikilinks]]`**. When adding a note,
  place it in the correct folder and link it generously. Almost every proper noun (person, place,
  organization, lore concept, session) is a wikilink on first mention.
- Link forms in use: plain `[[Magic]]`, aliased `[[Study Hall - 6|Study Advisement]]`, and heading
  links `[[Astaria#The HUMI|The HUMI]]`.
- Many notes are deliberate stubs (empty or one line). Don't treat an empty note as broken.
- **Write one line per paragraph — do not hard-wrap prose at a fixed column.** These notes are read
  and edited in Obsidian, where mid-sentence line breaks show up as awkward chops in the editor. Let
  the editor soft-wrap. (This applies to vault notes; `CLAUDE.md` itself is exempt since it is not
  viewed through Obsidian.)

### Top-level folders

- `People/` — characters, split by role: `Player Characters/`, `Students/`, `Teachers/`,
  `Other Adults/`, `Families/`, `Witches/`, `Wizards/`, `Spirits/`, `Great Spirits and Divinity/`.
  Player-character files are named `Name (PlayerName).md`.
- `Lore/` — worldbuilding backbone (`Avira.md`, `Magic.md`, `The Kamihara.md`), plus `History/`
  (a 6-era timeline) and `Spellcasters/` (Sorcerers/Witches/Warlocks/Wizards).
- `Countries/` — nations, grouped `First World Nations/`, `Orochi Nations/`, `Dead Nations/`.
- `Locations/` — settlements grouped per country: `Locations/<Country>/Cities/` and
  `Locations/<Country>/Towns/`. National capitals always go under `Cities/`, whatever their size.
  A city-state may sit directly under its country folder (e.g. `Locations/Zimino/`). A settlement
  gets its own subfolder (like `Lake Prospect/`, which holds `Schools/`, `City Life/`, `Nature/`)
  only once it accumulates subnotes.
- `Organizations/` (Corporations/Global/Religions/School), `Classes/` (school
  curriculum, named `Subject - Period.md`), `System Design/` (homebrew mechanics), `Tools/` (GM aids),
  `Session Logs/`, `Obsidian Stuff/Images/` (pasted asset storage).

## Scratchpad — `Tools/Claude Notes/`

Use the `Tools/Claude Notes/` folder for temporary, drafted, or in-progress notes about the current
task — so real vault notes are never cluttered with unfinished information. Give each task its own
`.md` file in that folder, and break its content into the same labeled blocks the destination note
uses (e.g. `### Backstory:`, `### Relationships:`), keeping full detail while drafting. Delete a
task's file once its information has been finalized and moved into its permanent note.

## Note templates and conventions

Follow the existing templates when creating notes:

- **Characters** — copy the relevant block from `People/Templates.md` (Student / Adult / Spirit).
  Standard sections in order: intro paragraph (name, player in parens for PCs, in-world birthday,
  age) → `## Gameplay Mechanics:` (a stat table of Strength/Dexterity/Intelligence/Constitution/
  Charisma/Wisdom — plus a Magic row for casters — with "Current Die"/"Stat Modifier"/"Magic Modifier"
  columns, header cell linking `[[Stats]]`; then `### Strengths:` bullets with bold ability labels)
  → `## Character Breakdown:` (fixed interview: year, appearance, personality, cliques, goals, fears)
  → `## Backstory:` → `## Schedule:` (Periods 1–6 table linking `Classes/` notes) → `## Rumors:`
  (Good/Bad/Fake bullets) → `## Relationships:` (grouped `### Players:`/`### Family:`/`### School:`/
  `### Social:`; each entry links the person and nests an `Actual play history:` list of `[[Session N]]:`
  excerpts).
- **Nations** — copy `Countries/Country Template.md` (Organization Structure, Culture, Military,
  Technological and Scientific Level, Religion, Laws; deep files add a `# SECRETS` section).
- When creating notes, seperate information into their respective blocks (**Characters** having
  `## Backstory:`, `## Relationships:`, ect.). However, include as much information as possible when
  depicting these subcategories. It is prefered to have a very large subcategory containing all of the
  information related to the subcategory, as opposed to a short summarized subcategory that fits the page
  better. Include as much information as possible.

## Writing style

Notes should read like a person wrote them, not an assistant. Concretely:

- **Commit to specifics.** Prefer one vivid, concrete detail (a name, a smell, a specific grudge, an
  exact sum of money) over three abstract ones. Invent grounded texture rather than gesturing at it
  with words like "ancient," "mysterious," "powerful," "renowned," or "a rich history."
- **Have a point of view.** Write with the confidence of an in-world chronicler or an opinionated GM.
  Don't hedge ("perhaps," "it could be said," "in some ways") or present every trait as neatly
  balanced. Characters and factions can be biased, wrong, petty, or unfair — say so plainly.
- **Vary the rhythm.** Mix short punchy sentences with longer ones. Avoid the steady, even cadence and
  the reflexive rule-of-three list ("brave, loyal, and kind"). One good adjective beats three.
- **Cut the AI tells.** No summary/restatement sentence at the end of a section. No "it's not just X,
  it's Y" antithesis. No "stands as a testament to," "weaves a tapestry," "delve," "navigate the
  complexities of," "little did they know," or "at the end of the day." Don't over-explain a joke or
  moralize about a character's choices.
- **Don't editorialize about the writing.** State events and facts directly; skip meta-commentary like
  "this adds depth" or "which makes them a compelling character."
- **Match the neighbors.** Before writing, skim an existing rich note (e.g. a fleshed-out Player
  Character or `Countries/First World Nations/Astaria.md`) and echo its voice, diction, and humor
  rather than importing a generic encyclopedia tone.
- **Avoid overuse of the em dash (—).** It's the loudest AI tell of all. A page peppered with em
  dashes reads as machine-written even when everything else is clean. Most of the time a comma,
  period, colon, or parentheses does the job better — so reach for those first, and let a sentence
  simply end instead of tacking on a dashed afterthought. Keep the em dash for the occasional real
  interruption or hard pivot, and rarely more than one per paragraph.

## Naming conventions (from `Tools/Language and Naming Conventions.md`)

Invented names should match each nation's real-world linguistic basis:

- Astaria → modern American names · Jiā → Chinese · Neridora → Vietnamese/Moroccan ·
  Palicia → Greek · The Grand Aviran Empire (dead) → mystical / Old English. (Rane: undefined.)

## In-world calendar

Dates use a custom calendar — months follow two cycles of seasons to form a year (the months
start with `First Spring`, and end with `Second Winter`), each month has exactly 50 days, and
`BA`/`AV` eras (Before Avira / after). Example: "8/36/1603, or the 36th of Second Winter, 1603".
Preserve this format; don't convert to real-world dates.

## Session logs

Files `Session N.md` each start with a sibling-nav header (`Previous: [[Session N-1]]` /
`Next: [[Session N+1]]`). Two accepted formats coexist: early sessions are continuous present-tense
prose densely wikilinked to every character; later sessions use a `## Saga20 Recap:` summary followed
by a numbered `### Key Events` list with bolded event titles. `Story Leads.md` and `Scratch Notes.md`
are GM planning docs (plot hooks; `- [ ]` worldbuilding TODOs).

- When pulling information from the session logs, double check with the user for information validity whenever
  pulling from notes under the header of `## Saga20 Recap:`. These are notes autogenerated from an AI, and
  when information in these notes conflict with other sources, take the other source as truth and correct
  the Saga20 note.

## Plugin-dependent notes — edit the source syntax carefully

Some notes render via Obsidian community plugins; preserve their raw syntax:

- `Tools/Planner.md` — Kanban board (`kanban-plugin: board`), the GM's session-prep board.
- `Lore/History/Broad History.md` — a fenced ` ```timeline-labeled ` block with `date:`/`title:`/
  `content:` entries (Timeline plugin).
- `People/Relationships.canvas` — an Obsidian Canvas (JSON), not Markdown.

## Setting primer (so edits stay in-world)

The world is **Avira**: modern and technological, but magic is real and secret — known to under 1% of
people, mostly the ruling elite; modern tech actually grew out of magic. **Astaria** is the main
nation (stands in for the USA); the campaign follows teenagers at **West Paradise High School** in
**Lake Prospect** who are each secretly magical. All magic originates from **The Kamihara**; casters
are Sorcerers/Witches/Warlocks/Wizards. A hidden wizard cabal, the **Scholars of Avira**, covertly
controls world governments (Astaria's secret magical arms: the **HUMI** and **HCI**). Deepest lore
lives in `Countries/First World Nations/Astaria.md` and `Lore/History/Broad History.md`.
