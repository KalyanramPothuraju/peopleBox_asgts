# peopleBox_asgts
Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss
$ git init
Initialized empty Git repository in C:/Users/Kalyan Ram/OneDrive/Desktop/asgtss/.git/

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (master)
$ git config --global user.email kalyanram_pothuraju@srmap.edu.in

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (master)
$ git config --global user.name KalyanramPothuraju

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (master)
$ echo "# peopleBox_asgts" >> README.md

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (master)
$ git add README.md
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (master)
$ git commit -m "first commit"
[master (root-commit) 5906ae3] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (master)
$ git branch -M main

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (main)
$ git remote add origin https://github.com/KalyanramPothuraju/peopleBox_asgts.git

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (main)
$ git push -u origin main
info: please complete authentication in your browser...
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 255 bytes | 127.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/KalyanramPothuraju/peopleBox_asgts.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (main)
$ git checkout -b  feature/newfeature
Switched to a new branch 'feature/newfeature'

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (feature/newfeature)
$ echo "Hello,World!" > example.txt

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (feature/newfeature)
$ git add example.txt
warning: in the working copy of 'example.txt', LF will be replaced by CRLF the next time Git touches it

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (feature/newfeature)
$ git commit -m "Add example.txt with hello, world! content"
[feature/newfeature 4920b5b] Add example.txt with hello, world! content
 1 file changed, 1 insertion(+)
 create mode 100644 example.txt

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (feature/newfeature)
$ git push -u origin feature/new-feature
error: src refspec feature/new-feature does not match any
error: failed to push some refs to 'https://github.com/KalyanramPothuraju/peopleBox_asgts.git'

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (feature/newfeature)
$ git push -u origin feauture/newfeature
error: src refspec feauture/newfeature does not match any
error: failed to push some refs to 'https://github.com/KalyanramPothuraju/peopleBox_asgts.git'

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (feature/newfeature)
$ git push -u origin feature/newfeature
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 340 bytes | 340.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'feature/newfeature' on GitHub by visiting:
remote:      https://github.com/KalyanramPothuraju/peopleBox_asgts/pull/new/feature/newfeature
remote:
To https://github.com/KalyanramPothuraju/peopleBox_asgts.git
 * [new branch]      feature/newfeature -> feature/newfeature
branch 'feature/newfeature' set up to track 'origin/feature/newfeature'.

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (feature/newfeature)
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        q2-asgt1.py
        q2-asgt2.py
        q3-asgt1.py
        q3-asgt1.txt
        q4-asgt1.js
        q5-asgt1.py

nothing added to commit but untracked files present (use "git add" to track)

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (main)
$ git push
Everything up-to-date

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (main)
$ git add .

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (main)
$ git commit -m "files added"
[main e268f1c] files added
 6 files changed, 73 insertions(+)
 create mode 100644 q2-asgt1.py
 create mode 100644 q2-asgt2.py
 create mode 100644 q3-asgt1.py
 create mode 100644 q3-asgt1.txt
 create mode 100644 q4-asgt1.js
 create mode 100644 q5-asgt1.py

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (main)
$ git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 16 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.15 KiB | 1.15 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/KalyanramPothuraju/peopleBox_asgts.git
   5906ae3..e268f1c  main -> main

Kalyan Ram@?????? MINGW64 ~/OneDrive/Desktop/asgtss (main)
$
