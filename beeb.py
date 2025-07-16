########################################################################################################################
# API Scraper for gathering data from various Capcom Cup related tournaments.
#
########################################################################################################################
import argparse
import os
import sys

def challonge_scrape(user, apikey, owner, name, target):
    print("Fetching Challonge Bracket: %s" % (str(name)))

    os.system(
        "curl -XGET -k -v https://%s:%s@api.challonge.com/v1/tournaments/%s-%s.json " \
        "| python3 -m json.tool > " \
        "%s/%s/tournaments/%s-tournament.json" % (str(user), str(apikey), str(owner), str(name),
                                                     str(target), str(name), str(name)))
    os.system(
        "curl -XGET -k -v https://%s:%s@api.challonge.com/v1/tournaments/%s-%s/participants.json " \
        "| python3 -m json.tool > " \
        "%s/%s/participants/%s-participants.json" % (str(user), str(apikey), str(owner), str(name),
                                                        str(target), str(name), str(name)))
    os.system(
        "curl -XGET -k -v https://%s:%s@api.challonge.com/v1/tournaments/%s-%s/matches.json " \
        "| python3 -m json.tool > " \
        "%s/%s/matches/%s-matches.json" % (str(user), str(apikey), str(owner), str(name),
                                              str(target), str(name), str(name)))

    print("Completed Fetching Challonge Brackets")

if __name__ == "__main__":

    user = "algolagniac"
    apikey = "L6p4JuLEnPL3Dna41T0oyt0Uaxns6muRxxYuIsZ0"
    owner = "tourney_locator"
    tour_name = "usw38_redemption"
    target = "example1"

    if not os.path.isdir("%s/%s" %(target, tour_name)):
        os.makedirs("%s/%s" % (target, tour_name))
        os.mkdir("%s/%s/tournaments" % (target, tour_name))
        os.mkdir("%s/%s/matches" % (target, tour_name))
        os.mkdir("%s/%s/participants" % (target, tour_name))

    challonge_scrape(user, apikey, owner, tour_name, target)
