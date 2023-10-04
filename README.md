# Simplify Path
## Usage

### Install

```console
$ pipx install git+ssh://git@github.com/nagomiso/simplify-path.git
```

### Set bashrc

```bashrc
export PATH="foo:${PATH}"
export PATH="bar:${PATH}"
export PATH="foo:${PATH}"
echo "${PARH}"  # foo:bar:foo
export PATH="${simplify-path}"
echo "${PARH}"  # foo:bar
```
