# ranger-vuration
A plugin for calculating video duration in ranger file manager.

### Features

- Get the duration of single and multiple video files using selection feature of ranger.
- [ ] Results are printed in a TUI and accessable dialog
- [ ] The history of the files analyzed files can be tracked and reviewed

### Install

Git to clone this repository into your
`~/.config/ranger/plugins` folder. For example:

```sh
git clone git@github.com/krr0ption/ranger-vuration.git ~/.config/ranger/plugins/vuration
```

### Usage
Moving your cursor over the target file and use the below command.
```
:vuration
```
You can add add keybinding for this command in your `rc.conf`.
```
map <C-v> vuration
```

The same command can be used for getting the total duration of files that are marked with `<space>`.
