from autoresearch.inputs import InputManifest, QualityThresholds
from autoresearch.ingestion.graph import ResearchGraph
from autoresearch.orchestrator.planner import StagedPlanner
from autoresearch.review.self_review import StructuredSelfReview
import json

def review_all_given_repos():
    # 1. Define the repos given in the problem statement
    given_repos = [
        "SakanaAI/AI-Scientist",
        "assafelovic/gpt-researcher",
        "stanford-oval/storm",
        "FoundationAgents/MetaGPT",
        "HKUDS/AI-Researcher"
    ]
    
    # 2. Setup the manifest
    manifest = InputManifest(
        target_question="Review capabilities and limitations of SOTA autoresearch repos",
        user_provided_repos=given_repos,
        related_repos=[],
        paper_list=[]
    )
    
    # 3. Initialize components
    graph = ResearchGraph()
    reviewer = StructuredSelfReview()
    
    print(f"Starting review of {len(manifest.user_provided_repos)} given repos...")
    
    # 4. Ingest and review
    results = {}
    for repo in manifest.user_provided_repos:
        print(f"Ingesting {repo}...")
        graph.ingest_codebase(repo)
        
        # Simulate extracted claims from repo
        repo_data = {
            "id": repo,
            "claims": ["Autonomous research", "SOTA performance"],
            "evidence": []
        }
        
        print(f"Running structured self-review for {repo}...")
        review_result = reviewer.run_review(repo_data)
        
        results[repo] = {
            "status": "Reviewed",
            "approved": review_result["approved"],
            "feedback": review_result["feedback"]
        }
        
    print("\n--- Review Summary ---")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    review_all_given_repos()
