#!/bin/sh

tmux new-session -d 'emacs -nw game.py'
tmux split-window -v 
tmux -2 attach-session -d
