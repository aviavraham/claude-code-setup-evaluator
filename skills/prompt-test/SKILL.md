---
name: prompt-test
description: Use when explicitly asked to evaluate a prompt, compare prompt versions, or check prompt regressions against fixtures or saved baselines.
---

# Evaluate Prompts

Accept a prompt path/function, `--compare` (working tree versus HEAD), or
`--baseline <file>` from the invocation. Resolve the supplied repository or
current focus to an absolute path. If the target is ambiguous, identify
candidate prompt entry points and ask which one to evaluate.

## Prepare

Inspect prompt code and dependencies statically before executing or importing
them. Watch for import-time API calls, writes, and production integrations.
Render only through an existing safe renderer or isolated pure prompt logic;
if safe rendering is unavailable, report that limitation instead of importing
the application. Leave the prompt source unchanged.

Use existing approved fixtures or synthetic inputs, including ordinary,
sparse, malformed, and boundary cases relevant to the prompt. Replace secrets
and personal/confidential data before display or external use. Show a redacted
rendered example and disclose substitutions; keep unredacted inputs and
responses out of logs and reports.

Define expected fields, format/schema, grounding requirements, acceptable
length, parser behavior, and case-specific success criteria before scoring.
Reuse the project's evaluation harness when available.

## Run and compare

Default to local rendering and validation. A live model call requires user
authorization covering the provider/endpoint, model, fixture scope, and call
budget. The presence of credentials alone is not permission. Identify a
production endpoint before asking for authorization. Report missing
credentials without displaying them; do not install SDKs automatically.

For `--compare`, read HEAD files through Git without checking out, resetting,
or overwriting working files. Compare both versions on identical sanitized
fixtures and matched model/settings, using an isolated harness if execution
is needed. Do not import a historical module with uncontrolled side effects.

Record prompt version/hash, fixture identity, model/provider, generation
settings, seed when supported, parser/evaluator version, run count, errors,
and scores. Do not assume a seed makes model output deterministic. For noisy
results, use repeated trials within the authorized budget or report uncertainty.
Missing baseline provenance/settings means **inconclusive/not comparable**,
not a claimed improvement or regression.

## Report

Separate rendering/schema/parser checks from semantic quality and live-model
results. Report PASS, FAIL, or INCONCLUSIVE per criterion with redacted evidence,
what was actually executed, and limitations. Label token counts as estimates
unless measured with the model's tokenizer. Save a sanitized baseline with
its provenance only if requested; do not persist raw sensitive fixtures.
