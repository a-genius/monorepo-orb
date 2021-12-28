import pytest

from src.scripts.prepare_modules import get_modules, check_configs_exist, dump_modules, main
from src.tests.conftest import does_not_raise


@pytest.mark.parametrize(
    "modules, expected",
    [
        (["module1", "module2"], {"module1/.circleci/config.yml\n", "module2/.circleci/config.yml\n"}),
        (["module1/.circleci/config.yml\n"], {"module1/.circleci/config.yml\n"}),
        (["module1/.circleci/config.yml"], {"module1/.circleci/config.yml\n"}),
        ([".circleci/common_config.yml"], {".circleci/common_config.yml\n"}),
        ([], set()),
    ]
)
def test_get_modules(modules, expected):
    assert get_modules(modules) == expected


@pytest.mark.parametrize(
    "files, expected_paths, expectation",
    [
        (["one", "two"], ["one", "two"], does_not_raise()),
        (["one"], ["one", "two"], pytest.raises(FileNotFoundError)),
    ], indirect=["files"]
)
def test_check_configs_exist(tmpdir, files, expected_paths, expectation):  # pylint: disable=unused-argument
    expected_paths = [tmpdir / x for x in expected_paths]
    with expectation:
        check_configs_exist(expected_paths)


def test_dump_modules(monkeypatch, tmpdir):
    path = tmpdir / "modules.txt"
    to_dump = ["test\n", "test2\n"]
    monkeypatch.setenv("MODULES_PATH", str(path))
    dump_modules(to_dump)
    with open(path) as fd:
        assert fd.readlines() == to_dump


@pytest.mark.parametrize(
    "default_modules, modules_file, expected",
    [
        ("module1,module2", [], ["module1/.circleci/config.yml\n", "module2/.circleci/config.yml\n"]),
        ("", ["module1", "module2"], ["module1/.circleci/config.yml\n", "module2/.circleci/config.yml\n"]),
        (
            "module1,module2", ["module1", "module3"],
            ["module1/.circleci/config.yml\n", "module2/.circleci/config.yml\n", "module3/.circleci/config.yml\n"]
        ),
        ("", [], []),
    ], indirect=["modules_file"]
)
def test_main(monkeypatch, tmpdir, default_modules, modules_file, expected):
    monkeypatch.setenv("DEFAULT_MODULES", default_modules)
    monkeypatch.setenv("MODULES_PATH", str(modules_file))
    monkeypatch.setattr("src.scripts.prepare_modules.check_configs_exist", lambda x: True)
    main()
    with open(str(modules_file)) as fd:
        assert fd.readlines().sort() == expected.sort()
