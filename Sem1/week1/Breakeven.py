#Define Variables
CostProduce = float(20.00)
SalePricePerItem = float(40.00)
FixCost = float(50000.00)
ProPerItem = float(00.00)
print ("Cost to produce eash item: ", CostProduce)
print ("Sale price for each item: ", SalePricePerItem)
print ("Fixed Costs: ", FixCost)

#calculates profit and item cost rom the sale price
ProPerItem = float(SalePricePerItem / 2)
ItemCost = float(SalePricePerItem / 2)
print ("Profit per item: ", ProPerItem)

##Break even calculation

#dose the subtraction
Beven1 = float(SalePricePerItem - ItemCost)

#Break even final calculation
BevenFinal = float(FixCost / Beven1)
print ("Breakeven: ", BevenFinal, "items.")
