---
name: architecture-docs
description: Use when explicitly asked to document an existing system's architecture, produce a component or data-flow diagram, or explain its design decisions.
---

# Document Existing Architecture

Accept a repository path, a focus such as data flow or decisions, and
`--quick`/`quick` from the invocation. Otherwise use the current conversation's
focused repository or current project; ask if multiple targets are ambiguous.
Resolve an absolute project path before reading or writing. The directory
containing this skill and the shell's working directory may be different from
the project being documented.

Read project instructions, README, existing architecture docs, entry points,
configuration, and relevant modules. Trace representative input-to-output
paths and external dependencies using actual code. Explore sequentially;
parallel agents are optional when available and appropriate, not a prerequisite.

## Quick mode

Produce a concise Mermaid component or data-flow diagram and a brief explanation
of its edges. Use only the components the system actually has; a two-component
system does not need extra nodes to meet a quota. Label arrows with data,
events, or control flow and mark external boundaries. Stop after the diagram
and its explanation. Show Mermaid inline by default. If an export was requested,
save it at the supplied path or a clearly reported path inside the target repo;
no workspace-specific helper, CDN, or HTML renderer is required.

## Full mode

Document system purpose, components and their responsibilities, data/control
flow, external integrations, storage/models when relevant, configuration,
and credential-handling boundaries. Use Mermaid where it clarifies the system.
Scale detail to project complexity and link important source paths as evidence.

Distinguish observed implementation choices from historical rationale. Cite
existing ADRs or other evidence for motivations and alternatives. If those
are undocumented, say so; label deductions as inferences rather than inventing
decisions, stakeholders, or design history. Describe the current system, not
proposed architecture. Never copy credential values into the document.

Update the existing architecture document when one exists, preserving unrelated
content and user edits. Otherwise write `docs/architecture.md` within the target
project, unless the user requested a different destination or chat-only output.
Check that diagram labels/edges agree with the code, links resolve, and the
output is at the intended path. Report unverified areas. Do not change product
code, create decision records for imaginary history, or commit automatically.
