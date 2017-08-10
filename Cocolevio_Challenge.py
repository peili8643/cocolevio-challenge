#Cocolevio Interview Challenge

#In our Materials Marketplace we have many different companies all looking
#for the same material. However, each company is looking for a specific
#quantity of the material at a price they set themselves. A company approaches
#our team with a large amount of that material, but not enough to complete
#every request for it. Given the total amount of the material they have, the
#company asks us to find out what companies they should sell to in order to
#maximize their profits. This scenario happens frequently so we need to be able
#to compute the answer relatively quickly and with minimal processing power.

def findMaxProfit(profitCombination):

    maxProfit = profitCombination[0]

    for index in range(len(profitCombination)):
        #the only combination possible will be the best combination
        if len(profitCombination) == 1:
            bestCombination = index
            
        if profitCombination[index] > maxProfit:
            maxProfit = profitCombination[index]
            #keep track of which combination had the highest profit
            bestCombination = index

    return (bestCombination)

    
#returns a list of all the combinations of ways to sum to a specific value
#given a set of numbers
def findSumCombo(numbers, target, partial=[],combination=[]):
    s = sum(partial)
    
    # check if the partial sum is equals to target
    if s == target:
        combination.append(partial)
    else:
        for index in range(len(numbers)):
            n = numbers[index]
            remaining = numbers[index+1:]
            findSumCombo(remaining, target, partial + [n]) 

    return(combination)

#finds the corresponding company name given a list of the amounts
def findCompany(totalCompanies,amountList):

    companies = []
    
    for item in amountList:
        companies.append(totalCompanies[item-1])

    print("The list of companies you should choose from is:", companies)
    
def main():

    #given data
    company = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    amount = [1,2,3,4,5,6,7,8,9,10]
    price = [1,5,8,9,10,17,17,20,24,30]
    
    totalMaterials = int(input("Enter total amount of materials: "))

    #if the total amount of materials is enough for everyone, then all companies get what they want
    if totalMaterials > sum(amount):
        print("The list of companies you should choose from is all of them:", company)
    else:
        #finding all the combinations so the amount adds up to the total materials
        amountCombination = findSumCombo(amount,totalMaterials)
        profitCombination = []

        #finding all the combinations of different profits using the different amounts
        for index in range(len(amountCombination)):
            testCombo = amountCombination[index]
            profit = 0
            #finding the corresponding price to the item amount
            for item in testCombo:
                profit += price[item-1]
                
            profitCombination.append(profit)

        bestCombo = findMaxProfit(profitCombination)

        bestAmounts = amountCombination[bestCombo]

        findCompany(company,bestAmounts)

main()


