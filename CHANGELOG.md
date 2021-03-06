# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] - 2022-01-16
### Changed
- fixed an issue where `setup-and-continue` and `setup-without continue` jobs were not passing `get-base-from-github`
parameter to the `prepare-pipeline-files` command

## [0.2.0] - 2022-01-16
### Added
- new `pre-continue` parameter in `setup-and-continue` job that allows to specify an array of steps to run
  before continuation is triggered

### Changed
- in main, when trying to get the diff block, first try to run `find_diff_files` without specifying remote.
  Specify remote only if it fails. I've found out that this approach reduces the number of git errors.

## [0.1.5] - 2022-01-16
### Changed
- specify remote when getting the diff. Now remote is assigned to a variable in main and passed to both get_base and
  find_diff_files
- improves error message in the catch block when getting the diff

## [0.1.4] - 2022-01-16
### Added
- message that is printed out when the pattern matches in the commit subject.
- exception handling in the case when getting the diff fails. This happens in cases when polyrepo is merged together
  to create a monorepo.

### Changed
- `mappings` doc updated with the explanation that `re.search` is used when looking at last commit subject


## [0.1.3] - 2022-01-07
### Changed
- multiple modules that are specified in the mapping are now split using a comma as a delimiter
- slashes are not added to the end of module paths anymore in `prepare-pipeline-files` and `prepare_files.py`

## [0.1.2] - 2022-01-07
### Changed
- behavior of `prepare_modules.py::get_modules` method. It no longer adds newlines to the constructed paths.
- `default-modules.txt` doc now says that a custom path to config must end in `config.yml`
- tests updated to reflect the change
- fix the tests that were doing incorrect comparison

## [0.1.1] - 2022-01-07
### Changed
- behavior of `prepare_file.py::set_params_and_modules` method. It now does what the documentation states.
  It no longer dumps the JSON array into the file, but adds modules to the file separated by line breaks.
- tests updated to reflect the change

## [0.1.0] - 2022-01-06
A minor release to indicate the fast pace of changes
### Added
- Initial release of CircleCI orb.

[Unreleased]: https://github.com/a-genius/monorepo-orb/compare/v0.2.1...main
[0.2.1]: https://github.com/a-genius/monorepo-orb/releases/tag/v0.2.1
[0.2.0]: https://github.com/a-genius/monorepo-orb/releases/tag/v0.2.0
[0.1.5]: https://github.com/a-genius/monorepo-orb/releases/tag/v0.1.5
[0.1.4]: https://github.com/a-genius/monorepo-orb/releases/tag/v0.1.4
[0.1.3]: https://github.com/a-genius/monorepo-orb/releases/tag/v0.1.3
[0.1.2]: https://github.com/a-genius/monorepo-orb/releases/tag/v0.1.2
[0.1.1]: https://github.com/a-genius/monorepo-orb/releases/tag/v0.1.1
[0.1.0]: https://github.com/a-genius/monorepo-orb/releases/tag/v0.1.0
