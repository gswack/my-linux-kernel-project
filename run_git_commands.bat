git init
git add .
git commit -m "Initial commit"
@REM gh auth login
@REM gh repo create my-linux-kernel --public --source=. --remote=origin --push
git remote add origin https://github.com/gswack/my-linux-kernel
git remote -v
git branch -M main
git push -u origin main
pause