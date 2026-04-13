@echo off
cd /d C:\Users\Axelf\OneDrive\GRANITE-FINAL\deployed-store
git add -A
git commit -m "Fix card sizing and section spacing - compact layouts across all pages"
git push origin main
del "%~f0"
