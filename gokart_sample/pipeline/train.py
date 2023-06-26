import gokart
import lightgbm as lgb

from gokart_sample.utils.template import GokartTask


class TrainTask(GokartTask):
    train_task = gokart.TaskInstanceParameter()
    valid_task = gokart.TaskInstanceParameter()

    def requires(self) -> None:
        return {"train": self.train_task, "valid": self.valid_task}

    def run(self) -> None:
        train = self.load("train")
        valid = self.load("valid")

        X_train, y_train = train["X_train"], train["y_train"]
        X_valid, y_valid = valid["X_valid"], valid["y_valid"]

        # パラメータの設定
        params = {
            "application": "multiclass",
            "objective": "softmax",
            "metric": "multi_logloss",
            "is_unbalance": "true",
            "boosting": "gbdt",
            "num_leaves": 31,
            "feature_fraction": 0.5,
            "bagging_fraction": 0.5,
            "bagging_freq": 20,
            "learning_rate": 0.05,
            "verbose": 0,
            "num_class": 3,
        }

        lgb_train = lgb.Dataset(X_train, y_train)
        lgb_eval = lgb.Dataset(X_valid, y_valid, reference=lgb_train)

        # モデルの学習
        model = lgb.train(
            params,
            train,
            num_boost_round=5000,
            valid_sets=lgb_eval,
            callbacks=[lgb.early_stopping(stopping_rounds=100)],
        )
        breakpoint()
        return model
