#!/bin/bash
# One-command deploy: Git push + FTP upload
# Usage: ./deploy.sh brevardfl   or   ./deploy.sh cocoa

SITE=$1

if [ "$SITE" != "brevardfl" ] && [ "$SITE" != "cocoa" ]; then
    echo "Usage: ./deploy.sh brevardfl  or  ./deploy.sh cocoa"
    exit 1
fi

echo "=== Git: committing all changes ==="
cd "$(dirname "$0")"
git add .
git commit -m "Deploy $SITE - $(date '+%Y-%m-%d %H:%M')"
git push origin main
echo "✅ GitHub updated"

echo "=== FTP: uploading $SITE ==="
# Credentials filled in below
if [ "$SITE" == "brevardfl" ]; then
    FTP_HOST="YOUR_BREVARDFL_HOST"
    FTP_USER="YOUR_BREVARDFL_USER"
    FTP_PASS="YOUR_BREVARDFL_PASS"
    FTP_REMOTE_DIR="/"
    LOCAL_DIR="./brevardfl"
else
    FTP_HOST="YOUR_COCOA_HOST"
    FTP_USER="YOUR_COCOA_USER"
    FTP_PASS="YOUR_COCOA_PASS"
    FTP_REMOTE_DIR="/"
    LOCAL_DIR="./cocoa"
fi

# Upload via lftp (mirrors local folder to remote)
lftp -u "$FTP_USER","$FTP_PASS" "$FTP_HOST" <<EOF
set ssl:verify-certificate no
set ftp:ssl-allow no
mirror -R --delete --verbose "$LOCAL_DIR" "$FTP_REMOTE_DIR"
bye
EOF

echo "✅ $SITE deployed live"
