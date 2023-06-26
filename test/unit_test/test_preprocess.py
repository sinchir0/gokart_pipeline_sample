import pandas as pd
import pytest

from gokart_pipeline_sample.pipeline.preprocess import PreprocessTask


class TestMakeAreaTask:
    @pytest.mark.parametrize(
        ("length", "width", "expect"),
        [
            (
                pd.Series([2.0, 4.0, 6.0]),
                pd.Series([1.0, 2.0, 3.0]),
                pd.Series([2.0, 8.0, 18.0])
            )
        ],
    )
    def test_run_imp(
        self,
        length: pd.Series,
        width: pd.Series,
        expect: pd.Series
    ) -> None:
        actual = PreprocessTask.make_area(length, width)
        assert actual.equals(expect)