# Hellspire - D&D Campaign Wiki

This is an Obsidian vault serving as a wiki and planning tool for the **Hellspire** D&D campaign. It contains world lore, character profiles, session logs, and DM tools.

## Project Structure

```
Characters/
  Player Characters/
    The Hellbringers/           # Season 1 party (Malm, Deyrale, Gabble, Almint)
    The Fellowship of the Gate/  # Season 2 party (Fel, Zilton, Na'Hal)
  NPCs/
    Origin in Season 1/
    Origin in Season 2/          # NPCs introduced in Season 2
    Other/
Images/                          # Obsidian image attachments
Lore/
  Specific Notes/                # Deep lore articles (souls, magic systems, etc.)
Session Logs/
  Season 1 (The Hellbringers)/
  Season 2 (The Fellowship of the Gate)/
Side Stories/                    # Narrative pieces outside main sessions
Tools/
  Homebrew Rulesets/             # Custom spells, time travel rules, etc.
```

## Conventions

### Obsidian Linking
- All character names in session logs and articles should use `[[Character Name]]` links.
- When a character is referred to by a short name or alias, use piped links: `[[Full Name|Alias]]`.
  - Examples: `[[Fel Sinderheim|Fel]]`, `[[Na' Hal|Na'Hal]]`, `[[Leolar Spirit|the blind man]]`, `[[Almint Friea|Almond]]`, `[[Deyrale Dinglebottom|Daryl]]`
- Titles (Queen, Captain, etc.) stay outside the link: `**Queen** [[Layla Tenama]]`

### Characters
- **Player Characters** get their own file named after the character, placed under their party's folder.
- **NPCs** go under `Characters/NPCs/` in the subfolder matching the season they first appeared in.
- Na'Hal is actually two imps ([[Nampha]] and [[Andhal]]) who combine into a tiefling form. Each imp has its own file under the Na'Hal subfolder.
- Fel Sinderheim's soul inhabits the body of [[Aji Skipplestump]]. Both have separate articles.

### Character Article Format
All character articles (PCs and NPCs) use a consistent info table at the top. Include only categories you are certain about, in this order of priority:

1. **Player** (PCs only)
2. **Species**
3. **Class** & **Level** (if applicable)
4. **Age**
5. **Status** (Alive, Dead, Missing, Trapped, etc.)
6. **Current Location**
7. **Affiliation(s)**

Article body sections (include as applicable):
- **Backstory** - Origin and history before current events
- **Season N Events** - What the character did during sessions, organized by session with a brief title
- **Relationships** - Notable connections to other characters, using `[[links]]`
- **Original Notes** - Raw player notes from character creation (PCs only, preserved at bottom after a `---` divider)

### Session Logs
- Each session is a separate file named `Session N.md`.
- Session numbering is continuous across seasons (Season 1 has Sessions 1-3, Season 2 starts at Session 4).
- Logs begin with a `## Saga20:` header followed by a narrative summary paragraph. This is for summaries that are imported from the Saga20 webapp, and are only for including if they are being imported by the user.
- The body uses a numbered `### Key Events` structure with bold event titles.
- Session logs are written in past-tense narrative prose, not bullet points.

### Lore
- Lore articles go under `Lore/Specific Notes/` for focused topics about world mechanics and metaphysics.

### Tools
- Homebrew rules, custom spells, and DM utilities go under `Tools/`.

## Important Context about the sessions:
- We have already completed up to session 18. I have not finished summarizing the sessions and importing them into the obsidian project.
## Important World Context
- The campaign is set in a world where a Gate to Hell has been opened, unleashing an infernal invasion.
- **Season 1 (The Hellbringers):** Gabble Skipplestump opened the gate using a goblet of fire and a wand. Malm is now trapped in the gate's roots. Deyrale fell into the Nine Hells.
- **Season 2 (The Fellowship of the Gate):** Fel, Zilton, and Na'Hal are on a mission to close the Gate to Hell. They operate as a royal garrison under Queen Layla Tenama of New Friea.
- The Engine of Nessus is a colossal infernal war machine threatening the world.
- Leolar Spirit (the blind man) is an omniscient NPC guiding events from the shadows, invisible even to gods.
