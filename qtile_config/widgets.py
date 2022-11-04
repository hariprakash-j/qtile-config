from libqtile import widget
from .def_theme import colors

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=1
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=35,
        padding=-5
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]

primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color2', 'dark'),

    widget.Notify(**base(bg='focus')),

    powerline('dark', 'color2'),

    icon(bg="dark", fg="light", text='  '),

    widget.Volume(**base(bg='dark', fg='light')),

    powerline('color2', 'dark'),

    icon(bg="color2", text='  '),  # Icon: nf-fa-feed
    
    widget.Wlan(**base(bg='color2'), interface='wlp4s0', format="{essid} ({percent:2.0%})"),

    powerline('dark', 'color2'),

    widget.CurrentLayoutIcon(**base(bg='dark'), scale=0.55),

    widget.CurrentLayout(**base(bg='dark', fg='light'), padding=5),

    powerline('color2', 'dark'),

    icon(bg="color2", fontsize=17, text='  '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color2'), format='%A %d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color2', 'dark'),

    powerline('dark', 'color2'),

    widget.CurrentLayoutIcon(**base(bg='dark'), scale=0.65),

    widget.CurrentLayout(**base(bg='dark', fg='light'), padding=5),
]

