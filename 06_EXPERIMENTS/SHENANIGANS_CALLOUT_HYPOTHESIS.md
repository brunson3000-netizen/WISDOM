# Experiment — "Shenanigans" Recurring Callout

**Status:** WORKING THEORY / NONCANONICAL PEDAGOGICAL EXPERIMENT  
**Date opened:** 2026-09-06  
**Curriculum authority:** none

## Working hypothesis

Occasional, deliberately spaced **SHENANIGANS** callouts may make failure modes more memorable and train learners to notice when an AI, tool, workflow, governance rule, or operator assumption is behaving in a superficially plausible but operationally ridiculous way.

The proposed recurring idea is roughly:

> Every so often the learner turns the page and encounters **SHENANIGANS** — a real incident where something looked reasonable, went sideways, and exposed a reusable lesson about how to watch the system rather than merely trust the plan.

This is a presentation hypothesis, not an adopted course device.

## What "shenanigans" would mean

"Shenanigans" is not a technical failure class.

It is a memorable wrapper around a real underlying issue such as:

- hidden state;
- authority confusion;
- evidence overclaim;
- tool/interface mismatch;
- incomplete handoff;
- brittle automation;
- governance recursion;
- silent synchronization failure;
- context loss;
- a human assumption that was reasonable but wrong.

Every callout should still name the actual technical lesson.

## Why it may work

The hypothesis is that a recurring anomaly frame could:

- create anticipation without turning instruction into a lecture;
- make abstract failure modes concrete;
- normalize checking what actually happened;
- teach healthy skepticism toward both AI output and one's own assumptions;
- preserve humor around frustrating mistakes without mocking the learner;
- improve recall by attaching a distinctive label to a failure/recovery pattern.

## Important boundary

Shenanigans must be **two-sided**.

The joke cannot always be "the AI did something stupid." Useful examples may originate from:

- the model;
- the tool;
- the interface;
- the project architecture;
- the instructions;
- the operator;
- interactions between otherwise reasonable components.

That keeps the lesson grounded in systems thinking rather than AI-bashing.

## Candidate callout anatomy

A future callout might contain only five parts:

### SHENANIGANS

**What looked reasonable?**  
The assumption, command, response, or workflow that passed an initial smell test.

**What actually happened?**  
The observed mismatch.

**What kind of shenanigans was it?**  
The real technical failure class.

**How was it caught?**  
Evidence, test, operator observation, validation, or contradiction.

**What watches for it next time?**  
A habit, boundary, test, deterministic mechanism, or design change.

## Candidate examples already present in the evidence corpus

These are research examples, not selected course material:

- an interactive `set -e` block closing the operator's terminal;
- Nano retaining a correct provenance buffer but failing because the path context was wrong;
- a whitespace checker objecting to immutable, hash-verified imported evidence;
- a supposed command-line invocation unexpectedly opening a GUI;
- a complete-looking handoff missing a parent dependency and promised fixtures;
- governance adding rules until the rule system began recursively branching;
- telemetry supporting a narrower conclusion than the surrounding prose wanted to claim;
- agents rechecking validated state until attention drifted away from the actual unresolved problem.

## Risks / falsification targets

The idea should be rejected or changed if testing shows that it:

- becomes a gimmick;
- distracts from the underlying technical concept;
- makes serious authority, security, privacy, or safety failures feel trivial;
- appears too frequently and loses surprise value;
- encourages learners to treat normal uncertainty as incompetence;
- becomes condescending or performs humor at the learner's expense;
- improves entertainment but not recall, diagnosis, or transfer.

## Research questions

1. Do learners remember the underlying failure pattern better after a Shenanigans callout than after ordinary exposition?
2. Does the device improve transfer — can learners notice the same class of problem in a new context?
3. What frequency keeps it memorable without turning it into branding noise?
4. Should the callout appear only after the learner has enough context to diagnose the incident?
5. Does a mix of AI-, tool-, process-, and operator-originated examples produce better systems thinking?
6. Which failures are too consequential to frame humorously?
7. Does the label still feel respectful and useful to learners with different ages, backgrounds, and goals?

## Current disposition

Keep the idea alive and collect suitable evidence.

Do not design the curriculum around it yet.
