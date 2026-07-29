#!/usr/bin/env bash
# hooks/session-start.sh
# Fires on SessionStart (startup, clear, compact) events.
# Injects a short routing reminder. Detailed policy stays in the workflow files.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
WORKFLOW_FILE="$PROJECT_ROOT/WORKFLOW.md"
REFACTOR_WORKFLOW_FILE="$PROJECT_ROOT/REFACTOR_WORKFLOW.md"

echo "<IMPORTANT>"
echo "Read $WORKFLOW_FILE and $REFACTOR_WORKFLOW_FILE."
echo "Orchestration must be Fable 5 or GPT-5.6 Sol."
echo "Sonnet and Haiku are workers only. Run the deterministic gate before delivery."
echo "</IMPORTANT>"
