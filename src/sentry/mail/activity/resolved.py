from .base import ActivityEmail


class ResolvedActivityEmail(ActivityEmail):
    def get_activity_name(self):
        return "Resolved Issue"

    def get_description(self):
        return "{author} marked {an issue} as resolved"

    def get_category(self):
        return "resolved_activity_email"
