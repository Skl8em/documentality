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
            # our validators (linkcheck, frontmatter, ULID); pyyaml is the frontmatter
            # parser (Phase 11 T2), pinned here with the interpreter it runs in
            (pkgs.python3.withPackages (ps: [ ps.pyyaml ]))
            pkgs.git # the validators derive the repo root and file list from git
            # the engine, docsys/ (and this repository's own .venv): uv installs the
            # Python packages its uv.lock pins, into a .venv built on this flake's
            # interpreter, never on one uv downloads or finds elsewhere
            pkgs.uv
          ];

          shellHook = ''
            export DOCSYS_DEVSHELL=1  # lets scripts/check.py know the pinned tools are on PATH
            export UV_PYTHON=${pkgs.python3}/bin/python3  # every .venv is built on this interpreter
            export UV_PYTHON_DOWNLOADS=never              # and uv fetches none of its own
            echo "documentation-system devShell:"
            echo "  markdownlint-cli2 $(markdownlint-cli2 2>&1 | head -1 | sed 's/^markdownlint-cli2 //')"
            echo "  $(node --version)  |  $(python3 --version)  |  $(uv --version)"
            echo "Run the full gate with: python3 scripts/check.py"
          '';
        };
      });

      # `nix fmt` convenience (formats this flake).
      formatter = forAllSystems (pkgs: pkgs.nixfmt-rfc-style);
    };
}
