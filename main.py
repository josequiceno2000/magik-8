from user_input import get_user_input
from sentiment_analysis import sentiment_analysis

def main():
    """Gets user input via speech to text and outputs it to the console"""
    user_question = get_user_input()
    sentiment_analysis(user_question)


if __name__ == "__main__":
    main() 