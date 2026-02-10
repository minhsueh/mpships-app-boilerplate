## 🚢 MPShips APP Boilerplate

The MPShips App Boilerplate helps you quickly create a new MPShips application using [cookiecutter](https://github.com/cookiecutter/cookiecutter). It provides a ready-to-use project structure with sensible defaults so you can focus on building your app, not setup.


### Getting Started
1. Install Cookiecutter
```
$ pip install cookiecutter
```
2. Create a new MPShips App
```
$ cookiecutter gh:minhsueh/mpships-app-boilerplate
```
3. Customize your project by answering the following questions:
- `project_name`: The full project name. Default: `My MPships App`
- `project_shortname`: Used as the Python package directory name. Typically the lowercase version of `project_name`, with hyphen("-") and space(" ") with underscore("_"). Default: `my_mpships_app`
- `author_name`: Author name for `pyproject.toml` and package metadata.
- `author_email`: Author email for pyproject.toml and package metadata.
- `description`: A short description of your project, used in `pyproject.toml` and `README.md`.
- `first_version`: Initial project version. Default: `0.1.0`
- `license`: Choose one of the following licenses: `MIT License`, `BSD License`, `ISC License`,`Apache Software License 2.0`, `GNU General Public License v3`, `Not open source`. Default: `1` (`MIT License`)
- `install_dependencies`: Automatically create a virtual environment and install default dependencies. Default: `y`