let
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix/";
    ref = "refs/tags/3.3.0";
  }) {
    # optionally bring your own nixpkgs
    # pkgs = import <nixpkgs> {};

    # optionally specify the python version
    python = "python38";
  };
in
mach-nix.mkPythonShell {
  requirements = ''
${builtins.readFile ./requirements.txt}
jupyterlab'';
}
