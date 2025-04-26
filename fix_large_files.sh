#!/bin/bash

# Step 1: Remove the large files from git history
git rm --cached llama7b-agri-qlora/checkpoint-1000/adapter_model.safetensors
git rm --cached llama7b-agri-qlora/checkpoint-1000/optimizer.pt

# Step 2: Tell git-lfs to track large files
git lfs track "*.safetensors"
git lfs track "*.pt"

# Step 3: Add updated .gitattributes and all other changes
git add .gitattributes
git add .

# Step 4: Commit the changes
git commit -m "Fix: Track large model files with LFS properly"

# Step 5: Push forcefully to remote
git push -u origin master --force

echo "✅ Done! Your large files are now correctly tracked with Git LFS and pushed!"

