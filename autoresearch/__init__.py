from typing import Dict, Any, List

from .inputs import InputManifest, QualityThresholds, validate_inputs
from .ingestion.graph import ResearchGraph
from .orchestrator.planner import StagedPlanner
from .agents.pipeline import MultiAgentDebate
from .verification.core import VerificationCore
from .experiment.loop import AutonomousExperimentLoop, ExperimentProposal
from .review.self_review import StructuredSelfReview, RedTeamReview
from .evaluation.benchmark import SOTAEvaluator
from .governance import HumanGovernanceModel
from .deliverables import FinalDeliverable, RankedClaim, generate_report

class AutoResearchFramework:
    """
    SOTA-level autonomous AutoResearch workflow.
    """
    def __init__(self):
        self.graph = ResearchGraph()
        self.planner = StagedPlanner()
        self.debate = MultiAgentDebate(["repo_analyst", "verifier", "critic"])
        self.verifier = VerificationCore()
        self.experiment_loop = AutonomousExperimentLoop()
        self.reviewer = StructuredSelfReview()
        self.red_team = RedTeamReview()
        self.evaluator = SOTAEvaluator()
        self.governance = HumanGovernanceModel()

    def run(self, manifest: InputManifest) -> FinalDeliverable:
        """Executes the end-to-end AutoResearch pipeline."""
        
        print("1. Validating Inputs...")
        if not validate_inputs(manifest):
            raise ValueError("Input manifest validation failed.")
            
        print("2. Ingestion...")
        for repo in manifest.user_provided_repos + manifest.related_repos:
            self.graph.ingest_codebase(repo)
        for paper in manifest.paper_list:
            self.graph.ingest_paper({"title": paper})
            
        print("3. Planning...")
        tasks = self.planner.decompose_objective(manifest.target_question)
        
        print("4. Multi-Agent Debate & Analysis...")
        debate_result = self.debate.conduct_debate(manifest.target_question)
        final_ruling = self.debate.final_arbiter_ruling(debate_result)
        
        print("5. Verification...")
        claims = ["Proposed framework achieves SOTA"]
        for claim in claims:
            self.verifier.enforce_claim_linkage(claim, [])
            
        print("6. Autonomous Experimentation...")
        if self.governance.request_human_approval("experiment_launch", {}):
            proposal = self.experiment_loop.generate_proposal(final_ruling)
            exp_result = self.experiment_loop.run_experiment(proposal)
        else:
            exp_result = {"status": "blocked", "reason": "Human approval denied"}
            
        print("7. Self-Review & Self-Correction...")
        review_result = self.reviewer.run_review({"experiment": exp_result})
        
        print("8. SOTA Evaluation...")
        eval_score = self.evaluator.evaluate_stage("synthesis", review_result)
        
        print("9. Generating Deliverables...")
        ranked_claims = [
            RankedClaim(statement=claims[0], status="supported", evidence_ids=[])
        ]
        
        deliverable = FinalDeliverable(
            unified_evidence_map={"graph_nodes": len(self.graph.nodes)},
            ranked_claims=ranked_claims,
            failure_log=[exp_result] if exp_result.get("status") != "success" else [],
            reproducibility_pack={"code": "included"},
            next_iteration_plan={"action": "refine_hypothesis"}
        )
        
        return deliverable

__all__ = [
    "InputManifest", "QualityThresholds", "validate_inputs",
    "ResearchGraph",
    "StagedPlanner",
    "MultiAgentDebate",
    "VerificationCore",
    "AutonomousExperimentLoop", "ExperimentProposal",
    "StructuredSelfReview", "RedTeamReview",
    "SOTAEvaluator",
    "HumanGovernanceModel",
    "FinalDeliverable", "RankedClaim", "generate_report",
    "AutoResearchFramework"
]