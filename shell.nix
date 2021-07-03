let
  _default = "conda,nixpkgs,wheel";
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix/";
    ref = "master";
  }) {};
in mach-nix.mkPythonShell {
  requirements = builtins.readFile ./requirements.txt;
}
