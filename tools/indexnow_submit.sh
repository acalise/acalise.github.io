#!/usr/bin/env bash
# Submit every URL in sitemap.xml to IndexNow (Bing, Yandex, Naver, Seznam, Yep share the index).
# Key file lives at https://acalise.com/<KEY>.txt. Run after any content deploy.
set -euo pipefail
KEY="12f4b7a7ce2bf5cda07a5b0c23243c23"
HOST="acalise.com"
SITEMAP="$(dirname "$0")/../sitemap.xml"

URLS=$(grep -o '<loc>[^<]*</loc>' "$SITEMAP" | sed -e 's#<loc>##' -e 's#</loc>##' | sed 's/.*/"&"/' | paste -sd, -)

curl -sS -o /dev/null -w "IndexNow HTTP %{http_code}\n" \
  -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d "{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"https://$HOST/$KEY.txt\",\"urlList\":[$URLS]}"
