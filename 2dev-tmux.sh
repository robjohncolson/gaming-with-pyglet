#!/bin/sh

tmux split-window -v -c './replscript.sh'
tmux new-session -d 'emacs -nw game.py'
tmux -2 attach-session -d
