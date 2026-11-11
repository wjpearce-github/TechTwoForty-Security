# Security gates

Every check this repo runs, where it runs, and what happens when it finds something.

| Check | Tool | On my machine | In the pipeline | Blocks or reports |
|---|---|---|---|---|
| Benchmark | Lynis, Prowler | By hand | Weekly, benchmark.yml | Reports |
| Secrets | Trivy | Pre-commit hook | First step | Blocks |
| Tests | pytest | By hand | Every push and PR | Blocks |
| Code (SAST) | Semgrep | By hand | Every push and PR | Blocks |
| Dependencies (SCA) | Trivy | By hand | Every push and PR | Blocks on HIGH, CRITICAL |
| SBOM | Trivy | By hand | Every push and PR | Saved as an artifact |
| Infrastructure (IaC) | Trivy, Checkov | By hand | Every push and PR | Blocks on HIGH, CRITICAL, minus the risk register |
| Container image | Trivy, ECR | By hand | Every push and PR | Blocks on fixable CRITICAL |
| Running app (DAST) | ZAP | By hand | Every push and PR | Reports |
| Where findings go | DefectDojo | Imported with tools/dojo_import.py | Reports saved as security-reports | Triaged by a person |
