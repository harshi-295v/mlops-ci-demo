from kfp import dsl, local

@dsl.component(base_image="python:3.11")
def hello(name: str) -> str:
    message = f"Hello from KFP DockerRunner, {name}!"
    print(message)
    return message

@dsl.pipeline(name="hello-docker-pipeline")
def hello_pipeline(name: str = "MLOps Students"):
    hello_task = hello(name=name)

if __name__ == "__main__":
    local.init(runner=local.DockerRunner())
    hello_pipeline(name="MLOps Students")
