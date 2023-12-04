from __future__ import annotations

import typing as t
from pathlib import Path

from sphinx.application import Sphinx

if t.TYPE_CHECKING:  # We get circular imports otherwise
    from pharaoh.project import PharaohProject
    from pharaoh.templating.second_level.template_env import PharaohTemplateEnv


class PharaohSphinx(Sphinx):
    # Set by entrypoint of Sphinx plugin "asset_ext"
    # ...sphinx_ext.asset_ext.setup()
    pharaoh_proj: PharaohProject | None = None
    # Set by entrypoint of Sphinx plugin "jinja_ext"
    # ...jinja_ext.setup()
    pharaoh_te: PharaohTemplateEnv | None = None

    @property
    def assets_dir(self):
        return Path(self.builder.outdir) / "pharaoh_assets"
