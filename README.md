# ranger-vuration
A plugin for calculating video duration in ranger file manager.

### Features

- Get the duration of single and multiple video files using selection mark  feature of ranger.

### Install

Git to clone this repository into your
`~/.config/ranger/plugins` folder. For example:

```sh
git clone git@github.com/username/ranger-vuration.git ~/.config/ranger/plugins/vuration
```

Or you can install it just by directly positioning the init file inside the plugins.
```sh
wget -O ~/.config/ranger/plugins/vuration.py https://raw.githubusercontent.com/krr0ption/ranger-vuration/master/__init__.py
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
