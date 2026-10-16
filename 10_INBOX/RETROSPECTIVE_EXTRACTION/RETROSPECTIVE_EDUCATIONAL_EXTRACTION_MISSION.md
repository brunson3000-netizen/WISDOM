# W.I.S.D.O.M. Retrospective Educational Extraction — Raw Harvest Mission

**Status:** WORKING HARVEST MISSION — NONCANONICAL
**Project:** W.I.S.D.O.M.
**Repository:** `/home/chromikey/Projects/WISDOM_PROJECT`
**Primary dump location:** `10_INBOX/RETROSPECTIVE_EXTRACTION/`

## Mission

Mine accessible W.I.S.D.O.M. project history, prior conversation/thread history, repository records, project handoffs, educational-evidence records, and relevant S.W.A.R.M./G.A.M.E./S.P.A.R.K. history for anything that may later strengthen W.I.S.D.O.M. as a course, program, instructional system, learner experience, or project methodology.

This is a **harvest mission, not an adjudication mission**.

The goal is to build a large, provenance-preserving pile of potentially useful material for later research, falsification, classification, and curriculum design.

Do not require the Operator to manually summarize old threads before beginning. Exhaust the history and repository material actually available to you first. If some source cannot be accessed, record the gap precisely instead of guessing what it contained.

## Core boundary

**W.I.S.D.O.M. may study a project without becoming that project.**

S.W.A.R.M., G.A.M.E., S.P.A.R.K., and other source projects are evidence corpora. Their governance, terminology, architecture, conclusions, aesthetics, and operating rules do not automatically become W.I.S.D.O.M. doctrine.

Preserve transferable lessons; do not import source-project authority.

## Harvest first

During this mission:

- collect broadly;
- preserve source provenance;
- retain contradictions and failed ideas when they may teach something;
- capture repeated patterns;
- capture one-off events when their consequence or learning value may be high;
- record uncertainties;
- allow overlap between categories;
- prefer inclusion over premature pruning when genuine educational potential exists.

Do **not**:

- write the curriculum;
- decide final lesson sequence;
- create a Constitution;
- promote harvested material into Canon;
- treat repository placement as adoption;
- research every candidate to conclusion during collection;
- discard a candidate merely because it is currently awkward or unresolved;
- turn the source projects into W.I.S.D.O.M. templates;
- ask the Operator to reconstruct accessible material manually.

## Sources to mine

Search as broadly as available across:

1. W.I.S.D.O.M. conversation and project history;
2. W.I.S.D.O.M. repository records;
3. W.I.S.D.O.M. thread closeouts and handoffs;
4. educational-evidence records;
5. accessible S.W.A.R.M. history;
6. accessible G.A.M.E. history;
7. accessible S.P.A.R.K. history;
8. other project history where the learner encountered relevant AI-assisted work;
9. repository commits, artifacts, failures, corrections, experimental records, and operator workflows;
10. prior research already preserved in W.I.S.D.O.M.

Use available conversation-history/personal-context retrieval where supported. Use repository evidence to corroborate remembered or summarized events when possible.

Do not claim exhaustive coverage unless the accessible source set genuinely supports that claim.

## What to harvest

Look for candidate educational value in at least these forms:

### Learner events

- misunderstandings;
- conceptual breakthroughs;
- moments where a prior idea suddenly became applicable;
- changes in mental model;
- skills that stopped requiring assistance;
- skills that still required assistance;
- surprising tool behavior;
- productive confusion;
- unproductive confusion;
- recovery from mistakes;
- confidence that was justified or unjustified;
- cases where AI output hid lack of learner understanding.

### AI-working methods

- prompting patterns;
- delegation;
- agent coordination;
- context management;
- use of primary coordinators and workers;
- independent review;
- claim verification;
- correction loops;
- escalation;
- model/tool selection;
- separating architecture from implementation;
- using lighter/heavier models appropriately;
- evidence gathering;
- avoiding repeated reasoning by creating deterministic mechanisms.

### Engineering procedures

- repository setup;
- durable state;
- Git use;
- handoffs;
- artifact custody;
- provenance;
- source-of-truth problems;
- tests versus actual behavior;
- debugging;
- project isolation;
- dependency or environment issues;
- telemetry;
- experiment design;
- staged complexity;
- failure containment;
- operator workflow.

### Governance and constitutional lessons

- authority before workflow;
- minimum sufficient governance;
- delegated autonomy;
- evidence versus authority;
- explicit adoption;
- policy versus enforcement;
- governance branching;
- two-sided tightening;
- amendment-impact reasoning;
- review independence;
- situations where governance prevented failure;
- situations where governance itself created unnecessary failure or branching.

Harvest the **generalizable lesson or question**, not the source project's governance as a rule for students.

### Pedagogy and course-design lessons

- scaffolding;
- fading;
- active learning;
- guided discovery;
- cognitive apprenticeship;
- retrieval;
- transfer;
- metacognition;
- formative evidence;
- learner autonomy;
- exam pressure;
- callout opportunities;
- prerequisite chains;
- sequencing clues;
- examples that made a concept understandable;
- examples that failed;
- places where explanation arrived too early or too late;
- places where theory and practice naturally connected.

### Learner experience and culture

- respect versus elitism;
- autonomy versus structure;
- community;
- belonging;
- fun;
- play;
- motivation;
- frustration;
- accessibility;
- dignity;
- social learning;
- S.W.A.R.M.-derived cultural ideas that may carry transferable virtues without requiring S.W.A.R.M. theming;
- mascot/P.A.L./gamification ideas, clearly marked as such.

### Product, delivery, and market implications

- different learner goals;
- different course-track needs;
- delivery-format implications;
- digital versus book/classroom constraints;
- features that only make sense online;
- barriers to entry;
- beginner assumptions that proved false;
- reasons a learner may want AI;
- evidence that should inform marketing without dictating curriculum.

### Negative evidence

Deliberately look for:

- approaches that repeatedly failed;
- unnecessary complexity;
- ceremony without value;
- misleading abstractions;
- context loss;
- repeated operator burden;
- status or hierarchy effects;
- artificial difficulty;
- over-scaffolding;
- under-scaffolding;
- AI doing the learner's cognition;
- false confidence from working artifacts;
- practices that looked sophisticated but did not improve outcomes.

Negative findings belong in the harvest.

## Raw classification only

Do not fully adjudicate Theory → Provisional → Probational → Canon during harvest.

Each item may instead receive one or more **harvest tags**. Use these only for retrieval and later routing:

- `LEARNER_EVENT`
- `PEDAGOGY`
- `AI_WORKING_METHOD`
- `ENGINEERING_PROCEDURE`
- `GOVERNANCE`
- `FAILURE_RECOVERY`
- `TOOLS_WORKFLOW`
- `COURSE_DESIGN`
- `CULTURE`
- `DELIVERY`
- `GAMIFICATION`
- `PRODUCT`
- `MARKETING`
- `NEGATIVE_EVIDENCE`
- `RESEARCH_NEEDED`
- `POSSIBLE_EXPERIMENT`
- `POSSIBLE_CALLOUT`
- `POSSIBLE_CONSTITUTIONAL_PRINCIPLE`

Multiple tags are encouraged when the same event matters in several ways.

Existing Canon/Provisional/Probational/Theory status must be preserved when already known. Do not silently reclassify it.

## Harvest item schema

Give every material candidate a durable ID:

`RX-YYYYMMDD-NNNN`

Each item should contain:

- **ID**
- **short title**
- **source project/thread**
- **source date or approximate period**
- **provenance pointer** — file, commit, thread description, artifact, or other identifiable origin when available
- **observation** — what happened or what was stated
- **possible educational value** — why it may matter
- **tags**
- **known status** — only if already established
- **contradiction/counterevidence** — if already visible
- **later research question**
- **confidence in reconstruction** — high / medium / low
- **duplicate/related IDs** — when known

Keep observation separate from interpretation.

## Repository dump structure

Write harvested material directly into:

`10_INBOX/RETROSPECTIVE_EXTRACTION/`

Use append-friendly bounded files rather than one endlessly growing document.

Recommended form:

- `HARVEST_YYYY-MM-DD_WISDOM.md`
- `HARVEST_YYYY-MM-DD_SWARM.md`
- `HARVEST_YYYY-MM-DD_GAME.md`
- `HARVEST_YYYY-MM-DD_SPARK.md`
- `HARVEST_YYYY-MM-DD_CROSS_PROJECT.md`
- additional bounded files when a source or period is large.

Also maintain:

`10_INBOX/RETROSPECTIVE_EXTRACTION/SOURCE_COVERAGE.md`

That file should record:

- sources searched;
- date ranges covered;
- sources partially covered;
- inaccessible or missing sources;
- whether repository corroboration exists;
- follow-up sources worth checking later.

Do not interpret a missing source as negative evidence.

## Deduplication rule

Do not aggressively collapse repeated events.

Recurrence may itself be educational evidence.

When two items appear to describe the same underlying event:

- link them;
- mark the likely duplicate;
- preserve separate provenance until later adjudication.

When a pattern recurs across distinct events, create a separate `CROSS_PROJECT` candidate describing the pattern and link the underlying item IDs.

## Research boundary

This pass is allowed to perform **minimal verification needed to avoid obvious misrepresentation**, but it should not turn into deep literature research.

When a harvested idea clearly requires outside evidence, tag it `RESEARCH_NEEDED` and state the question that later research must answer.

## Falsification posture

Do not harvest only attractive ideas.

For every repeated or apparently strong practice, actively notice:

- counterexamples;
- situations where the opposite worked;
- hidden costs;
- learner-specific explanations;
- source-project-specific explanations;
- cases where the practice solved one problem but created another.

Preserve these beside the candidate.

## Respect over elitism

Treat learner difficulty as evidence about the system, task, prerequisite chain, explanation, environment, or learner state—not as evidence of lesser worth.

Do not use sophistication, speed, tool fluency, agent count, technical jargon, or willingness to tolerate pain as proxies for learner value.

## Completion standard for one mining pass

A pass is complete when:

1. the accessible source scope for that pass has been searched;
2. candidate items have been written to the repository dump;
3. source coverage and gaps are recorded;
4. no harvested candidate has been silently promoted;
5. contradictions and negative evidence are retained;
6. repository files pass basic formatting/integrity checks;
7. only the harvest files for this mission are staged;
8. a local Git commit makes the harvest durable.

Do not push, merge, deploy, publish, or remotely promote anything unless the Operator separately authorizes it.

## Commit behavior

After each bounded harvesting pass:

1. inspect the live repository state;
2. do not overwrite unrelated work;
3. write/update only the retrospective extraction files needed for that pass;
4. run `git diff --check`;
5. stage only those files;
6. inspect the staged diff;
7. create one descriptive **local** commit;
8. report the commit SHA, files changed, source coverage, major gaps, and item count.

Suggested commit message:

`research: harvest retrospective educational candidates`

## Final return

Return a compact completion report, not a curriculum synthesis.

Report:

- number of candidates harvested;
- broad source coverage;
- major inaccessible/gap areas;
- files written;
- local commit SHA;
- any integrity problem that prevented completion.

Do not promote, rank, or resolve the pile unless the Operator separately starts the later research/adjudication mission.
