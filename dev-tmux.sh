#!/bin/sh

tmux new-session -d 'emacs -nw game.py'
tmux split-window -v -c './replscript.sh'
tmux -2 attach-session -d
