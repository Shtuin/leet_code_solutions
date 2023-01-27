class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        import re
        a = []
        for i in range(0, len(emails)):
            b = re.sub(r"(.{1,1000})(@)(.{1,1000})", r"\1", emails[i])
            c = re.sub(r"(.{1,1000})(@)(.{1,1000})", r"\2\3", emails[i])
            b = re.sub(r"([+])(.{1,1000})", "", b)
            b = re.sub(r"([.])", "", b)
            a.append(b+c)
        return len(set(a))