# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.5.0] - 2021-08-14
### Added
- Add `conftest fmt` option (thanks [@artis3n](https://github.com/artis3n)!)

## [1.4.1] - 2021-06-06
### Changed
- Fix "opa check" test to include all files.

## [1.4.0] - 2021-02-08
### Changed
- Include all files for test/verify, not just staged.

## [1.3.0] - 2020-08-31
### Changed
- Removed unused python hooks.

## [1.2.1] - 2020-08-21
### Changed
- Fix typo in conftest test hook.

## [1.2.0] - 2020-08-17
### Added
- conftest hooks.

## [1.1.0] - 2020-08-16
### Changed
- Use "system" style hooks rather than python ones as we don't need custom logic yet.

## [1.0.0] - 2020-08-16
### Changed
- First release, adding pre-commit checks with `opa fmt`, `opa check` and `opa test`
