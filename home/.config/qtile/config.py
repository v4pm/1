# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"

keys = [
    # Toggle floating
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'),

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Launch programs
    Key([mod], "Return", lazy.spawn('alacritty'), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn('firefox'), desc="Launch browser"),
    Key([mod, "control"], "b", lazy.spawn('firefox -P profile2'), desc="Launch firefox 2nd profile"),
    Key([mod], "f", lazy.spawn('pcmanfm'), desc="Launch file manager"),
    Key([mod], "p", lazy.spawn('keepassxc'), desc="Launch password manager"),
    Key([mod, "control"], "d", lazy.spawn('discord'), desc="Launch discord"),
    Key([mod, "control"], "p", lazy.spawn('pycharm'), desc="Launch pycharm"),
    Key([mod, "control"], "t", lazy.spawn('telegram-desktop'), desc="Launch telegram"),
    Key([mod], "u", lazy.spawn(
        'alacritty --title "Arch Updater" -e bash -c "sudo pacman -Syu ; echo Done - Press enter to exit; read"'),
        desc="Arch Updater"
        ),
    Key([mod], "c", lazy.spawn('chromium'), desc="Launch chromium"),
    Key([mod, "control"], "e", lazy.spawn('thunderbird'), desc="Launch email client"),
    Key([mod], "a", lazy.spawn('android/android-studio/bin/studio.sh'), desc="Launch android sudio"),
    Key([mod], "v", lazy.spawn('vlc'), desc="Launch CLC media player"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(f'  {i}  ') for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name.strip(),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name.strip(),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# colors =('#1c1b22', '#42414d', '#9e9ea5', '#fbfbfe', '#00ddff',)
colors = [
    '#F5F5F5',  # white
    '#D6D6D6',  # grey
    '#141414',  # black
    '#FB3640',  # pink
    '#232ED1',  # blue
    '#B8B8B8',  # grey text
]

window_spacing = 4

layouts = [
    layout.Columns(
        border_focus=colors[1],
        border_normal=colors[0],
        margin=window_spacing,
        margin_on_single=window_spacing,
        border_on_single=True,
        insert_position=1,
        border_width=2,
        border_focus_stack=colors[4],
        border_normal_stack=colors[3]
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Open Sans SemiBold",
    fontsize=12,
    padding=4,
    foreground=colors[2],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='line',
                    highlight_color=colors[1],
                    active=colors[2],
                    inactive=colors[5],
                    block_highlight_text_color=colors[2],
                    borderwidth=0,
                    margin_x=0,
                    margin_y=3,
                    background=colors[0],
                    disable_drag=True,
                    # use_mouse_wheel=False,
                ),
                widget.Spacer(length=2, background=colors[0]),
                widget.Prompt(),

                widget.WindowName(format=' {name}', max_chars=150),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),

                widget.CPU(format='  {load_percent}%'),
                widget.ThermalSensor(fmt=' {}', foreground=colors[2]),
                widget.Memory(measure_mem='G', format=' {MemUsed: .1f}{mm}'),
                # widget.TextBox(text='   ', fontsize=14),

                widget.Systray(icon_size=15, padding=8),
                widget.Clock(format="   %b %d %a %H:%M"),
                widget.TextBox(text=''),
                # widget.Volume(fmt='Vol: {}'),
            ],
            size=24,
            margin=[window_spacing * 2, window_spacing * 2, window_spacing, window_spacing * 2],
            background=colors[1],
            border_width=2,  # Draw top and bottom borders
            border_color=colors[0]  # Borders are magenta
        ),
        bottom=bar.Gap(window_spacing),
        left=bar.Gap(window_spacing),
        right=bar.Gap(window_spacing),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors[1],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry

        Match(title='Arch Updater'),
        Match(wm_class="transmission-gtk"),
        Match(wm_class="telegram-desktop"),
        Match(wm_class="discord"),

    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
