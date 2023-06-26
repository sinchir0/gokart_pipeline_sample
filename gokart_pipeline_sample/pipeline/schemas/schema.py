import pandera as pa
from pandera.typing import Series


class BaseSchema(pa.SchemaModel):
    class Config:
        coerce = True


class IrisFeatureSchema(BaseSchema):
    """
    Irisデータの特徴量のスキーマ
    """

    id: Series[int] = pa.Field(nullable=False, description="id")
    sepal_length: Series[float] = pa.Field(gt=0.0, nullable=False, description="がく片の長さ(cm)")
    sepal_width: Series[float] = pa.Field(gt=0.0, nullable=False, description="がく片の幅(cm)")
    petal_length: Series[float] = pa.Field(gt=0.0, nullable=False, description="花びらの長さ(cm)")
    petal_width: Series[float] = pa.Field(gt=0.0, nullable=False, description="花びらの幅(cm)")
    target: Series[int] = pa.Field(isin=(0, 1, 2), nullable=False, description="あやめの種類")


class PreprocessedSchema(BaseSchema):
    """
    前処理済データのスキーマ
    """

    id: Series[int] = pa.Field(nullable=False, description="id")
    sepal_length: Series[float] = pa.Field(gt=0.0, nullable=False, description="がく片の長さ(cm)")
    sepal_width: Series[float] = pa.Field(gt=0.0, nullable=False, description="がく片の幅(cm)")
    petal_length: Series[float] = pa.Field(gt=0.0, nullable=False, description="花びらの長さ(cm)")
    petal_width: Series[float] = pa.Field(gt=0.0, nullable=False, description="花びらの幅(cm)")
    petal_area: Series[float] = pa.Field(gt=0.0, nullable=False, description="花びらの面積(cm^2)")
    target: Series[int] = pa.Field(isin=(0, 1, 2), nullable=False, description="あやめの種類")


class OutputSchema(BaseSchema):
    """
    出力データのスキーマ
    """

    id: Series[int] = pa.Field(nullable=False, description="id")
    pred: Series[int] = pa.Field(isin=(0, 1, 2), nullable=False, description="推論結果")
