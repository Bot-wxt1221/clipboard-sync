{
  pkgs ? import <nixpkgs> { },
}:
pkgs.rustPlatform.buildRustPackage {
  buildInputs = with pkgs; [ ibxcb ];

  pname = "clipboard-sync";
  version = "0.2.0";
  cargoLock.lockFile = ./Cargo.lock;
  src = ./.;
}
