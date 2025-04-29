skore = [10,51,23,14,25,35,47,58,45,24,]
print(skore)
print(("průmer:"),sum(skore)/10)
print(("nejvíce:"),max(skore))
print(("nejméně:"),min(skore))
if sum(skore) > 500:
    print("výborná práce")
elif sum(skore) < 500:
    print("Můžete to příště zkusit lépe.")    