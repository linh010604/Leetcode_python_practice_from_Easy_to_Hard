class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        if purchaseAmount % 10 == 0 :
            return 100 - purchaseAmount
        elif purchaseAmount % 10 < 5 :
            return 100 - purchaseAmount + purchaseAmount%10
        else :
            return 100 - purchaseAmount - 10 + purchaseAmount%10
