from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int):
    """
    Run the Presidio anonymizer with provided parameters.

    Args:
        text (str): The input text.
        start (int): Start index of the entity.
        end (int): End index of the entity.

    Returns:
        AnonymizerResult: The anonymized result object.
    """
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(
                entity_type="PERSON",
                start=start,
                end=end,
                score=0.8
            )
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    return result


if __name__ == "__main__":
    # Keep CLI interactivity only here
    user_text = input("text: ")
    user_start = int(input("start: "))
    user_end = int(input("end: "))

    result = sample_run_anonymizer(user_text, user_start, user_end)
    print(result)
