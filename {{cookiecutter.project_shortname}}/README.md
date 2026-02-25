## {{cookiecutter.project_name}}

{{cookiecutter.description}}


## Get started
1. Make sure you are developing inside a virtual environment to manage dependencies properly.
2. Add your awesome design to: `src/{{cookiecutter.description}}/pages/`
3. To query data from the Materials Project API, use:
```
from mpships_infra import get_mp_rester

mpr = get_mp_rester()
docs = mpr.materials.summary.search(material_ids = ["mp-149"])
```