import os
import csv

#Find file
os.chdir(os.path.dirname(__file__))
csvpath = os.path.join("election_data.csv")

#open file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #Skip header
    row = next(csvreader)

 #Total votes casted
    num_votes = 0
    candidates = []
    votes = []

    for row in csvreader:
        num_votes += 1
#candidates data
#candidate voted for
        candidate = row[2]
#add other votes to corresponding candidate
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            votes[candidate_index] = votes[candidate_index] + 1
        else:
            candidates.append(candidate)
            votes.append(1)
#Find percentages

percentages = []
max_votes = votes[0]
index = 0
for count in range(len(candidates)):
    vote_percentage = votes[count]/num_votes*100
    percentages.append(vote_percentage)
    if votes[count] > max_votes:
        max_votes = votes[count]
        index = count
#print(max_votes)
winner = candidates[index]

#print
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({votes[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#write file

filewriter = open('poll_result.txt', 'w')

filewriter.write(f"Election Results\n")
filewriter.write(f"----------------------------------------------\n")
filewriter.write(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({votes[count]})\n")
filewriter.write("---------------------------\n")  
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

filewriter.close()




