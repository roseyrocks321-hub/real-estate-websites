#!/bin/bash
# One-command deploy: Git push + FTP upload via curl
# Usage: ./deploy.sh brevardfl   or   ./deploy.sh cocoa

SITE=$1

if [ "$SITE" != "brevardfl" ] && [ "$SITE" != "cocoa" ]; then
    echo "Usage: ./deploy.sh brevardfl  or  ./deploy.sh cocoa"
    exit 1
fi

echo "=== Git: committing all changes ==="
cd "$(dirname "$0")"
git add .
git commit -m "Deploy $SITE - $(date '+%Y-%m-%d %H:%M')" || echo "No changes to commit"
git push origin main
echo "✅ GitHub updated"

echo "=== FTP: uploading $SITE ==="
if [ "$SITE" == "brevardfl" ]; then
    FTP_USER="mb-editor@goldenticketrealty.com"
    FTP_PASS='-Rcdl86NPj_gH(m6'
    LOCAL_DIR="./brevardfl"
else
    FTP_USER="cocoafast@sellmyhousefastcocoa.com"
    FTP_PASS='FbnyZ%9t+AG7L}SX'
    LOCAL_DIR="./cocoa"
fi

FTP_HOST="ftp://162.0.232.161"

# Upload all files in the site folder
for f in "$LOCAL_DIR"/*; do
    [ -f "$f" ] || continue
    fname=$(basename "$f")
    curl -k --ftp-ssl-control -T "$f" "$FTP_HOST/$fname" --user "$FTP_USER:$FTP_PASS" 2>/dev/null && echo "  ✅ $fname" || echo "  ❌ $fname"
done

echo "✅ $SITE deployed live"
