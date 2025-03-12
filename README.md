admin@DESKTOP-F22EK55 MINGW64 ~ (master)
$ mkdir labo7

admin@DESKTOP-F22EK55 MINGW64 ~ (master)
$ cd labo7

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git init
Initialized empty Git repository in C:/Users/admin/labo7/.git/

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git add labo7.py
fatal: pathspec 'labo7.py' did not match any files

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git add das1.py

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git commit -m "dasgal1"
[master (root-commit) 2fa1d49] dasgal1
 1 file changed, 18 insertions(+)
 create mode 100644 das1.py

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git add das2.py

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git commit -m "dasgal2"
[master 00615dd] dasgal2
 1 file changed, 2 insertions(+)
 create mode 100644 das2.py

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git add das3.py

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git commit -m "dasgal3"
[master 959c270] dasgal3
 1 file changed, 9 insertions(+)
 create mode 100644 das3.py

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git add das4.py

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git commit -m "dasgal4"
[master c90b364] dasgal4
 1 file changed, 18 insertions(+)
 create mode 100644 das4.py

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git add das5.py

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git commit -m "dasgal5"
[master 1989d48] dasgal5
 1 file changed, 9 insertions(+)
 create mode 100644 das5.py

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git status
On branch master
nothing to commit, working tree clean

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (master)
$ git branch -M main

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (main)
$ git remote add originhttps://github.com/byambaa50/lab-7.git
usage: git remote add [<options>] <name> <url>

    -f, --[no-]fetch      fetch the remote branches
    --[no-]tags           import all tags and associated objects when fetching
                          or do not fetch any tag at all (--no-tags)
    -t, --[no-]track <branch>
                          branch(es) to track
    -m, --[no-]master <branch>
                          master branch
    --[no-]mirror[=(push|fetch)]
                          set up remote as a mirror to push to or fetch from


admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (main)
$ git remote add origin https://github.com/byambaa50/lab-7.git

admin@DESKTOP-F22EK55 MINGW64 ~/labo7 (main)
$ git push -u origin main
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 12 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (15/15), 1.62 KiB | 827.00 KiB/s, done.
Total 15 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), done.
To https://github.com/byambaa50/lab-7.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
