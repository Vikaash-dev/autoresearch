from autoresearch import AutoResearchFramework, InputManifest

manifest = InputManifest(
    target_question="Build a SOTA autoresearch framework",
    user_provided_repos=["SakanaAI/AI-Scientist"],
    related_repos=[],
    paper_list=[]
)

framework = AutoResearchFramework()
deliverable = framework.run(manifest)
print(deliverable)
