#Cocolevio Interview Challenge

#In our Materials Marketplace we have many different companies all looking
#for the same material. However, each company is looking for a specific
#quantity of the material at a price they set themselves. A company approaches
#our team with a large amount of that material, but not enough to complete
#every request for it. Given the total amount of the material they have, the
#company asks us to find out what companies they should sell to in order to
#maximize their profits. This scenario happens frequently so we need to be able
#to compute the answer relatively quickly and with minimal processing power.

def findMaxProfit(totalMaterials,company,amount,price,pricePer):

    #base case of recursion
    if totalMaterials <= 10:
        maxProfit = price[totalMaterial-1]
        for index in range(len(totalMaterials)):
            pass
    #if the totalMaterials is more than 10
    else:
        pass
    
#returns a list of all the combinations of ways to sum to a specific value
#given a set of numbers
def subset_sum(numbers, target, partial=[],combination=[]):
    s = sum(partial)
    
    # check if the partial sum is equals to target
    if s == target:
        combination.append(partial)
    else:
        for index in range(len(numbers)):
            n = numbers[index]
            remaining = numbers[index+1:]
            subset_sum(remaining, target, partial + [n]) 

    return(combination)           
    
    
def main():

    #given data
    company = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    amount = [1,2,3,4,5,6,7,8,9,10]
    price = [1,5,8,9,10,17,17,20,24,30]

    #finding price per unit of material
    pricePer = []
    for index in range(len(amount)):
        pricePer.append(price[index]/amount[index])
    print(pricePer)
    
    
    totalMaterials = int(input("Enter total amount of materials: "))

    #finding all the combinations so the amount adds up to the total materials
    amountCombination = subset_sum(amount,totalMaterials)
    profitCombination = []

    #finding all the combinations of different profits using the different amounts
    for index in range(len(amountCombination)):
        testCombo = amountCombination[index]
        profit = 0
        #finding the corresponding price to the item amount
        for item in testCombo:
            profit += price[item-1]
            
        profitCombination.append(profit)

    print(profitCombination)
    
    
main()
