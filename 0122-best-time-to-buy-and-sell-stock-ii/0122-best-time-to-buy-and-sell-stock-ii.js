/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
   let profit = 0, i = 0
   while(i < prices.length) {
    let minPrice = prices[i], j = i + 1
    while(j < prices.length && prices[j] > prices[j-1]) {
        j++
    }
    profit += prices[j-1] - prices[i]
    i = j
   }
   return profit 
};