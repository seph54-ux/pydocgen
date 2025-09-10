{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [
    (pkgs.python3.withPackages (ps: [
      ps.flask
      ps.python-docx
      ps.matplotlib
      ps.reportlab
      ps.fpdf
    ]))
  ];
  # Sets environment variables in the workspace
  env = {
    FLASK_APP = "main.py";
  };
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      "ms-python.python"
    ];
    # Enable previews
    previews = {
      enable = true;
      previews = {
        web = {
          command = ["flask" "run" "--host=0.0.0.0" "--port=$PORT"];
          manager = "web";
        };
      };
    };
    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Python packages are managed by Nix
      };
      # Runs when the workspace is (re)started
      onStart = {
      };
    };
  };
}
