# Import Dependencies
import os
import csv

def dash():
    return "-------------------------"


# Create the read and write paths
csvpath = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "PyPoll.txt")

with open(csvpath, encoding='UTF-8') as csvfile, open(output_path,"w") as txtfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

    print("Election Results")
    print(dash())
    txtfile.write("Election Results \n")
    txtfile.write(f"{dash()} \n")

    totalVote = 0
    candidate = []
    # Find the total number of votes and make a list of candidates
    for row in csvreader:
        totalVote += 1
        if row[2] not in candidate:
            candidate.append(row[2])
    print ("Total Votes: " + str(totalVote))
    print(dash())
    txtfile.write(f"Total Votes: {totalVote} \n")
    txtfile.write(f"{dash()} \n")

highest = 0
winner = "" 
for x in candidate:  
    with open(csvpath, encoding='UTF-8') as csvfile, open(output_path,"a") as txtfile:
        csvreader = csv.reader(csvfile, delimiter=",") 
        csv_header = next(csvreader)
        candidateVote = 0
        percent = 0.00

        # Find the total number of votes each candidate won
        for y in csvreader:
            if y[2] == x:
                candidateVote += 1

        # Find the percentage of votes each candidate won
        percent = '{0:.3f}'.format((candidateVote/totalVote)*100)

        # Find the winner
        if candidateVote > highest:
            highest = candidateVote
            winner = x
        print(f"{x}: {percent}% ({candidateVote})")
        txtfile.write(f"{x}: {percent}% ({candidateVote}) \n")
print(dash())
print(f"Winner: {winner}")
print(dash())

with open(output_path,"a") as txtfile:
    txtfile.write(f"{dash()} \n")
    txtfile.write(f"Winner: {winner} \n")
    txtfile.write(f"{dash()} \n")

    