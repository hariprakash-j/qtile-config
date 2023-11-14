#!/bin/bash

# Disabling display auto off
xset s off -dpms

# Starting the compositor
picom -b &

# Applying the wallpaper
nitrogen --restore

nextcloud &
gtk-launch feishin &
signal-desktop &
librewolf &
freetube &
signal-desktop &
thunar &

# launching the proton bridge and thunderbird after a delay
protonmail-bridge --noninteractive &
sleep 10
thunderbird &