#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${REPO_URL:-https://github.com/hashburst/mining_segmentation.git}"
BRANCH="${BRANCH:-main}"
PUBLISH_BRANCH="${PUBLISH_BRANCH:-pcb-dashboard-v3.2.5}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

cd "$ROOT"
mkdir -p "$STAGE/tree"
tar --exclude=.git -cf - . | tar -xf - -C "$STAGE/tree"

git remote get-url origin >/dev/null 2>&1 || git remote add origin "$REPO_URL"
git remote set-url origin "$REPO_URL"
git fetch origin "$BRANCH"
git checkout -B "$PUBLISH_BRANCH" "origin/$BRANCH"

cp "$STAGE/tree/README.md" README.md
cp "$STAGE/tree/LICENSE" LICENSE
cp "$STAGE/tree/.gitignore" .gitignore
rm -rf block_segmentation pcb-dashboard
cp -a "$STAGE/tree/block_segmentation" block_segmentation
cp -a "$STAGE/tree/pcb-dashboard" pcb-dashboard
cp "$STAGE/tree/publish-pcb-dashboard.sh" publish-pcb-dashboard.sh
chmod 755 publish-pcb-dashboard.sh pcb-dashboard/server-b/install-v3.2.5-ui-only.sh

git add .gitignore README.md LICENSE block_segmentation pcb-dashboard publish-pcb-dashboard.sh

if git diff --cached --quiet; then
  echo "No changes to publish"
  exit 0
fi

git commit -m "Add PCB dashboard v3.2.5 and update project documentation"
git push origin HEAD:"$BRANCH"

echo "repository=$REPO_URL"
echo "branch=$BRANCH"
