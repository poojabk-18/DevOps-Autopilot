# AI Log Analyzer – Real CI/CD Failure Demo

This is a **separate demo repository** for generating real GitHub Actions failure logs.

## What it demonstrates
Run the `Demo failure scenarios` workflow manually and choose one scenario:
1. `docker-build` – Docker fails because the Dockerfile copies a missing file.
2. `dependency-conflict` – pip cannot resolve incompatible pinned dependencies.
3. `test-failure` – a real pytest assertion fails.
4. `deployment-config` – deployment validation fails because a required environment variable is missing.

These are intentionally failing scenarios for demonstration. They do not deploy anything or access cloud resources.

## Setup
1. Create a new repository on GitHub (or use a teammate's repository where you have permission).
2. Upload **the contents of this folder** to the repository root, including the `.github` folder.
3. Open the repository's **Actions** tab.
4. Select **Demo failure scenarios**.
5. Click **Run workflow**, choose a scenario, and run it.
6. Repeat for each scenario. Each run produces actual GitHub Actions logs.

## Connect it to AI Log Analyzer
In the AI Log Analyzer Repositories page:
- Owner: the GitHub account or organization that owns this repository
- Repository: the repository name (not its URL)

The AI Log Analyzer backend must have permission to read Actions workflow runs and logs for this repository.

## Important
- This workflow is intentionally designed to fail.
- No GitHub secrets are required for these four demo scenarios.
- Do not upload API keys, personal access tokens, `.env` files, or other credentials.
