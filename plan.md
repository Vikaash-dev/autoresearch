1. We need to implement the core pipeline of the AutoResearch framework.
2. We'll create `autoresearch/framework.py` or edit `autoresearch/__init__.py` to expose a `SOTAAutoResearchFramework` class that orchestrates all 10 components mentioned in the README.
3. It will take an `InputManifest`, process it through `ResearchGraph`, `StagedPlanner`, `MultiAgentDebate`, `VerificationCore`, `AutonomousExperimentLoop`, `StructuredSelfReview`, `SOTAEvaluator`, `HumanGovernanceModel`, and output a `FinalDeliverable`.
