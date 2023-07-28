#!/bin/sh
intern=DP-0
extern=HDMI-0

if xrandr | grep "$extern disconnected"; then
    xrandr --output "$extern" --off --output "$intern" --auto
else
    xrandr --output "$intern" --off --output "$extern" --auto --rotate right
fi
