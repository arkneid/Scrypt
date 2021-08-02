# coding=utf-8

#########################
# Author: João Chaminé  #
#########################

# imports
import pymsteams


class Teams:
    def __init__(self, text, title):
        self.webhook = "https://multicertcom.webhook.office.com/webhookb2/8c53d0b7-f59d-4301-9f37-f678c7207640" \
                       "@2edf7faa-5af2-45b6-afc3-1c9dc44a7c3c/IncomingWebhook/1ab6c57d34ac4d2e8628b917c67f0549" \
                       "/5e1a96e7-8200-4207-a0b6-2d1a08d13ace"
        self.text = text
        self.title = title

    def send_teams_message(self):
        # Send message to teams
        myTeamsMessage = pymsteams.connectorcard(f"{self.webhook}")
        myTeamsMessage.title(f"{self.title}")
        myTeamsMessage.text(f"{self.text}")
        myTeamsMessage.send()
