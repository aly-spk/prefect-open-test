from prefect import flow


@flow
def test_workflow() -> str:
    print("Runnning test")
    return "Work flow test"


if __name__ == '__main__':
    test_workflow()
