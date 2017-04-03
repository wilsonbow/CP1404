"""
CP1404/CP5632 Practical
CSV scores file program - broken one
scores file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.

Fixed!
"""


def main():
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []

    # Store scores in a list of lists
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()

    # Print scores per subject
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        subject_scores = []
        for score_number in range(len(score_values)):
            score = score_values[score_number][i]
            subject_scores.append(score)
            print(score)
        print("Max:", max(subject_scores))
        print("Min:", min(subject_scores))
        print("Average:",sum(subject_scores)/len(subject_scores))
        print()


main()