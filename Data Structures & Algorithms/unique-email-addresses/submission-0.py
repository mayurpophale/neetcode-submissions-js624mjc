class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        un_email = set()
        for email in emails:
            local,domain = email.split('@')

            local = local.split('+')[0]
            local = local.replace('.','')

            un_email.add(local+'@'+domain)

        return len(un_email)