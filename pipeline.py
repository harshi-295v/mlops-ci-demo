from kfp import dsl, local


@dsl.component(base_image="python:3.11")
def prepare_data() -> str:
    print("Preparing data for the ML pipeline")
    return "Data prepared successfully"


@dsl.component(base_image="python:3.11")
def train_model(data_status: str) -> str:
    print(f"Training model using: {data_status}")
    return "Model trained successfully"


@dsl.pipeline(name="mlops-local-pipeline")
def ml_pipeline():
    data_task = prepare_data()
    train_model(data_status=data_task.output)


if __name__ == "__main__":
    local.init(
        runner=local.SubprocessRunner(use_venv=False),
        raise_on_error=False
    )
    ml_pipeline()
