/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
   let minPrice = prices[0], previousPrice = prices[0], profit = 0
   for (let i = 1; i < prices.length; i++) {
        if(prices[i] < previousPrice) {
            profit += Math.max(0, previousPrice - minPrice)
            minPrice = prices[i]
        }
        previousPrice = prices[i]
   }
   profit += Math.max(0, previousPrice - minPrice)
   return profit 
};