from prefect import flow
from prefect.logging import get_run_logger


@flow
def test_workflow(message: str = "what!") -> str:
    l = get_run_logger()
    l.info(f"Runnning test with {message}")
    return "Work flow test"


if __name__ == '__main__':
    test_workflow()
