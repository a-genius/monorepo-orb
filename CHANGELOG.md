# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2022-01-07
### Changed
- behavior of `prepare_file.py::set_params_and_modules` method. It now does what the documentation states.
  It no longer dumps the JSON array into the file, but adds modules to the file separated by line breaks.
- tests updated to reflecte the change

## [0.1.0] - 2022-01-06
A minor release to indicate the fast pace of changes
### Added
- Initial release of CircleCI orb.

[Unreleased]: https://github.com/a-genius/monorepo-orb/compare/v0.1.0...main
[0.1.1]: https://github.com/a-genius/monorepo-orb/releases/tag/v0.1.1
[0.1.0]: https://github.com/a-genius/monorepo-orb/releases/tag/v0.1.0
