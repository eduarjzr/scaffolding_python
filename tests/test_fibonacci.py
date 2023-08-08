from click.testing import CliRunner
from src.fibonacci_exercise.__main__ import start


class TestFibonacci:
    def test_start(self):
        runner = CliRunner()
        result = runner.invoke(start, ['--long', 2])
        assert result.exit_code == 0
        assert result.output == '[0, 1]\n'
