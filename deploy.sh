#!/bin/bash
set -e # Stop the script immediately if any command fails.

OUTPUT_TEMP="output/"                       # Temporary folder for Pelican build output
OUTPUT_REPO="../modago.github.io"          # Path to your GitHub Pages repo (relative to source)
OUTPUT_REPO_URL="git@github.com:Modago/modago.github.io.git"
BRANCH="master"                           # branch for the live site

# --- STEP 1: Build Pelican site ---
echo "🏗️  Building Pelican site into temporary folder..."
# -s specifies which config file to use (publishconf.py for production)
# -o specifies the output directory for generated files
pelican content -s publishconf.py -o "$OUTPUT_TEMP"

# --- STEP 2: Ensure output repo exists and is valid ---
if [ ! -d "$OUTPUT_REPO" ]; then
    echo "⚠️  Output repo not found. Cloning fresh copy from remote..."
    git clone "$OUTPUT_REPO_URL" "$OUTPUT_REPO"
fi

if [ ! -d "$OUTPUT_REPO/.git" ]; then
    echo "❌ ERROR: No .git directory found in $OUTPUT_REPO."
    echo "Please ensure this folder is a valid Git repo for your GitHub Pages site."
    exit 1
fi

# --- STEP 3: Display summary and confirm before syncing ---
echo "✅ Build complete."
echo "Ready to sync new site files into:"
echo "   $OUTPUT_REPO"
echo
read -p "Do you want to continue and preview changes before committing? (y/N): " confirm
if [[ ! $confirm =~ ^[Yy]$ ]]; then
    echo "🛑 Deployment aborted by user."
    exit 0
fi

# --- STEP 4: Sync files safely ---
echo "🔄 Syncing new site files into output repo (excluding .git to protect history)..."
# rsync copies all files from OUTPUT_TEMP into OUTPUT_REPO
# --delete removes files in the repo that no longer exist in the new build
# --exclude '.git' keeps your Git repo metadata safe
rsync -av --delete --exclude '.git' "$OUTPUT_TEMP/" "$OUTPUT_REPO/"

# Move into the output repo directory so we can check its Git status
cd "$OUTPUT_REPO"

# --- STEP 5: Show changes before staging ---
echo
echo "📋 These are the changes detected in your output repo:"
echo "------------------------------------------------------"
git status
echo "------------------------------------------------------"
echo

read -p "Do you want to stage and commit these changes? (y/N): " stage_confirm
if [[ ! $stage_confirm =~ ^[Yy]$ ]]; then
    echo "🛑 Stopped before staging or committing."
    # Return to previous directory (source repo)
    cd - >/dev/null
    exit 0
fi

# --- STEP 6: Stage, commit, and push changes ---
# Adds all modified/new/deleted files to staging
git add --all

# Check if there are actual differences before committing
if git diff-index --quiet HEAD --; then
    echo "✅ No new changes to commit. Everything is up to date."
else
    # Create a commit with a timestamp message
    git commit -m "Update site $(date +'%Y-%m-%d %H:%M:%S')"
    echo
    read -p "Do you want to push these changes to remote ($BRANCH)? (y/N): " push_confirm
    if [[ $push_confirm =~ ^[Yy]$ ]]; then
        git push origin "$BRANCH"
        echo "🚀 Deployment complete! Your site is live."
    else
        echo "💾 Changes committed locally but not pushed."
    fi
fi

# --- STEP 7: Return to source repo directory ---
# cd - returns to your previous directory (the source repo)
# >/dev/null hides the printed path to keep output clean
cd - >/dev/null

echo "✅ Done. You are now back in your source repo."