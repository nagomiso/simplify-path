# Simplify PATH
## Install

```console
$ pipx install git+ssh://git@github.com/nagomiso/simplify-path.git
```

## Usage

```bash
$ export PATH="/foo:${PATH}"
$ export PATH="/bar:${PATH}"
$ export PATH="/foo:${PATH}"
$ echo "${PARH}"  # /foo:/bar:/foo
$ export PATH="${simplify-path}"
$ echo "${PARH}"  # /foo:/bar
```
