"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [1],
            "answer": [1]
        },
        {
            "input": [2],
            "answer": [2,1]
        },
        {
            "input": [3],
            "answer": [3,10,5,16,8,4,2,1]
        }
    ],
    "Extra": [
        {
            "input": [5],
            "answer": [5,16,8,4,2,1]
        },
    ]
}
