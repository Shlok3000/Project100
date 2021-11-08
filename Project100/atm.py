class Atm(object):
    def __init__(self, CashWithdrawl, BalanceEnquiry, CashDeposit):
        self.CashWithdrawl = CashWithdrawl
        self.BalanceEnquiry = BalanceEnquiry
        self.CashDeposit = CashDeposit

    def openBalance(self):
        print("Open Bank account")

    def closeBalance(self):
        print("Close Bank account")

Americanexpress = Atm("$60", "$80,000", "$700")
Americanexpress.openBalance()
print(Americanexpress.BalanceEnquiry)
Americanexpress.closeBalance()
    