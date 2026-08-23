#!/usr/bin/env bash
set -euo pipefail

DASHBOARD_PATH="${DASHBOARD_PATH:-/var/www/html/pcb-dashboard}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$SCRIPT_DIR/index.html"
DST="$DASHBOARD_PATH/index.html"
EXPECTED_SHA="6bed070b47386997bb6c67c3eb7f1f3252beb39206905c87d16382f26a06c013"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"

[ -f "$SRC" ] || { echo "ERROR: missing source file: $SRC" >&2; exit 1; }
[ -d "$DASHBOARD_PATH" ] || { echo "ERROR: dashboard path does not exist: $DASHBOARD_PATH" >&2; exit 1; }

SRC_SHA="$(sha256sum "$SRC" | awk '{print $1}')"
[ "$SRC_SHA" = "$EXPECTED_SHA" ] || { echo "ERROR: unexpected source SHA-256" >&2; exit 1; }

if [ -f "$DST" ]; then
  cp -a "$DST" "$DST.bak.$STAMP"
  echo "backup=$DST.bak.$STAMP"
fi

TMP="$DASHBOARD_PATH/.index.html.tmp.$$"
trap 'rm -f "$TMP"' EXIT
install -m 0644 "$SRC" "$TMP"
mv -f "$TMP" "$DST"
trap - EXIT

DST_SHA="$(sha256sum "$DST" | awk '{print $1}')"
[ "$DST_SHA" = "$EXPECTED_SHA" ] || { echo "ERROR: deployed SHA-256 mismatch" >&2; exit 1; }

grep -q 'delta-symbol accepted' "$DST"
grep -q 'delta-symbol rejected' "$DST"
grep -q 'audited nodes accepted' "$DST"
! grep -q '>audited PCB accepted<' "$DST"

echo "phase=ui_only"
echo "version=3.2.5"
echo "sha256=$DST_SHA"
echo "dashboard=$DST"
echo "services_restarted=none"
