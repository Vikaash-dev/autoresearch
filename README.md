# Evidence-Based Verification of "Awesome Auto Research Tools" Claims

This repository documents a literature-grounded verification of the implicit claims in the **Awesome Auto Research Tools** directory (97 open-source tools, 13 categories).

## Architecture: Unified AutoResearch Framework

We are building a **self-reviewing, self-planning, SOTA-level autonomous AutoResearch workflow**.

### Key Components:
1. **Scope and Inputs** (`autoresearch/inputs.py`): Mandatory input manifests with inclusion/exclusion criteria and quality thresholds.
2. **Multi-source Ingestion** (`autoresearch/ingestion/graph.py`): Ingests codebases and papers into a normalized research graph with provenance tracking.
3. **Self-planning Orchestrator** (`autoresearch/orchestrator/planner.py`): Staged planning and dependency-aware execution.
4. **Specialist Agent Pipeline** (`autoresearch/agents/pipeline.py`): Multi-agent debate with arbiter rules to prevent optimistic bias.
5. **Verification-first Core** (`autoresearch/verification/core.py`): Enforces claim-evidence linkage, reverse analysis, and cross-analysis.
6. **Autonomous Experiment Loop** (`autoresearch/experiment/loop.py`): Guarded execution with feasibility checks and explicit failure reporting.
7. **Self-review & Self-correction** (`autoresearch/review/self_review.py`): Structured reviews (factuality, novelty) and red-team challenges.
8. **Benchmarking & SOTA Evaluation** (`autoresearch/evaluation/benchmark.py`): Measures transfer gaps between benchmarks and real-world tasks.
9. **Human Governance** (`autoresearch/governance.py`): Hard-stop gates for high-risk actions (experiment launch, publication claims).
10. **Deliverables Format** (`autoresearch/deliverables.py`): Final outputs including evidence maps, ranked claims, and failure logs.
