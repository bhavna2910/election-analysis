#Add our dependencies
import csv
from distutils import text_file
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Resources/analysis", "election_analysis_county.txt")

# 1. Initialize a total vote counter
total_votes = 0

# candidates options and candidate votes
candidate_options = []
county_options = []
# 1. Declare the empty dictionary
candidate_votes = {}
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Winning County and Winning Count Tracker
winning_county = ""
winning_count_county = 0
winning_percentage_county = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
# Read and print the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader: 
    # Add to the total vote count.
        total_votes += 1

    # Print the county name from each row.
        county_name = row[1]
        candidate_name = row[2]
    
        if county_name not in county_options:
        # Add the county name to the county list.
            county_options.append(county_name)
        
        # Begin tracking that county's vote count.
            county_votes[county_name] = 0
        
        # Add a vote to that county's count
        else: 
            county_votes[county_name] += 1

        if candidate_name not in candidate_options:
        # Add the county name to the county list.
            candidate_options.append(candidate_name)

        # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        else: 
            candidate_votes[candidate_name] += 1

    with open(file_to_save, "w") as txt_file:
        
        # Save the final vote count to the text file.
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")

        print("County Votes:\n" )

        txt_file.write(election_results)
        txt_file.write("County Votes:\n")


                # Determine the percentage of votes for each county by looping through the counts.
        # 1. Iterate through the county list.
        for county_name in county_votes:
            # 2. Retrieve vote count of a candidate.
            votes = county_votes[county_name]
            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # 4. Print the candidate name and percentage of votes.
            #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
            print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
            txt_file.write(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
            if (votes > winning_count_county) and (vote_percentage > winning_percentage_county):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
                winning_count_county = votes
                winning_percentage_county = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
                winning_county = county_name

        #To do: print out the winning candidate, vote count and percentage to terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        largest_county = (
            f"-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n"
        )
        print(largest_county)
        txt_file.write(largest_county)
        
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # 4. Print the candidate name and percentage of votes.
            #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            txt_file.write(f"\n")

            # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

        txt_file.close()


    






