class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('.')
            local = ''.join(local)
            local = local.split('+')
            local = local[0]
            email = local +'@'+  domain
            uniqueEmails.add(email)
        return len(uniqueEmails)