{
  description = "documentation-system — reproducible per-project tooling devShell (Phase 09)";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";

  outputs =
    { self, nixpkgs }:
    let
      # CI runs on linux; the maintainer is on x86_64-darwin. Keep all four.
      systems = [
        "x86_64-darwin"
        "aarch64-darwin"
        "x86_64-linux"
        "aarch64-linux"
      ];
      forAllSystems = f: nixpkgs.lib.genAttrs systems (system: f (import nixpkgs { inherit system; }));
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          # Project tooling is PINNED here, not in home-manager: markdownlint's
          # version is part of the contract with our custom rules (its rule API
          # shifts across majors), so it is frozen per project via flake.lock —
          # the same bit-for-bit binary locally and in CI.
          packages = [
            pkgs.markdownlint-cli2 # markdown linter; shares config with the VSCode extension
            pkgs.nodejs # runtime for markdownlint + the custom rule module
            pkgs.python3 # our validators (linkcheck, frontmatter, ULID) — stdlib only
          ];

          shellHook = ''
            echo "documentation-system devShell:"
            echo "  markdownlint-cli2 $(markdownlint-cli2 2>&1 | head -1 | sed 's/^markdownlint-cli2 //')"
            echo "  $(node --version)  |  $(python3 --version)"
            echo "Run the full gate with: python3 scripts/check.py"
          '';
        };
      });

      # `nix fmt` convenience (formats this flake).
      formatter = forAllSystems (pkgs: pkgs.nixfmt-rfc-style);
    };
}
