#PyPoll
import csv
import os

#Directory 
vote_data = os.path.join('..','Resources','election_data.csv')

#inital variables
vote_cast = []
candidates_list = []
candidate_vote = []
candidate_percent = []

invVoteNum = {}


#Read file
with open(vote_data, mode='r') as csvfile:
    #Only get the info from each column instead of the special characters
    file_data = csv.reader(csvfile, delimiter=',')
    next(file_data,None)

    #Reading the file
    for row in file_data:
        #List for all the ticket number
        vote_cast.append(row[0])
        TotalNumVote = len(vote_cast)

        #List for all the candidates
        candidates_list.append(row[2])

#print(TotalNumVote)

print("Election Results")
print("-----------------------")
print("Total Votes: " + str(TotalNumVote))
print("-----------------------")


#Get distinct value from a list
dis_candidates_list = set(candidates_list)
#print(dis_candidates_list)

#Get vote number / percentage for each candidate
for i in dis_candidates_list:
    temp_candidate_vote = candidates_list.count(i)
    candidate_vote.append(temp_candidate_vote)

    temp_candidate_percent = round((candidates_list.count(i)/TotalNumVote)*100,3)
    candidate_percent.append(temp_candidate_percent)
    print(f"{i}: {str(temp_candidate_percent)}% ({temp_candidate_vote})")

#print(candidate_percent)
#print(candidate_vote)

print("-----------------------")

#Get the winner
MaxVote = max(candidate_vote)
MaxPosition = candidate_vote.index(MaxVote)
dis_candidates_list = list(dis_candidates_list)
Winner = dis_candidates_list[MaxPosition]

print("Winner: " + Winner)
print("-----------------------")