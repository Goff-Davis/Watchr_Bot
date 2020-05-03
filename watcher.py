import datetime
import json
import praw

with open("config.json") as json_data_file:
	data = json.load(json_data_file)

SEARCH_STRINGS = data["search_strings"]
CATEGORY = data["search_category"]
USER = data["user"]
SUBREDDIT = data["subreddit"]
TIME_FILTER = data["time_filter"]

def main():
	reddit = create_reddit()
	destination_user = reddit.redditor(USER)
	subreddit_to_search = reddit.subreddit(SUBREDDIT)

	search_results = search(subreddit_to_search)

	if found_submissions(search_results):
		message = create_message(search_results)
		send_message(message, destination_user)

def create_reddit():
	return praw.Reddit(
		"watcher",
		user_agent="web:watcher:v0.1.0 (by u/MrGamer00)"
	)

def search(subreddit):
	results = {}

	for keyword in SEARCH_STRINGS:
		query = subreddit.search(
			keyword,
			sort="new",
			time_filter=TIME_FILTER
		)

		query_results = []

		for submission in query:
			query_results.append(submission)

		if len(query_results) > 0:
			results[keyword] = query_results

	return results

def found_submissions(search_results):
	return bool(search_results)

def create_message(search_results):
	keywords = list(search_results)
	category_list = ""
	links = ""
	i=0

	for keyword in keywords:
		if (i < len(keywords) - 1):
			category_list += "**" + keyword + "**, "
		else:
			category_list += "**" + keyword + "** "

		links += "\n\n## " + keyword + "\n"

		for submission in search_results[keyword]:
			date_created = generate_date_string(submission)

			links += "- [" + submission.title + "](" + submission.permalink + ") (" + date_created + ")\n"

		i += 1

	header = "# New Listings Found\n\n" + CATEGORY + " in the categories: " + category_list + "have been found.\n\n"
	body = "Links to the postings:" + links

	return header + body

def generate_date_string(submission):
	date = datetime.datetime.fromtimestamp(submission.created_utc)

	return date.strftime("%m-%d-%Y %H:%M")

def send_message(message, user):
	user.message(
		"" + CATEGORY + " has been posted.",
		message
	)

if __name__ == "__main__":
	main()
