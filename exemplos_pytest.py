# -*- coding: utf-8 -*-
# content of test_sample.py
import pytest
import sys


def func(x):
    return x + 1


@pytest.mark.parametrize("v_input, v_esperado",
                         [
                            (1, 2),
                            (2, 3),
                            (3, 4)
                         ])
def test_func(v_input, v_esperado):
    assert func(v_input) == v_esperado


@pytest.mark.linux  # marca registrada em pytest.ini
def test_func_2():
    # habilitando pdb via pytest
    # pytest.set_trace()
    assert func(1) == 2


@pytest.mark.windows  # marca registrada em pytest.ini
def test_func_3():
    assert func(3) == 4


# @pytest.mark.skip(reason='Pulando teste com valor 4')
@pytest.mark.skipif(sys.version_info > (3, 9), reason='Pular nas versões maiores que 3.8')
def test_com_valor_4():
    assert func(4) == 5


if __name__ == "__main__":
    # executar apenas o teste contendo valor_3 => pytest -v -k valor_3
    # pytest.main(args=['-v', '-k', 'valor_3'])
    # executar apenas os testes marcados como windows => pytest -m windows -v
    # pytest.main(args=['-m', 'windows', '-v'])
    # executar todos os testes no modo verbose => pytest -v
    pytest.main(args=['-v'])
