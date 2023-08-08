from click.testing import CliRunner
from src.combinations_coins.__main__ import start


class TestCoins:
    def test_start(self):
        runner = CliRunner()
        result = runner.invoke(start, ['--goal', 5])
        assert result.exit_code == 0
        assert result.output == 'Las posibles combinaciones son: \n[[5], [5]]\n'

    def test_no_combinations(self):
        runner = CliRunner()
        value = 1
        result = runner.invoke(start, ['--goal', value])
        assert result.exit_code == 0
        assert result.output == f'**** No se pueden generar posibles combinaciones para la cantidad {value}. ****\n'
